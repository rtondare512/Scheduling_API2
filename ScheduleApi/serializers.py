from rest_framework import serializers

from .models import DT

class DTSerializer(serializers.ModelSerializer):
  class Meta():
    model = DT
    fields ='__all__'


