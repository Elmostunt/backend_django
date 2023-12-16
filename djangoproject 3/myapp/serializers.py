from rest_framework import serializers
from .models import ReservarHora

class ReservarHoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservarHora
        fields = ['title', 'description', 'project', 'done']