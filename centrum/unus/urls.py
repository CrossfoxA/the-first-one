from django.urls import path
from unus import views
from unus.views import RestApiListView
from unus.views import RestApiDetailedView


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('api', RestApiListView.as_view()),
    path('api/<int:pk>', RestApiDetailedView.as_view())
]