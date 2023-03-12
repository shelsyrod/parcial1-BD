from unittest import mock
from app import app
import json    
from unittest.mock import MagicMock
import datetime

def test_app():
    # Simulamos la respuesta de la función peticion
    datos_mock = "datos de prueba"
    peticion_mock = MagicMock(return_value=datos_mock)
    
    # Simulamos la conexión al bucket de S3
    bucket_mock = MagicMock()
    put_object_mock = MagicMock()
    bucket_mock.put_object = put_object_mock
    
    # Ejecutamos la función app con los mocks
    with patch("app.peticion", peticion_mock):
        with patch("boto3.resource") as resource_mock:
            resource_mock.return_value.Bucket.return_value = bucket_mock
            app({}, {})
    
    # Verificamos que se haya llamado a la función put_object del bucket de S3
    put_object_mock.assert_called_once_with(Key=nombre, Body=datos_mock)
    
    # Verificamos que la función app no devuelva ningún valor
    assert app({}, {}) is None
