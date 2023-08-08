from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import WaterQuality
from .serializers import WaterQualitySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(["GET", "POST"])
def water_sample_list(request):

    if request.method == "GET":

        # get all samples
        samples = WaterQuality.objects.all()
        # serialize them 
        serialized_samples = WaterQualitySerializer(samples, many=True)
        # return them
        return Response(serialized_samples.data)
    
    if request.method == "POST":
        serialized_samples = WaterQualitySerializer(data=request.data)
        if serialized_samples.is_valid():
            serialized_samples.save()
            return Response (serialized_samples.data, status=status.HTTP_201_CREATED)
@api_view(["GET","PUT","DELETE"])
def water_sample_detail(request, id):
    try:
        water_sample = WaterQuality.objects.get(pk=id)
    except WaterQuality.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serialized_sample = WaterQualitySerializer(water_sample)
        return Response(serialized_sample.data)
    
    elif request.method == "PUT":
        serialized_sample = WaterQualitySerializer(serialized_sample, data=request.data)
        if serialized_sample.is_valid():
            serialized_sample.save()
            return Response(serialized_sample)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        water_sample.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


