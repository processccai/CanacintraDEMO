from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.views import APIView
from api.models import Perfil,Validar
import json

class AddProfiel(APIView):
    template_name="success_form.html"
    def post(self, request):
        # Recopila los datos del formulario
        age = request.POST['age']
        gender = request.POST['gender']
        opersys = request.POST['opersys']
        experienceage = request.POST['experienceage']
        specialdev = json.dumps(request.POST.getlist('specialdev'))
        frame_dev = json.dumps(request.POST.getlist('frame_dev'))
        program_dev = json.dumps(request.POST.getlist('program_dev'))
        open_dev = json.dumps(request.POST.getlist('open_dev'))
        challenge_dev = json.dumps(request.POST.getlist('challenge_dev'))
        community = request.POST['community']
        tools_dev = json.dumps(request.POST.getlist('tools_dev'))
        com_dev = json.dumps(request.POST.getlist('com_dev'))
        id_user = int(request.POST['id_user'])
        url = request.POST['url']
        # Obtener la instancia del usuario a partir del ID
        usuario = User.objects.get(id=id_user)

        # Crear una instancia del modelo con los datos del formulario y asignar la instancia del usuario
        perfil_instance = Perfil(
            edad=age,
            genero=gender,
            sistemas_operativos=opersys,
            años_programacion=experienceage,
            areas_especialidad=specialdev,
            frame_works=frame_dev,
            tipos_lenguajes=program_dev,
            marco_trabajo=open_dev,
            challenge_devs=challenge_dev,
            online_community=community,
            herramientas_comunicacion=com_dev,
            herramientas_desarrollo=tools_dev,
            usuario=usuario,  # Asignar la instancia del usuario, no el ID
            curriculum_link=url,
        )

        # Guardar la instancia en la base de datos
        perfil_instance.save()
        
        # Obtener o crear la instancia de Validar asociada al usuario
        validar_instance, created = Validar.objects.get_or_create(usuario=usuario)

        # Establecer validacion en True y guardar la instancia de Validar
        validar_instance.validacion = True
        validar_instance.save()
        
        
        # Puedes redirigir a otra vista o renderizar una plantilla de éxito
        return render(request, self.template_name)