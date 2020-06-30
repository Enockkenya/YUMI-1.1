from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from cloudinary.models import CloudinaryField

COUNTY_CATEGORY_TYPES = (
('Kenya', 'Kenya'),
('Lesotho', 'Lesotho'),
('Liberia', 'Liberia'),
('Libya', 'Libya'),
('Madagascar', 'Madagascar'),
('Malawi', 'Malawi'),
('Mali', 'Mali'),
('Mauritania', 'Mauritania'),
('Mauritius', 'Mauritius'),
('Morocco', 'Morocco'),
('Mozambique', 'Mozambique'),

)
TOWN_CATEGORY_TYPES = (
('Nairobi','Nairobi'),
('Niger', 'Niger'),
('Nigeria', 'Nigeria'),
('Rwanda', 'Rwanda'),
('Sao Tome and Principe', 'Sao Tome and Principe'),
('Senegal', 'Senegal'),
('Seychelles', 'Seychelles'),
('Sierra Leone', 'Sierra Leone'),
('Somalia', 'Somalia'),
('South Africa', 'South Africa'),
('South Sudan', 'South Sudan'),
('Sudan', 'Sudan'),
('Tanzania', 'Tanzania'),
('Togo', 'Togo'),
('Tunisia', 'Tunisia'),
('Uganda', 'Uganda' ),
('Zambia', 'Zambia' )
)

class PrivateMessage(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=127)
    text = models.TextField()
    sent_date = models.DateField(auto_now_add=True, null=True)
    to_address = models.CharField(max_length=255)
    from_address = models.CharField(max_length=255)
    
    def __str__(self):
        return "From: " + self.from_address + " To: " + self.to_address + " Title: " + self.title
    
    class Meta:
        db_table = 'at_private_messages'



class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic =  CloudinaryField('image', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=4, blank=True, null=True)
    county = models.CharField(max_length=127, choices=COUNTY_CATEGORY_TYPES,  blank=True,null=True,  default='Kenya')
    phone_number = models.IntegerField(blank=True, null=True)
    town = models.CharField(max_length=127, choices=TOWN_CATEGORY_TYPES,  blank=True,null=True,  default='Nairobi')
 
    
    def __str__(self):
        return self.user.first_name + " " + \
                          self.user.last_name 
  

    def create_client_profile(sender, **kwargs):
        if kwargs['created']:
            client = Client.objects.create(user=kwargs['instance'])

    post_save.connect(create_client_profile, sender=User)