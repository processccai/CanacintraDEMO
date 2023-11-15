from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.

class Login(APIView):
    template_name='authentication-login.html'
    def get(self,request):
        return render(request,self.template_name)
class Register(APIView):
    template_name='authentication-register.html'
    def get(self,request):
        return render(request,self.template_name)