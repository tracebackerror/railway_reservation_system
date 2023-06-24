from django.urls import path
from .views import *

urlpatterns = [
    path('', BookTicket.as_view()),
    path('login/', Login.as_view()),
    path('register/',Register.as_view()),
    path('logout/',Logout.as_view()),
    path('pnr-status/',PNRStatus.as_view()),
    path('fare-calculator/',FareCalculator.as_view()),
]
