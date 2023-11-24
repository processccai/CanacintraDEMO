from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from api.models import Perfil
import json
# Create your views here.
@method_decorator(login_required(login_url='login'), name='dispatch')  
class Home(APIView):
    template_name='home.html'
    def get(self, request):
        # Obtener el usuario actualmente autenticado
        usuario_actual = request.user

        # Obtener los últimos 5 perfiles ordenados por ID
        perfiles = Perfil.objects.all().order_by('-idPerfil')[:5]

        # Procesar los datos antes de pasarlos a la plantilla
        perfiles_converted = []
        for perfil in perfiles:
            try:
                tipos_lenguajes = json.loads(perfil.tipos_lenguajes) if perfil.tipos_lenguajes else []
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON for perfil {perfil.idPerfil}: {e}")
                tipos_lenguajes = []

            try:
                areas_especialidad = json.loads(perfil.areas_especialidad) if perfil.areas_especialidad else []
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON for perfil {perfil.idPerfil}: {e}")
                areas_especialidad = []

            perfiles_converted.append({
                'idPerfil': perfil.idPerfil,
                'edad': perfil.edad,
                'genero': perfil.genero,
                'fecha_realizacion': perfil.fecha_realizacion,
                'tipos_lenguajes': tipos_lenguajes,
                'años_programacion': perfil.años_programacion,
                'areas_especialidad': areas_especialidad,
                'marco_trabajo': perfil.marco_trabajo,
                'frame_works': perfil.frame_works,
                'sistemas_operativos': perfil.sistemas_operativos,
                'online_community': perfil.online_community,
                'challenge_devs': perfil.challenge_devs,
                'herramientas_comunicacion': perfil.herramientas_comunicacion,
                'herramientas_desarrollo': perfil.herramientas_desarrollo,
                'user': perfil.usuario
            })

        # Pasar los datos procesados al contexto
        context = {
            'Perfiles': perfiles_converted,
            'username': usuario_actual.username if usuario_actual else None,
            'id_user': usuario_actual.id if usuario_actual else None,
        }
        return render(request, self.template_name, context)