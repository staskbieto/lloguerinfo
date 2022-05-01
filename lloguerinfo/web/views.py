from django.http import HttpResponse
from web.cron import run_scrapy_fotocasa


def health(request):
    run_scrapy_fotocasa()
    return HttpResponse("Hello, World!")
