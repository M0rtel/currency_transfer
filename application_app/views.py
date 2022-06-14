from django.shortcuts import render


def main(request):
    return render(request, 'application_app/main.html')
