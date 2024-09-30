from django.shortcuts import render
from .models import Parameter
import numpy.random as r
import matplotlib.pyplot as plt
from django.http import JsonResponse

from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


def index(request):
    parameters = Parameter.objects.all()
    context = {'parameters': parameters,
               'len': Parameter.objects.count()}
    return render(request, 'main/index.html', context=context)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July'
        ]
        chartlabel = "my data"
        chartdata = [0, 10, 5, 2, 20, 30, 45]
        data = {
            "labels": labels,
            "chartlabel": chartlabel,
            "chartdata": chartdata,
        }
        return Response(data)
