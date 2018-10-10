from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest')),
    path('user/', include(('app_dir.user.urls', 'user'), namespace='user')),
    path('user/api/', include(('app_dir.user.api.urls', 'user_api'), namespace='user_api'))
]
