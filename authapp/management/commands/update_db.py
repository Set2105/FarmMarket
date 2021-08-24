from django.core.management.base import BaseCommand
from authapp.models import CustomerUser
from authapp.models import CustomerUserProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = CustomerUser.objects.all()
        for user in users:
            users_profile = CustomerUserProfile.objects.create(user=user)
            users_profile.save()
