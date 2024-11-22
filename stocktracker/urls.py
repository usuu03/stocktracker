from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.contrib import admin

schema_view = get_schema_view(
    openapi.Info(
        title="Multi-Tenant Inventory Management API",
        default_version="v1",
        description=(
            "This API provides endpoints for managing inventory in a multi-tenant SaaS "
            "platform. Features include product management, stock tracking, analytics, "
            "and role-based access control. Each tenant (organization) operates in a "
            "data-isolated environment while sharing the same application infrastructure."
        ),
        contact=openapi.Contact(email="support@inventoryapp.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/tenants/', include('tenants.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('auth/', include('accounts.urls'))
]
