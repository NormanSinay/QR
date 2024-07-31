from django.contrib import admin
from django.urls import path
from qrs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate/', views.generate_qr, name='generate_qr'),
]
