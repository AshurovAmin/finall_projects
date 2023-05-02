from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

schema_view = get_schema_view(
   openapi.Info(
      title="Online Volonteer API",
      default_version='v0.0.1',
      description="API Doc Online Volonteer Kg",
      contact=openapi.Contact(email="aminashurov22@list.ru"),
      license=openapi.License(name="No License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


doc_urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),

]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('project.urlsv1')),
    path('auth/', include('rest_framework.urls')),

] + doc_urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
