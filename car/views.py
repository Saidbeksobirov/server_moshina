import json

from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render

from car.models import CarModel


def car_list_view(request):
    cars = CarModel.objects.all()
    context = {'cars': cars}
    return render(request, 'car.html', context)


def car_detail_view(request, pk):
    car = CarModel.objects.get(id=pk)
    if car:
        context = {'car': car}
        return render('car_detail.html', context)
    else:
        return HttpResponseNotFound('Car not found')


def login_page(request):
    return render(request, 'login.html')


def car_1_page(request):
    cars = CarModel.objects.all()
    context = {'cars': cars}
    return render(request, 'car1.html', context)


def car_2_page(request):
    cars = CarModel.objects.all()
    context = {'cars': cars}
    return render(request, 'car2.html', context)


def image_upload_view(request, pk):
    car = CarModel.objects.filter(id=pk).first()
    with open("media/ecard",  "r") as file:
        image_data = json.load(file)
        context = {'image_data': image_data}
        if car:
            return render(request, "car.html", context)


def car_list_view_1(request):
    cars = CarModel.objects.all()
    context = {'cars': cars}
    return render(request, 'car.html', context)