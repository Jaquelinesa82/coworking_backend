import factory
from faker import Faker
from auth_app.models import CustomUser
import uuid

fake = Faker()


class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    email = factory.LazyAttribute(lambda _: f"{fake.unique.email()}_{uuid.uuid4()}")
    password = factory.PostGenerationMethodCall('set_password', '101010')
    first_name = factory.LazyAttribute(lambda _: fake.first_name())
    last_name = factory.LazyAttribute(lambda _: fake.last_name())
