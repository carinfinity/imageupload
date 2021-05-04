from django.urls import path
from blogs import views 


urlpatterns = [
    
    path('newcar/', views.newCar),
    path('upcomingcar/', views.upcomingCar)
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
