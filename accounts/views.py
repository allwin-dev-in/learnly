from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework import authentication,permissions
from rest_framework.response import Response

# from rest_framework_simplejwt.authentication

from accounts.serializers import UserSerializer
from accounts.models import User

# Create your views here.

class SignupView(APIView):
    def post(self,request):
        form_data=request.data
        user_role=form_data.get("role")
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            if user_role=="Student" or user_role=="Trainer":
                qs=User.objects.create_user(**cleaned_data)
            elif user_role=="Admin":
                qs=User.objects.create_superuser(**cleaned_data) 
            ser_inst=UserSerializer(qs)
            return Response(ser_inst.data)
        else:
            return Response(serializer_instance.errors)
        

class UserRetriveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]

    serializer_class=UserSerializer
    queryset=User.objects.all()