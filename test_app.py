from unittest import mock
from app import app
import json

def test_app():
    with mock.patch("__main__.peticion") as mock_peticion:
        mock_peticion.return_value = "datos_mockeados"
        result = app(None, None)
    assert result['statusCode'] == 200
    assert result['body'] == json.dumps('Se guardan los datos')
