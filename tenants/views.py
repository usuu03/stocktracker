from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_201_CREATED
from rest_framework.exceptions import NotFound

from tenants.models import Tenant
from tenants.serializers import TenantSerializer
from tenants.swagger_docs import tenant_list_operation, tenant_detail_operation, tenant_create_operation

class TenantView(APIView):
    # Use the Swagger documentation for the "List all tenants" operation
    @swagger_auto_schema(**tenant_list_operation)
    def get(self, request, *args, **kwargs):
        """Fetch all tenants"""
        queryset = Tenant.objects.all()
        serializer = TenantSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    @swagger_auto_schema(**tenant_create_operation)
    def post(self, request, *args, **kwargs):
        "Create a new tenant"
        serializer = TenantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    

class TenantDetailView(APIView):
    # Use the Swagger documentation for the "Retrieve a specific tenant" operation
    @swagger_auto_schema(**tenant_detail_operation)
    def get(self, request, pk, *args, **kwargs):
        """Fetch a single  asset by its ID."""
        try:
            tenant = Tenant.objects.get(pk=pk)
        except Tenant.DoesNotExist:
            raise NotFound({"error": f"Software with ID {pk} not found."})
        serializer = TenantSerializer(tenant)
        return Response(serializer.data, status=HTTP_200_OK)

