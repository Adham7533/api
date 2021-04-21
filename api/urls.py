from django.urls import path
from .views import TaxisAPIView,AccountAPIView

urlpatterns = [
    path('', TaxisAPIView.as_view()),
    path('',AccountAPIView.as_view()),

]