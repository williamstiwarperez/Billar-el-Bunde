from rest_framework import serializers
from .models import appBunde
class appBundeSeializer(serializers.ModelSerializer):
    class Meta:
        model = appBunde
        fields = '__all__'
        