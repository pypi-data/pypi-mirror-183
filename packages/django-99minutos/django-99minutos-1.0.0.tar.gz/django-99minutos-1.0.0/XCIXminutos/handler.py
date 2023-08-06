# -*- coding: utf-8 -*-
import logging

from XCIXminutos.connector import Connector, ConnectorException
from XCIXminutos.settings import api_settings

logger = logging.getLogger(__name__)


class XCIXMinutosHandler:
    """
        Handler to send shipping payload to 99minutos
    """

    def __init__(self, base_url=api_settings.XCIXMINUTOS['BASE_URL'],
                 client_id=api_settings.XCIXMINUTOS['CLIENT_ID'],
                 client_secret=api_settings.XCIXMINUTOS['CLIENT_SECRET'],
                 token=api_settings.XCIXMINUTOS['TOKEN'],
                 verify=True, **kwargs):

        self.base_url = kwargs.pop('base_url', base_url)
        self.client_id = kwargs.pop('client_id', client_id)
        self.client_secret = kwargs.pop('client_secret', client_secret)
        self.token = kwargs.pop('token', token)
        self.verify = kwargs.pop('verify', verify)
        self.connector = Connector(self._headers(), verify_ssl=self.verify)

    def _login(self):
        url = f'{self.base_url}oauth/token'
        credentials = {'client_id': self.client_id, 'client_secret': self.client_secret}

        response = self.connector.post(url, credentials)
        return response

    def _headers(self):
        """
            Here define the headers for all connections with 99minutos.
        """
        return {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json',
        }

    def get_shipping_label(self):
        raise NotImplementedError(
            'get_shipping_label is not a method implemented for XCIXMinutosHandler')

    def get_default_payload(self, instance):
        """
            This method generates by default all the necessary data with
            an appropriate structure for 99minutos courier.
        """

        payload = {
            'shipments': [
                {
                    'internalKey': '',
                    'deliveryType': api_settings.XCIXMINUTOS['DELIVERY_TYPE'],
                    'sender': {
                        'firstName': api_settings.SENDER['FIRST_NAME'],
                        'lastName': api_settings.SENDER['LAST_NAME'],
                        'phone': api_settings.SENDER['PHONE'],
                        'email': api_settings.SENDER['EMAIL'],
                    },
                    'recipient': {
                        'firstName': instance.customer.first_name or instance.customer.full_name,
                        'lastName': instance.customer.last_name,
                        'phone': f'+56{instance.customer.phone}',
                        'email': api_settings.SENDER['EMAIL'],
                    },
                    'origin': {
                        'address': api_settings.SENDER['ADDRESS'],
                        'country': api_settings.SENDER['COUNTRY_CODE'],
                        'reference': api_settings.SENDER['REFERENCE'],
                        'zipcode': api_settings.SENDER['ZIPCODE'],
                    },
                    'destination': {
                        'address': f"{instance.address.full_address}, {instance.commune.name}, {instance.region.name}, {api_settings.SENDER['COUNTRY_NAME']}",
                        'reference': '',
                        'country': api_settings.SENDER['COUNTRY_CODE'],
                        'zipcode': instance.commune.zone_code
                    },
                    'payments': {
                        'paymentMethod': 'monthly'
                    },
                    'options': {},
                    'items': [
                        {
                            'size': 's',
                            'description': item.name,
                            'weight': 1000,
                        } for item in instance.items
                    ]
                }
            ],
            'draft': False
        }

        logger.debug(payload)
        return payload

    def create_shipping(self, data):
        """
            This method generate a 99minutos shipping.
            If the get_default_payload method returns data, send it here,
            otherwise, generate your own payload.
        """

        url = f'{self.base_url}orders'
        logger.debug(data)

        try:
            response = self.connector.post(url, data)
            response.update({
                'tracking_number': response['data']['shipments'][0]['trackingId'],
            })
            return response

        except ConnectorException as error:
            logger.error(error)

            raise ConnectorException(error.message, error.description, error.code) from error

    def get_tracking(self, identifier):
        raise NotImplementedError(
            'get_tracking is not a method implemented for XCIXMinutosHandler')

    def get_events(self, raw_data):
        """
            This method obtain array events.
            structure:

            file -> README.md

            return [{
                'statuscode': '1002',
                'statusname': 'confirmed',
                'data': {
                    'comment': 'NEW_ORDER_CONFIRMED',
                    'evidence': []
                },
                'createdat': '2022-10-31 15:16:09'
            }]
        """
        return raw_data['request']['body']['events']

    def get_status(self, raw_data):
        """
            This method returns the status of the order and "is_delivered".
            structure:

            file -> README.md

            status: [
                'CONFIRMED', 'COLLECTED', 'STORED', 'ON_LINEHAUL',
                'ON_ROAD_TO_DELIVERY', 'DELIVERED'
            ]

            response: ('DELIVERED', True)
        """

        status = raw_data['request']['body']['events'][-1]['statusname'].upper()
        is_delivered = False

        if status == 'DELIVERED':
            is_delivered = True

        return status, is_delivered
