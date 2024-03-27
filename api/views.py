from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
# Create your views here.
class HomePage(View):
    def get(self, request, *args, **kwargs):
        # Perform io-blocking view logic using await, sleep for example.
        return render(request,'home.html')

home = HomePage.as_view()

from rest_framework.decorators import api_view
from api.models import Menu,BookingTable
from api.serializers import MenuSerializer,BookingTableSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from django.http import JsonResponse

@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def msg(request):
    pass
    return JsonResponse({'message':'this view protected'})

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView): 
    queryset = Menu.objects.all() 
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):     
    queryset = Menu.objects.all() 
    serializer_class = MenuSerializer

class MenuItemsView(generics.ListCreateAPIView):
   permission_classes = [IsAuthenticated]
   queryset = Menu.objects.all()
   serializer_class = MenuItemSerializer