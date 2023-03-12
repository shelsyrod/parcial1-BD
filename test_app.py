from unittest import mock
from app import app
import json    
from unittest.mock import MagicMock
import datetime
    
def test_app():
    mock_client = mock.Mock()
    mock_client.put_object.return_value = {'ResponseMetadata': {'HTTPStatusCode': 200}}
    result = app(None, None)
    assert result['statusCode'] == 200
    assert result['body'] == json.dumps('Se guardan los datos')
