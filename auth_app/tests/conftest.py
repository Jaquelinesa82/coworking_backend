import pytest
from auth_app.models import CustomUser


@pytest.fixture(autouse=True)
def auto_cleanup(db):
    yield
    print("🔄 Limpando dados...")
    CustomUser.objects.all().delete()
