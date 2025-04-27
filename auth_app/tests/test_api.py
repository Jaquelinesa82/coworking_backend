from auth_app.models import CustomUser
from rest_framework.test import APIClient
import pytest
from auth_app.factories import CustomUserFactory
from faker import Faker

fake = Faker()


@pytest.mark.django_db(transaction=True)
def test_register_user():
    client = APIClient()

    email = fake.unique.email()
    first_name = fake.first_name()
    last_name = fake.last_name()

    payload = {
        'email': email,
        'password': '101010',
        'first_name': first_name,
        'last_name': last_name,
    }

    response = client.post('/auth_app/register/', payload, format='json')

    print(f'dados: {response.data}')

    assert response.status_code == 201
    assert response.data['email'] == payload['email']


@pytest.mark.django_db
def test_login_user():
    client = APIClient()
    user = CustomUserFactory()

    payload = {'email': user.email, 'password': '101010'}

    response = client.post('/auth_app/login/', payload, format='json')

    assert response.status_code == 200
    assert response.data['message'] == 'Login success'


@pytest.mark.django_db
def test_list_user():
    client = APIClient()

    CustomUserFactory()

    response = client.get('/auth_app/list_user/', {}, format='json')

    assert response.status_code == 200
    assert len(response.data) > 0


@pytest.mark.django_db
def test_update_user():
    client = APIClient()

    user = CustomUserFactory()
    email = fake.unique.email()
    first_name = fake.first_name()
    last_name = fake.last_name()

    payload = {
        'email': email,
        'password': '101010',
        'first_name': first_name,
        'last_name': last_name,
    }

    response = client.put(f'/auth_app/update_user/{user.pk}/', payload, format='json')

    assert response.status_code == 200


@pytest.mark.django_db
def delete_user():
    client = APIClient()
    user = CustomUserFactory()

    response = client.delete(f'/auth_app/delete_user/{user.pk}', user, format='json')

    assert response.status_code == 204
