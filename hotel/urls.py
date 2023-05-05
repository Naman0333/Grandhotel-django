from django.urls import path
from . import views

urlpatterns = [
    path('',views.hotel,name='hotel'),
    path('rooms/', views.rooms, name='rooms'),
    path('booking/<int:room_id>/',views.booking,name='booking'),
    path('contact/',views.contact,name='contact'),
    path('about/', views.about, name='about'),
    path('facilities/', views.facilities, name='facilities'),
    path('dining/',views.dining,name='dining'),
    path('facilities/', views.facilities, name='facilities'),
    path('newsletter/',views.newsletter,name='newsletter'),
    path('validate-booking-date/<str:email>/<str:check_in>/<str:check_out>/',views.validate_booking_date,name='validate_booking_date')
    
]
