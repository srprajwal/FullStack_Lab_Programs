import datetime
from django.http import HttpResponse


def currDate(request):
    now = datetime.datetime.now()
    res = "<h1>%s</h1>"%now
    return HttpResponse(res)
