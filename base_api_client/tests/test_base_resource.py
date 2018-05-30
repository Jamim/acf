import pytest

from base_api_client.error.base import UnknownActionError
from base_api_client.resource.base import BaseResource


def test_base_resource_getattr():
    class Resource(BaseResource):
        ACTIONS = {'get': list}

    resource = Resource()

    assert isinstance(resource.get, list)

    with pytest.raises(UnknownActionError):
        resource.unknown_action