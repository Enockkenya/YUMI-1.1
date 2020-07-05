from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from pyuploadcare.dj.models import ImageGroupField, ImageField




class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ImageField(blank=True, null=True)
  
    

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('adverts:adverts_list_by_category', args=[self.slug])

class Location(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'location'
        verbose_name_plural = 'locations'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('adverts:adverts_list_by_location', args=[self.slug])

class Option(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'option'
        verbose_name_plural = 'options'

    def __str__(self):
        return self.name

class Item_condition(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Item_condition'
        verbose_name_plural = 'Item_conditions'

    def __str__(self):
        return self.name



class Advert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='location', on_delete=models.CASCADE)
    option = models.ForeignKey(Option, related_name='option', on_delete=models.CASCADE)
    item_condition = models.ForeignKey(Item_condition, related_name='item_condition', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=100, db_index=True)
    price = models.IntegerField(blank=True, null=True)
    pub_date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ImageGroupField(blank=True, null=True)
    available = models.BooleanField(default=True)
    accept_terms = models.BooleanField(default=True)




    class Meta:
        ordering = ('-pub_date', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name +'' + 'by' + '' + str(self.user)

    def snippet(self):
        return self.description[:50]

    def get_absolute_url(self):
        return reverse('adverts:advert_detail',  kwargs={"id":self.id, "slug":self.slug})

 

