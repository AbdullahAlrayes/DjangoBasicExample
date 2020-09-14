from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from website import views as website_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', website_views.get_list, name="home"),
    path('website/', include('website.urls', namespace='website')),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
