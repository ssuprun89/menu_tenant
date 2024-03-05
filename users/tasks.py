import datetime

from clients.models import Client, Domain, ClientBrand, ClientContact, ClientsHours
from users.models import User, UserClient


def create_user(user_id, organization_name):
    user = User.objects.get(id=user_id)
    time = str(datetime.datetime.utcnow().timestamp()).replace(".", "")
    client = Client.objects.create(schema_name=f"s_{time}", name=organization_name)
    UserClient.objects.create(user=user, client=client, role=UserClient.UserRole.OWNER)
    Domain.objects.create(tenant=client, is_primary=True)
    ClientBrand.objects.create(tenant=client)
    ClientContact.objects.create(tenant=client)
    for i in range(1, 8):
        ClientsHours.objects.create(tenant=client, day_number=i, time_from="08:00", time_by="22:00")
