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
        apps = Xray.objects.filter(scene_start=0).order_by('package_name')
        return render(request, 'archive.html', {'apps': apps})


def result(request):
    if request.method == 'GET':
        package = request.GET.get('package')
        apps = Xray.objects.filter(package_name=package).order_by('-experiment_date', 'scene_start')
        return render(request, 'result.html', {'apps': apps})
