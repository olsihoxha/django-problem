from django.urls import path
from .views import TeslaModelListCreateAPIView, CountryNameListCreateAPIView

urlpatterns = [
    path('models/', TeslaModelListCreateAPIView.as_view()),
    path('countries/', CountryNameListCreateAPIView.as_view()),
]
