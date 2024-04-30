from django.contrib.auth.models import User, Group

# Assign users to groups based on their roles
def assign_users_to_groups():
    admin_users = User.objects.filter(is_superuser=True)
    admin_group = Group.objects.get(name='Admins')
    admin_group.user_set.set(admin_users)

    # Similarly, assign service providers and clients to their respective groups

assign_users_to_groups()
