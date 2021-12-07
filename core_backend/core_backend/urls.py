from django.urls import path, include
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('api/', include('robots.urls')),
    path('api/', include('users.urls')),
    path('api/', include('products.urls')),
    path('api/', include('zones.urls')),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
         "api/docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    )
]
