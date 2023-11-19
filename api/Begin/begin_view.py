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
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, password=password1)

                # Leer el contenido del archivo HTML
                with open('api/templates/send_mail.html', 'r') as file:
                    html_content = file.read()

                # Reemplazar las variables en el archivo HTML con datos del usuario
                html_content = html_content.format(username=username, password=password1)

                # Envío de correo electrónico al usuario registrado con formato HTML
                send_mail(
                    'Not reply, successfuly register',
                    '',  # Deja el cuerpo del mensaje en blanco, ya que lo proporcionamos en HTML
                    'processautomedccai@gmail.com',
                    [email],
                    html_message=html_content,  # Especifica el mensaje HTML
                    fail_silently=False,
                )

                user = authenticate(request, username=username, password=password1)
                login(request, user)

                return redirect('success_register')
            else:
                return render(request, self.template_name, {'error': 'El usuario ya existe.'})
        else:
            return render(request, self.template_name, {'error': 'Las contraseñas no coinciden.'})

class Success_register(APIView):
    template_name='success_register.html'
    def get(self,request):
        return render(request,self.template_name)
    
