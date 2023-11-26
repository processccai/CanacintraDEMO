from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from api.models import Perfil,Validar
from collections import Counter
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

        # Contador para almacenar la frecuencia de cada lenguaje
        language_counter = Counter()

        # Procesar los datos antes de pasarlos a la plantilla
        perfiles_converted = []
        for perfil in perfiles:
            try:
                tipos_lenguajes = json.loads(perfil.tipos_lenguajes) if perfil.tipos_lenguajes else []
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON for perfil {perfil.idPerfil}: {e}")
                tipos_lenguajes = []

            # Incrementar la frecuencia de cada lenguaje
            language_counter.update(tipos_lenguajes)

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
                'user': perfil.usuario,
                'url' : perfil.curriculum_link,
            })
        total_perfiles = Perfil.objects.count()
        # Obtener la instancia de Validar para el usuario actual
        validar_instancia = get_object_or_404(Validar, usuario=usuario_actual)

        # Obtener el valor de validacion
        valor_validacion = validar_instancia.validacion

        # Obtener los 3 lenguajes más seleccionados
        top_languages = language_counter.most_common(3)

        # Pasar los datos procesados al contexto
        context = {
            'Perfiles': perfiles_converted,
            'username': usuario_actual.username if usuario_actual else None,
            'id_user': usuario_actual.id if usuario_actual else None,
            'valor_validacion': valor_validacion,
            'top_languages': top_languages,
            'total_perfiles': total_perfiles,
        }

        return render(request, self.template_name, context)