from rest_framework import serializers

from vaccines.models import User, Vaccine

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]

class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        exclude = []