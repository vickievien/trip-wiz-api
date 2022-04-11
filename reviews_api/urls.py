from django.urls import path
from . import views

urlpatterns = [
    path('api/reviews/', views.ReviewList.as_view(), name='review_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review_detail'), # api/contacts will be routed to the ContactDetail view for handling
]