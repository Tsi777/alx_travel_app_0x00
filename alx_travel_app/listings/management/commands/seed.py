from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        # Logic to create Listings
        Listing.objects.create(title='Sample Listing', description='Description', price=100.00)
