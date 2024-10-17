from django.urls import path, include
from .views import home


urlpatterns = [
    path('', home, name='A_TEA'),
    path('admin/', admin.site.urls),
    path('compromissos/', include('compromissos.urls')),
]
