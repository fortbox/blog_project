from django.shortcuts import render
import logging

logger = logging.getLogger("blog.views")


# Create your views here.
def index(request):
    try:
        file=open("a.txt",'r')
    except Exception as e:
        logger.error(e)


    return render(request, "index.html", locals())
