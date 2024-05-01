from django.db import models
from django.contrib.auth.models import User


# Create your models here.
CATEGORY_CHOICES = (
    ('CR', 'Curd'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('KL', 'Kulfi'),
    ('MS', 'MilkShake'),
    ('PN', 'Paneer'),
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),
    ('IC', 'Ice-Cream'),
    
)

STATE_CHOICES = (
    ('Delta', 'Delta'),
    ('Edo', 'Edo'),
    ('Ebonyi', 'Ebonyi'),
    ('Imo', 'Imo'),
    ('Uyo', 'Uyo'),
    ('Oyo', 'Oyo'),
    ('Lagos', 'Lagos'),
    ('Ekiti', 'Ekiti'),
    ('Abia', 'Abia'),
    ('Bayelsa', 'Bayelsa'),
    ('Rivers', 'Rivers'),
    ('Cross River', 'Cross River'),
    ('Ondo', 'Ondo'),
    ('Ogun', 'Ogun'),
    ('Osun', 'Osun'),
    ('Gobe', 'Gobe'),
    ('Kano', 'Kano'),
    ('Kaduna', 'Kaduna'),
    ('Kebbi', 'Kebbi'),
    ('Adamawa', 'Adamawa'),
    ('Akwaibom', 'Akwaibom'),
    ('Anambra', 'Anambra'),
    ('Bauchi', 'Bauchi'),
    ('Benue', 'Benue'),
    ('Bonue', 'Bonue'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField(null=True, blank=True)
    discounted_price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    compisition = models.TextField(default="", null=True, blank=True)
    prodapp = models.TextField(default="", null=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, null=True, blank=True)
    product_image = models.ImageField(upload_to='product', null=True, blank=True)

    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=100, choices=STATE_CHOICES)

    def __str__(self):
        return self.name
    
