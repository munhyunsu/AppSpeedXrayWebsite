from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Here is a xray archive page")
