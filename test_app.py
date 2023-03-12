from unittest import mock
from app import app
import json

def test_app():
    # Creamos una instancia del objeto Mock para la función 'peticion'
    peticion_mock = mock.Mock(return_value="Estos son los datos de la petición")
    
    # Configuramos la función 'boto3.resource' para que retorne una instancia de nuestra clase Mock
    with mock.patch('boto3.resource', return_value=MockS3Bucket()):
        # Configuramos la función 'peticion' para que retorne un valor específico
        with mock.patch('my_module.peticion', peticion_mock):
            # Llamamos a la función 'app' con argumentos dummy
            result = app("event", "context")
    
    # Verificamos que la función 'peticion' fue llamada una vez
    peticion_mock.assert_called_once()
    
    # Verificamos que se llamó a la función 'put_object' de nuestro objeto Mock
    assert MockS3Bucket().put_object.called_once()
    
    # Verificamos que la respuesta de la función 'app' es la esperada
    assert result == {
        'statusCode': 200,
        'body': json.dumps('Se guardan los datos')
    }
