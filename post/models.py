from django.urls import reverse
from django.db import models


class OfferType(models.Model):
    type = models.CharField('Offer type', max_length=50)

    def __str__(self):
        return self.type

class PropertyType(models.Model):
    type = models.CharField('Property type', max_length=50)

    def __str__(self):
        return self.type

class ConstructionType(models.Model):
    type = models.CharField('Construction type', max_length=50)

    def __str__(self):
        return self.type

class Heating(models.Model):
    type = models.CharField('Heating', max_length=50)

    def __str__(self):
        return self.type

class Post(models.Model):
    title = models.CharField('Title', max_length=150)
    location = models.CharField('Location', max_length=50)
    price = models.IntegerField('Price')
    neighborhood = models.CharField('Neighborhood', max_length=60, blank=True)
    square_meters = models.IntegerField('Square meters')
    number_of_rooms = models.IntegerField('Number of rooms', null=True, blank=True)
    bathroom = models.IntegerField('Bathroom', null=True, blank=True)
    bedroom = models.IntegerField('Bedroom', null=True, blank=True)
    balcony = models.IntegerField('Balcony', null=True, blank=True)
    floor = models.IntegerField('Floor', null=True, blank=True)
    parking = models.BooleanField('Parking', default=False, null=True, blank=True)
    garage = models.BooleanField('Garage', default=False, null=True, blank=True)
    basement = models.BooleanField('Basement', default=False, null=True, blank=True)
    garret = models.BooleanField('Garret', default=False, null=True, blank=True)
    created = models.DateTimeField('Created', auto_now_add=True)
    more_information = models.TextField('More information')
    for_contact = models.CharField('For contact', max_length=100, null=True)


    offer_type = models.ForeignKey(OfferType, on_delete=models.PROTECT)
    property_type = models.ForeignKey(PropertyType, on_delete=models.PROTECT)
    construction_type = models.ForeignKey(ConstructionType, on_delete=models.PROTECT, null=True, blank=True)
    heating = models.ForeignKey(Heating, on_delete=models.PROTECT, null=True, blank=True)

    main_picture = models.ImageField('Main picture', upload_to='property_pictures', default='default_property.jpg')
    picture_1 = models.ImageField('Picture 1', upload_to='property_pictures', default='default_property.jpg')
    picture_2 = models.ImageField('Picture 2', upload_to='property_pictures', default='default_property.jpg')
    picture_3 = models.ImageField('Picture 3', upload_to='property_pictures', default='default_property.jpg')
    picture_4 = models.ImageField('Picture 4', upload_to='property_pictures', default='default_property.jpg')
    picture_5 = models.ImageField('Picture 5', upload_to='property_pictures', default='default_property.jpg')
    picture_6 = models.ImageField('Picture 6', upload_to='property_pictures', default='default_property.jpg')
    picture_7 = models.ImageField('Picture 7', upload_to='property_pictures', default='default_property.jpg')
    picture_8 = models.ImageField('Picture 8', upload_to='property_pictures', default='default_property.jpg')
    picture_9 = models.ImageField('Picture 9', upload_to='property_pictures', default='default_property.jpg')
    picture_10 = models.ImageField('Picture 10', upload_to='property_pictures', default='default_property.jpg')

    def __str__(self):
        return f"{self.title} - {self.location} - {self.price}"

    def get_absolute_url(self):
        return reverse('post-details', args=(self.id,))

    class Meta:
        ordering = ['-created']

