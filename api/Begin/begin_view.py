from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
# Create your views here.

class Login(APIView):
    template_name='authentication-login.html'
    def get(self,request):
        return render(request,self.template_name)
    def post(self, request):
        username = request.POST.get('username')  # Obtén el valor del campo de nombre de usuario
        password = request.POST.get('password')  # Obtén el valor del campo de contraseña

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')  # Cambia 'dashboard' por la URL a la que quieres redirigir después del inicio de sesión
            else:
                # El usuario no fue autenticado correctamente
                error_message = 'Invalid credentials'
        else:
            # Los campos de nombre de usuario y contraseña son obligatorios
            error_message = 'Username and password are required'

        # No necesitas instanciar el formulario si no estás utilizándolo para mostrar errores específicos por campo
        # form = TuFormularioExistente(request.POST)
        # form.add_error(None, error_message)  # Esto no es necesario si no estás utilizando el formulario

        return render(request, self.template_name, {'error_message': error_message})

class Logout(APIView):
    def get(self, request):
        # Realiza el logout
        logout(request)
        # Redirige a la página de inicio o a donde desees después del logout
        return redirect('login')  # Ajusta 'home' según la URL a la que deseas redirigir

class Register(APIView):
    template_name='authentication-register.html'
    def get(self,request):
        return render(request,self.template_name)