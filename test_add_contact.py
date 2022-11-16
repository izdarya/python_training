# -*- coding: utf-8 -*-

import pytest
from contact import Contact
from application_contact import Apllication_contact

@pytest.fixture
def app(request):
    fixture =Apllication_contact()
    request.addfinalizer(fixture.destroy)
    return fixture
def test_add_contact(app):

    app.login(username="admin", password="secret")
    app.add_contact(Contact(first="Dasha", middle="Dasha", last="Dasha", nickname="Dasha", company="Test", title="Test", address="Test", telephone_home="2-22-22", telephone_mobile="8-977-983-01-25",
                         telephone_work="Test", email="Test@test.ru", birthday_year="1994", address_s="Test", home="Test", notes="Test", birthday_day="8", birthday_month="June"))
    app.logout()




