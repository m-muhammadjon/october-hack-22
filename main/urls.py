from django.urls import path
from main import views

urlpatterns = [
    path('advocates/', views.AdvocateListView.as_view()),
    path('advocates/<str:username>', views.AdvocateDetailView.as_view()),
]