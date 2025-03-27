from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    # Remove or comment out the Django auth URLs since we're using our own logout view
    # path('accounts/', include('django.contrib.auth.urls')),
]
