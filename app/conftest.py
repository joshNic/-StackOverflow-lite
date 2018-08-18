import pytest
from app.view import create_app
import json

@pytest.fixture
def app():
    app = create_app()
    app.debug = True
    return app
