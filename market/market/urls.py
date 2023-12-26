from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Neobis-Eco-Market",
        default_version='v1',
        description="Eco Market REST API",
    ),
    public=True,
)

swagger_info = schema_view.with_ui('swagger', cache_timeout=0)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', swagger_info, name='swagger'),
    path("", include("products.urls")),
    path("", include("orders.urls")),
]
