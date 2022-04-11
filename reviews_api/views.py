from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ReviewSerializer
from .models import Review

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = ReviewSerializer # tell django what serializer to use

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all().order_by('id')
    serializer_class = ReviewSerializer