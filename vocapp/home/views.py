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


def register_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "vocapp/gateway/register.html", {})


def register_ok_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "vocapp/gateway/register_success.html", {})


def login_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "vocapp/gateway/login.html", {})



def logout_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "vocapp/gateway/logout.html", {})








#---dashboard---

def dashboard_page(request):
    return render(request, "vocapp/dashboard/dashboard.html", {
        'user': request.user,
    })



def voc_add(request):
    return render(request, "vocapp/dashboard/voc_add.html", {})
