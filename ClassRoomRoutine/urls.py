
from django.contrib import admin
from django.urls import path,include

admin.site.site_header = 'Class Room Routine'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',include('main.urls'))

]
