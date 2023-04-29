
from lambda_function import lambda_handler

def test_lambda_function():
    expected = {'statusCode': 200, 'body': '"Ya were in Lambda"'}
    result = lambda_handler('', '')

    assert result == expected
