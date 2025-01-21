
from django.contrib import admin
from django.urls import path
from saas_zakiyou import views  
from pdf_encrypt import views  as pdf_encrypt
from remove_bg import views  as remove_bg


urlpatterns = [
    # path('admin/', admin.site.urls),
     path('', views.acceuil, name='acceuil'),
     path('pdf_encrypt', pdf_encrypt.Viewpdf_encrypt, name='pdf_encrypt'),
     path('encrypt-pdf/',pdf_encrypt.encrypt_pdf, name='encrypt_pdf'),
     path('media/<str:file_name>/', pdf_encrypt.media_file, name='media_file'),  # Serveur pour les médias
     
      path('remove-bg/', remove_bg.remove_bg, name='remove_bg'),
    path('remove-background/', remove_bg.ViewRemoveBg, name='ViewRemoveBg'),


]
