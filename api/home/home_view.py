from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(login_required(login_url='login'), name='dispatch')  
class Home(APIView):
    template_name='home.html'
    def get(self,request):
        return render(request,self.template_name)