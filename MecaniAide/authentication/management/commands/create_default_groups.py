from django.contrib.auth.models import Group

# Create default groups if they don't exist
def create_default_groups():
    admin_group, _ = Group.objects.get_or_create(name='Admins')
    service_provider_group, _ = Group.objects.get_or_create(name='Service Providers')
    client_group, _ = Group.objects.get_or_create(name='Clients')

create_default_groups()
