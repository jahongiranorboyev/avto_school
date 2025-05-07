from django.contrib import admin
from django.urls import path, include, re_path
from .swagger import schema_view


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    path('admin/', admin.site.urls),
    path('api/v1/quizzes/', include('apps.quizzes.urls')),
    path('api/v1/payment/', include('apps.payments.urls')),
    path('api/v1/auth/', include('apps.authentications.urls')),
    path('api/v1/user-list/', include('apps.users.urls')),
    path('api/v1/general/', include('apps.general.urls')),
    path('ap1/v1/roadsigns/',include('apps.roadsigns.urls')),
    path('api/v1/lessons/', include('apps.lessons.urls')),
    path('api/v1/notifications/', include('apps.notifications.urls')),
    path('api/v1/phrases/', include('apps.phrases.urls'))
    ]