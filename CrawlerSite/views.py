from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the start of the Auto Crawler project site.")