import mock
import pytest

from acf.errors.http import RequestError
from acf.protocols.base import BaseProtocol
from acf.protocols.http import HttpProtocol


def test_base_protocol_execute():
    with pytest.raises(NotImplementedError):
        BaseProtocol().execute()


def test_http_protocol_execute(requests_mock):
    url = 'http://test.com'
    method = 'get'
    expected_response = 'some response'

    requests_mock.request(method, url, text=expected_response)
    response = HttpProtocol().execute(method=method, url=url)

    assert response.text == expected_response

    # test a failed request
    target = 'acf.protocols.http.HttpProtocol._perform_request'
    with mock.patch(target, side_effect=Exception()):
        with pytest.raises(RequestError):
            response = HttpProtocol().execute(method=method, url=url)
