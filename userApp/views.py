from django.views.generic import *
from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


class ProfileRegistrationView(CreateAPIView):
    # permission_classes = (AllowAny,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileRetrieveUpdateDestroyView(RetrieveUpdateAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response(ProfileSerializer(user).data)
