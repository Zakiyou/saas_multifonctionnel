from django.shortcuts import render

def acceuil(request):
    return render(request, 'pages/acceuil.html')