from django.urls import path

from car.views import car_detail_view, car_list_view, car_1_page, car_2_page, login_page

app_name = 'car'

urlpatterns = [
    path('', login_page, name='list'),
    path('cars/', car_list_view, name='list'),

    path('car_1/', car_1_page, name='car_'),
    path('car_2/', car_2_page, name='car_2')
]