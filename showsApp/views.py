from django.shortcuts import render
from showsApp.models import Show, Platform
from showsApp.serializers import PlatformSerializer
from showsApp.serializers import ShowSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class ShowListGV(generics.ListCreateAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class ShowDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer


class PlatformListAV(APIView):
    def get(self, request):
        platforms = Platform.objects.all()
        serializer = PlatformSerializer(platforms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class PlatformDetailAV(APIView):
    def get(self, request, pk):
        try:
            platform = Platform.objects.get(pk=pk)
            serializer = PlatformSerializer(platform)
            return Response(serializer.data)
        except Platform.DoesNotExist:
            return Response(status=404)

    def put(self, request, pk):
        try:
            platform = Platform.objects.get(pk=pk)
            serializer = PlatformSerializer(platform, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Platform.DoesNotExist:
            return Response(status=404)

    def delete(self, request, pk):
        try:
            platform = Platform.objects.get(pk=pk)
            platform.delete()
            return Response(status=204)
        except Platform.DoesNotExist:
            return Response(status=404)