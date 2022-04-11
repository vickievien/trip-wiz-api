from rest_framework import serializers 
from .models import Review 

class ReviewSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Review
        fields = ('id', 'reviewer_name', 'city', 'country', 'review', 'img', 'trip_start_date', 'trip_end_date',)