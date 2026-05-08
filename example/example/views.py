import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def hello(request):
    logger.info("Hello")
    return HttpResponse("Hello World!")
