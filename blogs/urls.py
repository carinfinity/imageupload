from django.urls import path
from blogs import views 


urlpatterns = [
    
    path('newcar/', views.newCar),
    path('upcomingcar/', views.upcomingCar)
]
