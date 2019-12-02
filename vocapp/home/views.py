from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import status, response, views






# ---- homepage -----


def index_page(request):
    return render(request, 'vocapp/homepage/index.html', {

    })

def contact_page(request):
    return render(request, 'vocapp/homepage/contact.html', {

    })
