from django.urls import path

from .views import *

urlpatterns = [
    path('category/', CategoryListCreateView.as_view()),

    path('projects/', ProjectAPIView.as_view()),
    path('project/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view()),

    path('connect/', ConnectionListCreateView.as_view()),

    path('comment/', CommentListCreateAPIView.as_view()),
    path('comment/<int:pk>/', CommentRetrieveDestroyView.as_view()),

    path('like/', LikeListCreateAPIView.as_view()),
    path('like/<int:pk>/', LikeDestroyView.as_view()),

]
