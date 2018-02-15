from django.urls import path
from unus import views
from unus.views import RestApiView

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('api', RestApiView.as_view())
]