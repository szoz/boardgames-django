import pytest
from rest_framework.test import APIClient


@pytest.fixture(scope="class")
def api_client():
    """Create and return DRF test client."""
    return APIClient()
