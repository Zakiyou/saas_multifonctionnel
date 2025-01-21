from django.shortcuts import render
from django.http import JsonResponse
from rembg import remove 
from PIL import Image
import os
from django.conf import settings
from django.http import FileResponse

def ViewRemoveBg(request):
    return render(request, 'pages/remove_bg.html')

def remove_bg(request):
    if request.method == 'POST':
        file = request.FILES.get('image')

        if file:
            try:
                if not file.content_type.startswith('image/'):
                    raise ValueError("Le fichier envoyé n'est pas une image valide.")

                # Supprimer l'arrière-plan
                output_image = remove(file.read())
                unique_filename = f"removed_bg_{os.path.splitext(file.name)[0]}_{int(os.urandom(4).hex(), 16)}.png"
                output_path = os.path.join(settings.MEDIA_ROOT, unique_filename)

                with open(output_path, 'wb') as out_file:
                    out_file.write(output_image)

                media_url = f"{settings.MEDIA_URL}{unique_filename}"
                return JsonResponse({'file_path': media_url, 'file_name': unique_filename, 'content_type': 'image/png'})

            except Exception as e:
                return JsonResponse({'error': 'Erreur lors du traitement de l’image.', 'exception': str(e)})

    return JsonResponse({'error': 'Requête invalide.'}, status=400)



def media_file(request, file_name):
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    return FileResponse(open(file_path, 'rb'), content_type='image/png')
