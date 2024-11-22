from django.contrib import admin
from django.urls import path, include

from .views import TenantView, TenantDetailView


urlpatterns = [
    path("", TenantView.as_view(), name="all-tenants"),
    path("<str:pk>/", TenantDetailView.as_view(), name="tenant")
   
]
