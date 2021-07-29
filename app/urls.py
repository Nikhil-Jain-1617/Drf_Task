from django.urls import path
from app.views import CategoryApi,ProductApi

urlpatterns = [
    path('category/', CategoryApi.as_view() ),
    path('product/', ProductApi.as_view() ),
]