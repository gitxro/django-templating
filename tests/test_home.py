from pytest_django.asserts import assertTemplateUsed


def test_html_homepage(client):

    response = client.get("/html/")

    assertTemplateUsed(response, "app.html")
    assert response.status_code == 200


def test_jinja_homepage(client):

    response = client.get("/jinja/")
    assertTemplateUsed(response, "app.jinja")

    assert response.status_code == 200
