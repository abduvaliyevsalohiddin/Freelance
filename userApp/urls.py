from django.urls import path

from .views import *

urlpatterns = [
    path('profil/<int:pk>/', ProfileRetrieveUpdateDestroyView.as_view()),
    path('profile/', ProfileAPIView.as_view()),

]
