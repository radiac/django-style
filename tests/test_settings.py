import pytest
from django.test import override_settings
from django.test.client import Client


def test_default_settings(client):
    response = client.get("/")
    assert response.status_code == 200

    context = response.context
    assert context["STYLE_BASE"] == "django_style/simple/base.html"
    assert context["STYLE_IS_APP"] is False
    assert "simple/styles.css" in response.content.decode()


@override_settings(STYLE_THEME="bootstrap", STYLE_IS_APP=True)
def test_custom_settings_applied(client):
    response = client.get("/")
    assert response.status_code == 200

    context = response.context
    assert context["STYLE_BASE"] == "django_style/bootstrap/base.html"
    assert context["STYLE_IS_APP"] is True
    assert "bootstrap/styles.css" in response.content.decode()


@override_settings(STYLE_THEME="_undefined")
def test_unknown_theme_caught(client):
    with pytest.raises(ValueError, match="Unknown django-style theme: _undefined"):
        _ = client.get("/")
