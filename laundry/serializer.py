from rest_framework import serializers
from .models import User
from .models import Laundry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','password','phone_number','email','type']

class LaundrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laundry
        fields = ['id','name','location','image','phone_number']
