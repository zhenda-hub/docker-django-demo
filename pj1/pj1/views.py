import os
from django.http.response import HttpResponse, JsonResponse


def home(request):
    # breakpoint()
    # return HttpResponse(f'home: {request.META.get('REMOTE_ADDR')}')
    return HttpResponse(f'home: {os.getenv('WEB_HOST')} , updated2')
