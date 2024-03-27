from django.contrib.auth.models import User 
from rest_framework import serializers 
from api.models import Menu,BookingTable
class UserSerializer(serializers.ModelSerializer): 

    class Meta: 
        model = User 
        fields = ['url', 'username', 'email', 'groups']

class MenuSerailizer(serializers.ModelSerializer):
    model = Menu
    fields = '__all__'

class BookingTableSerializer(serializers.ModelSerializer):
    model = BookingTable
    fields = '__all__'