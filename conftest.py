# -*- coding: utf-8 -*-
import pytest
from requests import request
from fixture.application import Application




@pytest.fixture(scope = "session")
def app():
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
