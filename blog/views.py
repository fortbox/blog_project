from django.shortcuts import render
import logging
# from blog_project import settings
from django.conf import settings

logger = logging.getLogger("blog.views")


# Create your views here.
def global_setting(request):
    return {
        'SITE_URL': settings.SITE_URL,
        'SITE_NAME': settings.SITE_NAME,
    }


def index(request):
    try:
        file = open("a.txt", 'r')
    except Exception as e:
        logger.error(e)
    return render(request, "index.html", locals())
