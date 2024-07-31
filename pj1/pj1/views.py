from django.http.response import HttpResponse, JsonResponse


def home(request):
    # breakpoint()
    return HttpResponse(f'home: {request.META.get('REMOTE_ADDR')}')
