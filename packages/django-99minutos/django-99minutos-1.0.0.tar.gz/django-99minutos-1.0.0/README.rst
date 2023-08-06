# django-99MINUTOS

## Starting
_These instructions will allow you to install the library in your python project._

### Current features

-   Get default payload.
-   Create shipping.

### Pre-requisitos

-   Python >= 3.7
-   Django >= 3
-   requests >= 2
***
## Installation

1. To get the latest stable release from PyPi:
```
pip install django-99minutos
```
or

2. From a build
```
git clone https://gitlab.com/linets/ecommerce/oms/integrations/django-99minutos
```

```
cd {{project}}
```

```
python setup.py sdist
```
and, install in your project django
```
pip install {{path}}/django-99MINUTOS/dist/{{tar.gz file}}
```

3. Settings in django project

```
DJANGO_99MINUTOS = {
    'XCIXMINUTOS': {
        'BASE_URL': '<99MINUTOS_BASE_URL>',
        'TOKEN': '<99MINUTOS_TOKEN>',
        'SERVICE': '<99MINUTOS_SERVICE>',
        'START_TIME': '<99MINUTOS_START_TIME>',
        'END_TIME': '<99MINUTOS_END_TIME>',
    },
    'SENDER': {
        'CD_NAME': '<99MINUTOS_CD_NAME>',
        'CD_ADDRESS': '<99MINUTOS_CD_ADDRESS>',
        'CD_COMMUNE': '<99MINUTOS_CD_COMMUNE>',
        'CD_LOCATION_ID': '<99MINUTOS_CD_LOCATION_ID>',
    }
}
```

## Usage

1. Create instance to be sent
    ```
    import json
    from types import SimpleNamespace

    dict_ = {
        'shipments': [
            {
                'internalKey': '',
                'deliveryType': 'NXD',
                'sender': {
                    'firstName': 'Esteban',
                    'lastName': 'Ramirez',
                    'phone': '+52999999999',
                    'email': 'esteban@gmail.com'
                },
                'recipient': {
                    'firstName': 'Carlos',
                    'lastName': 'Gonzalez',
                    'phone': '+52999999999',
                    'email': 'esteban@gmail.com'
                },
                'origin': {
                    'address': 'Av. del Taller 451, Jardín Balbuena, Álvaro Obregón, 15900 Ciudad de México, CDMX, México',
                    'country': 'MEX',
                    'reference':'Primer Piso',
                    'zipcode': '15900'
                },
                'destination': {
                    'address': 'Av 9 Pte 308, Centro histórico de Puebla, Puebla, Pue., México',
                    'reference':'Torre 3 Apartamente 905',
                    'country': 'MEX',
                    'zipcode': '72000'
                },
                'payments': {
                    'paymentMethod': 'monthly'
                },
                'options': {
                    'pickUpAfter':'2022-02-01T08:00:00.000Z',
                    'deliveryBetween': {
                       'start':'2022-02-02T12:00:00.000Z',
                       'end':'2022-02-02T20:00:00.000Z'
                    },
                    'requiresIdentification': False,
                    'requiresSignature': False,
                    'twoFactorAuth': False,
                    'notes':'**Information to be printed on the label**'
                },
                'items': [
                    {
                        'size': 's',
                        'description': 'lorem ipsum',
                        'weight': 1000,
                        'length': 50,
                        'width': 30,
                        'height': 20
                    }
                ]
            }
        ],
        'draft': False
    }

    instance = json.loads(json.dumps(dict_), object_hook=lambda attr: SimpleNamespace(**attr))
    ```

2. Get default payload:
```
from XCIXminutos.handler import XCIXMinutosHandler

handler = XCIXMinutosHandler()
default_data = handler.get_default_payload(<instance>)
```

3. Create shipping:
```
from XCIXminutos.handler import XCIXMinutosHandler

handler = XCIXMinutosHandler()
default_data = handler.create_shipping(<default_data>)
```

4. Get events:
```
from XCIXminutos.handler import XCIXMinutosHandler

handler = XCIXMinutosHandler()

raw_data = {
    '_id': {
        '$oid': '636142b3ba74ddfba5152d3e'
    },
    'request': {
        'url': 'https://api.bendo.app/api/wh/99minutosv3/',
        'headers': {
            'Authorization': 'Basic KEY',
            'Content-Type': 'application/json',
            'User-Agent': '99notifications'
        },
        'body': {
            'statusname': 'onRoadToDelivery',
            'trackingid': '7250229709',
            'internalkey': '786-A1D-D33',
            'events': [
                {
                    'statuscode': '1002',
                    'statusname': 'confirmed',
                    'data': {
                        'comment': 'NEW_ORDER_CONFIRMED',
                        'evidence': []
                    },
                    'createdat': '2022-10-31 15:16:09'
                },
                {
                    'statuscode': '2003',
                    'statusname': 'collected',
                    'data': {
                        'comment': 'Recolectada por el veloz Don Veloz 99m B 3ed6433',
                        'evidence': []
                    },
                    'createdat': '2022-10-31 19:17:58'
                },
                {
                    'statuscode': '3001',
                    'statusname': 'stored',
                    'data': {
                        'comment': 'En estación MX0 por módulo de inducción',
                        'evidence': []
                    },
                    'createdat': '2022-11-01 06:02:25'
                },
                {
                    'statuscode': '3002',
                    'statusname': 'onContainer',
                    'data': {
                        'comment': 'Contenerizado en la estación MX0 en el contenedor VIH-131 en el finger F4',
                        'evidence': []
                    },
                    'createdat': '2022-11-01 06:35:31'
                },
                {
                    'statuscode': '3003',
                    'statusname': 'chargedToVehicle',
                    'data': {
                        'comment': 'Subida al line haul del veloz Juan Carlos, Enciso Ahuatzi con las placas LE17833 en la estacion MX0 dentro del contenedor VIH-131',
                        'evidence': []
                    },
                    'createdat': '2022-11-01 09:54:15'
                },
                {
                    'statuscode': '3004',
                    'statusname': 'onLinehaul',
                    'data': {
                        'comment': 'Despachado de la estación MX0 hacia la estación MX3, en el line haul del veloz Juan Carlos, Enciso Ahuatzi con las placas LE17833 en el contenedor VIH-131',
                        'evidence': []
                    },
                    'createdat': '2022-11-01 10:22:47'
                },
                {
                    'statuscode': '3001',
                    'statusname': 'stored',
                    'data': {
                        'evidence': [],
                        'comment': 'En estación final MX3 por módulo de inducción'
                    },
                    'createdat': '2022-11-01 11:40:19'
                },
                {
                    'statuscode': '4001',
                    'statusname': 'onRoadToDelivery',
                    'data': {
                        'comment': 'Asignación masiva al veloz: Felipe Ramirez Zepeda por: nancy.concepcion en la estación: Alvaro Obregón el número de orden 7250229709',
                        'evidence': []
                    },
                    'createdat': '2022-11-01 16:00:50'
                }
            ]
        }
    }

response = handler.get_events(raw_data)

Output:
[{
    'city': 'Santiago'
    'state': 'RM',
    'description': 'Llego al almacén',
    'date': '12/12/2021'
}]
```

5. Get status and if "is_delivered":
```
from XCIXminutos.handler import XCIXMinutosHandler

handler = XCIXMinutosHandler()

raw_data = {
    '_id': {
        '$oid': '636142b3ba74ddfba5152d3e'
    },
    'request': {
        'url': 'https://api.bendo.app/api/wh/99minutosv3/',
        'headers': {
            'Authorization': 'Basic KEY',
            'Content-Type': 'application/json',
            'User-Agent': '99notifications'
        },
        'body': {
            'statusname': 'onRoadToDelivery',
            'trackingid': '7250229709',
            'internalkey': '786-A1D-D33',
            'events': [
                {
                    'statuscode': '1002',
                    'statusname': 'confirmed',
                    'data': {
                        'comment': 'NEW_ORDER_CONFIRMED',
                        'evidence': []
                    },
                    'createdat': '2022-10-31 15:16:09'
                },
                {
                    'statuscode': '2003',
                    'statusname': 'collected',
                    'data': {
                        'comment': 'Recolectada por el veloz Don Veloz 99m B 3ed6433',
                        'evidence': []
                    },
                    'createdat': '2022-10-31 19:17:58'
                },
                {
                    'statuscode': '3001',
                    'statusname': 'stored',
                    'data': {
                        'comment': 'En estación MX0 por módulo de inducción',
                        'evidence': []
                    },
                    'createdat': '2022-11-01 06:02:25'
                },
                {
                    'statuscode': '3002',
                    'statusname': 'onContainer',
                    'data': {
                        'comment': 'Contenerizado en la estación MX0 en el contenedor VIH-131 en el finger F4',
                        'evidence': []
                    },
                    'createdat': '2022-11-01 06:35:31'
                },
                {
                    'statuscode': '3003',
                    'statusname': 'chargedToVehicle',
                    'data': {
                        'comment': 'Subida al line haul del veloz Juan Carlos, Enciso Ahuatzi con las placas LE17833 en la estacion MX0 dentro del contenedor VIH-131',
                        'evidence': []
                    },
                    'createdat': '2022-11-01 09:54:15'
                },
                {
                    'statuscode': '3004',
                    'statusname': 'onLinehaul',
                    'data': {
                        'comment': 'Despachado de la estación MX0 hacia la estación MX3, en el line haul del veloz Juan Carlos, Enciso Ahuatzi con las placas LE17833 en el contenedor VIH-131',
                        'evidence': []
                    },
                    'createdat': '2022-11-01 10:22:47'
                },
                {
                    'statuscode': '3001',
                    'statusname': 'stored',
                    'data': {
                        'evidence': [],
                        'comment': 'En estación final MX3 por módulo de inducción'
                    },
                    'createdat': '2022-11-01 11:40:19'
                },
                {
                    'statuscode': '4001',
                    'statusname': 'onRoadToDelivery',
                    'data': {
                        'comment': 'Asignación masiva al veloz: Felipe Ramirez Zepeda por: nancy.concepcion en la estación: Alvaro Obregón el número de orden 7250229709',
                        'evidence': []
                    },
                    'createdat': '2022-11-01 16:00:50'
                }
            ]
        }
    }

response = handler.get_status(raw_data)

Output:
('Entregado', True)
```
