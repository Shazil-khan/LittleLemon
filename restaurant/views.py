from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from restaurant.serializers import bookingSerializer, menuSerializer
from restaurant.models import Booking, Menu
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework import viewsets

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class bookingView(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data)
    
    
class menuView(APIView):
    def post(self, request):
        serializer = menuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class BookingViewset(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer