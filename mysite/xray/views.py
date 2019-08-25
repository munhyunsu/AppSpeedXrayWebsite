from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import viewsets
from xray.models import Xray
from xray.serializers import XraySerializer

from xray.xray_handler import send_request


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
        apps = list(set(Xray.objects.values_list('package_name', flat=True)))
        apps.sort()
        return render(request, 'archive.html', {'apps': apps})


def result(request):
    if request.method == 'GET':
        package = request.GET.get('package')
        apps = Xray.objects.filter(package_name=package).order_by('-experiment_date', 'scene_start')
        return render(request, 'result.html', {'apps': apps})


def newreq(request):
    if request.method == 'GET':
        return render(request, 'newreq.html')


def submitreq(request):
    if request.method == 'GET':
        return redirect('/newreq')
    elif request.method == 'POST':
        send_request(request.POST)
        return redirect('/result?package=' + request.POST['app'])
