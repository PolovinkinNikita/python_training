# -*- coding: utf-8 -*-
import pytest
from requests import request
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app():
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="dsfsdf", header="dfdfd", footer="dsfad"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()