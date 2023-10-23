from django.urls import path
from . import views

urlpatterns = [
    path('', views.button_view1 ,name = 'button_view1' ),
    path('', views.button_view2 ,name = 'button_view2' ),
    path('', views.slider_view1 ,name = 'slider_view1' ),
    path('', views.slider_view2 ,name = 'slider_view2' ),
    path('', views.get_humidity_data ,name = 'get_humidity_data' ),
]
