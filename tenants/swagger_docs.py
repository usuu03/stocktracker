from drf_yasg import openapi
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from tenants.models import Tenant
from tenants.serializers import TenantSerializer

# Example of a single tenant response
tenant_example = {
    "name": "GreenTech Solutions",
    "subdomain": "greentech"
}

# Response schema for listing all tenants
tenant_list_response = openapi.Response(
    description="A list of tenants in the system",
    examples={
        "application/json": [
            tenant_example,
            {
                "name": "Urban Outfitters",
                "subdomain": "urbanoutfitters"
            },
            {
                "name": "TechNova Inc.",
                "subdomain": "technova"
            }
        ]
    }
)

# Define operation for GET request to list tenants
tenant_list_operation = {
    "operation_id": "List all tenants",
    "operation_description": "Retrieve a list of all tenants in the system.",
    "responses": {
        HTTP_200_OK: tenant_list_response
    },
}

# Define operation for GET request to retrieve a specific tenant by ID
tenant_detail_response = openapi.Response(
    description="A single tenant in the system",
    examples={
        "application/json": tenant_example
    }
)

tenant_detail_operation = {
    "operation_id": "Retrieve a specific tenant",
    "operation_description": "Retrieve details of a specific tenant by ID.",
    "responses": {
        HTTP_200_OK: tenant_detail_response,
        HTTP_404_NOT_FOUND: openapi.Response(description="No Tenant with that ID found")
    },
}

# Define operation for POST request to create a tenant
tenant_create_response = openapi.Response(
    description="Tenant successfully created.",
    examples={
        "application/json": {
            "name": "GreenTech Solutions",
            "subdomain": "greentech"
        }
    }
)

tenant_create_operation = {
    "operation_id": "Create a new tenant",
    "operation_description": "Create a new tenant in the system.",
    "request_body": TenantSerializer,
    "responses": {
        HTTP_201_CREATED: tenant_create_response,
        HTTP_400_BAD_REQUEST: openapi.Response(description="Invalid input data")
    },
}