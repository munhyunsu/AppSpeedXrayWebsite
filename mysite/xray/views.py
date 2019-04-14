from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from xray.models import Xray
from xray.serializers import XraySerializer


# Create Serializer views
class XrayView(viewsets.ModelViewSet):
    queryset = Xray.objects.all()
    serializer_class = XraySerializer


# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def archive(request):
    if request.method == 'GET':
        return render(request, 'archive.html')
