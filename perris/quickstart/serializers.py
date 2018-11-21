from rest_framework import serializers
from perris.models import Perros_Rescatados

#Creamos nuestra clase 

class RescatadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perros_Rescatados
        fields = ('id' , 'estado','fotografia_perro', 'nombre_perro', 'raza_predominante', 'descripcion' )