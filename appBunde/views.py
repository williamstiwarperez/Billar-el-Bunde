from rest_framework import viewsets
from .serializer import appBundeSeializer
from .models import appBunde

# Create your views here.
class appBundeView(viewsets.ModelViewSet):
    serializer_class = appBundeSeializer
    queryset = appBunde.objects.all()
    