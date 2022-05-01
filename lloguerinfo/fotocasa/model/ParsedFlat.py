
from scrapy_djangoitem import DjangoItem

from web.models import FlatInfo


class Flat(DjangoItem):
    django_model = FlatInfo