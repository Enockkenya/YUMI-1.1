import datetime
from haystack import indexes
from .models import Advert, Category


class AdvertIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    category = indexes.CharField(model_attr='category')
    location = indexes.CharField(model_attr='location')
    name = indexes.CharField(model_attr="name")
    description = indexes.CharField(model_attr="description")
    content_auto = indexes.EdgeNgramField(model_attr='content')

    def get_model(self):
        return Advert

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())



class CategoryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    slug = indexes.CharField(model_attr='slug')
    content_auto = indexes.EdgeNgramField(model_attr='content')

    def get_model(self):
        return Category

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter( created_at__lte=datetime.datetime.now())

