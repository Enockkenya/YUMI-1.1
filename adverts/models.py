from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
import datetime



from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', blank=True, null=True)
  
    

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def adverts_in_category(self):
        return self.adverts.all().count()
        

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

class Tag(models.Model):
    name = models.CharField(max_length=150, db_index=True)


    class Meta:
        ordering = ('name', )
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name

class Advert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='adverts', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='adverts', on_delete=models.CASCADE)
    option = models.ForeignKey(Option, related_name='adverts', on_delete=models.CASCADE)
    item_condition = models.ForeignKey(Item_condition, related_name='item_condition', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, db_index=True)
    price = models.PositiveIntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image')
    available = models.BooleanField(default=True)
    likes = models.ManyToManyField(User, related_name='post_likes')
    accept_terms = models.BooleanField(default=True)
    
   



    class Meta:
        ordering = ('-pub_date', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name +'' + 'by' + '' + str(self.user)

    def snippet(self):
        return self.description[:50]


    @property
    def total_likes(self):
        return self.likes.count()
    
    
    

    def get_absolute_url(self):
        return reverse('adverts:advert_detail',  kwargs={"id":self.id, "slug":self.slug})







class Review(models.Model):
    """This class creates an ads reviewing odel."""

    reviewer = models.ForeignKey(
        User,
        related_name='client_review',
        on_delete=models.CASCADE
    )
    adseller = models.ForeignKey(
       User,
        related_name='seller_reviews',
        on_delete=models.CASCADE
    )
    review = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    def reviewer_name(self):
        """This method gets the username of the user reveiwing  advert ."""
        return self.user.username
    
    def __str__(self):
        return self.review + '' + 'by' + '' + str(self.reviewer) + '' + 'for' + ' ' + str(self.adseller)

    