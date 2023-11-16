from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
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
    template_name = 'authentication-register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            # Verificar si el usuario ya existe
            if not User.objects.filter(username=username).exists():
                # Crear el usuario
                user = User.objects.create_user(username=username, email=email, password=password1)

                # Envío de correo electrónico al usuario registrado
                send_mail(
                    'Registro Exitoso',
                    f'Gracias por registrarte en nuestro sitio.\n\nTu nombre de usuario es: {username}\nTu correo electrónico es: {email}',
                    'processautomedccai@gmail.com',
                    [email],
                    fail_silently=False,
                )

                # Autenticar al usuario
                user = authenticate(request, username=username, password=password1)
                login(request, user)

                return redirect('success_register')  # Redirigir a la página de inicio de sesión
            else:
                # El usuario ya existe
                return render(request, self.template_name, {'error': 'El usuario ya existe.'})
        else:
            # Las contraseñas no coinciden
            return render(request, self.template_name, {'error': 'Las contraseñas no coinciden.'})

class Success_register(APIView):
    template_name='success_register.html'
    def get(self,request):
        return render(request,self.template_name)