from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)  # Replace with a User model
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'Booking for {self.listing.title} by {self.user}'

class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)  # Replace with a User model
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'Review for {self.listing.title} by {self.user}'

# Create your models here.
