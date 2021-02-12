from django.contrib import admin
from django.urls import path
import tesla_data.urls as tesla_url

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += tesla_url.urlpatterns
