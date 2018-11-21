from perris.models import Perros_Rescatados
from rest_framework import viewsets
#Importamos el archivo serializers.py
from perris.quickstart.serializers import RescatadoSerializer




class RescatadoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Perros_Rescatados.objects.all()
    serializer_class = RescatadoSerializer
