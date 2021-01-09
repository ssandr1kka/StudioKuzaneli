from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse, resolve
from .models import Picture
from Marketing.models import Signup
from Marketing.forms import EmailSignUpForm
from cart.cart import Cart
import stripe


def emailsubscription(request):
    email = request.POST("email")
    new_signup = Signup()
    new_signup.email = email
    new_signup.save()


def index(request):
    form = EmailSignUpForm()
    if request.method == "POST":
        emailsubscription(request)
    context = {
        "form": form
    }

    return render(request, "kuzaneli/index.html", context)


def contact(request):
    form = EmailSignUpForm()
    if request.method == "POST":
        emailsubscription(request)
    context = {
        "form": form
    }
    return render(request, "kuzaneli/contact.html", context)


def gallerywalls(request):
    form = EmailSignUpForm()
    if request.method == "POST":
        emailsubscription(request)

    queryset = Picture.objects.filter(priority=True)
    result, hlist, vlist = [], [], []
    counter = 0
    if queryset.count() == 0:
        context = {
            'object_list': None,
            "form": form
        }
    else:
        for item in queryset:
            if item.vorh == "V":
                vlist.append(item)
            elif item.vorh == "H":
                hlist.append(item)
        for i in range(len(vlist) + len(hlist)):
            if counter < 4 and vlist:
                result.append(vlist.pop(0))
            elif hlist:
                result.append(hlist.pop(0))
            counter += 1
            if counter == 5:
                counter = 0
        context = {
            'object_list': result,
            "form": form
        }

    return render(request, "kuzaneli/walls.html", context)


def gwpicture(request, picture_title):
    try:
        picture = Picture.objects.get(title=picture_title)
    except Picture.DoesNotExist:
        text = {
            'text': "Picture does not exist."
        }
        return render(request, "kuzaneli/error.html", text)

    incart = False
    cart = request.session.get(settings.CART_SESSION_ID)
    if not cart:
        cart = request.session[settings.CART_SESSION_ID] = {}
    for key, value in cart.items():
        if value["name"] == picture.title:
            incart = True

    form = EmailSignUpForm()
    if request.method == "POST":
        emailsubscription(request)

    context = {
        "picture": picture,
        "form": form,
        "incart": incart
    }
    return render(request, "kuzaneli/picture.html", context)


def cart(request):
    form = EmailSignUpForm()
    if request.method == "POST":
        emailsubscription(request)

    context = {
        "form": form,
    }
    return render(request, "kuzaneli/cart.html", context)


def cart_add(request, id):
    pic = Cart(request)
    product = Picture.objects.get(id=id)
    pic.add(product=product)
    return HttpResponseRedirect(reverse(viewname="picture", args=[product.title]))


def item_clear(request, id):
    pic = Cart(request)
    product = Picture.objects.get(id=id)
    pic.remove(product)
    return HttpResponseRedirect(reverse(viewname='cart'))

def item_clear_2(request, id):
    pic = Cart(request)
    product = Picture.objects.get(id=id)
    pic.remove(product)
    return HttpResponseRedirect(reverse(viewname="picture", args=[product.title]))

def cart_clear(request):
    pics = Cart(request)
    pics.clear()
    return HttpResponseRedirect(reverse(viewname='cart'))

def checkout(request):
    cart = request.session.get(settings.CART_SESSION_ID)
    total = 0
    if not cart:
        return HttpResponseRedirect(reverse(viewname='cart'))
    for key, value in cart.items():
        total += float(value["price"])
    total = int(total) * 100

    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='eur',
        # Verify your integration in this guide by including this parameter
        metadata={'integration_check': 'accept_a_payment'},
    )

    context = {
        "STRIPE_PRIVATE_KEY": stripe.api_key,
        "clientSecret": intent.client_secret,
        "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
        "total": total
    }
    return render(request, "kuzaneli/checkout.html", context)