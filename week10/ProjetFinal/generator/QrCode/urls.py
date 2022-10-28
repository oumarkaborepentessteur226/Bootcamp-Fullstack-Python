from django.urls import path
from QrCode import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.demo, name='demo'),

] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)