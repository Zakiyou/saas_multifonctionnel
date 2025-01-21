from django.shortcuts import render
from django.http import JsonResponse
import PyPDF2
from django.http import FileResponse
import os
from django.conf import settings
def Viewpdf_encrypt(request):
    return render(request, 'pages/pdf_encrypt.html')


def encrypt_pdf(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        password = request.POST.get('password')

        if file and password:
            input_pdf = PyPDF2.PdfReader(file)
            output_pdf = PyPDF2.PdfWriter()

            # Ajouter les pages sans mot de passe
            for page_num in range(len(input_pdf.pages)):
                page = input_pdf.pages[page_num]
                output_pdf.add_page(page)

            # Chiffrement du PDF avec le mot de passe
            output_pdf.encrypt(password)

            # Enregistrement du fichier chiffré
            encrypted_file_path = f"media/encrypted_{file.name}"  
            with open(encrypted_file_path, 'wb') as output_file:
                output_pdf.write(output_file)

            # Retourner le chemin du fichier chiffré en JSON pour le JS
            return JsonResponse({'file_path': encrypted_file_path})

    return render(request, 'composant/pdf_encrypt.html')



def media_file(request, file_name):
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    content_type = 'application/octet-stream'  # Type par défaut
    
    # Définir les types MIME selon les extensions de fichier
    if file_name.endswith('.png') or file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
        content_type = 'image/png'  # ou 'image/jpeg'
    elif file_name.endswith('.pdf'):
        content_type = 'application/pdf'
    elif file_name.endswith('.mp4') or file_name.endswith('.avi'):
        content_type = 'video/mp4'  # ou 'video/avi'
    elif file_name.endswith('.mp3'):
        content_type = 'audio/mpeg'
    # Ajouter d'autres types selon les besoins

    return FileResponse(open(file_path, 'rb'), content_type=content_type)

