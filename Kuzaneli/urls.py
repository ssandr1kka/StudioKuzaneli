from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("contact", views.contact, name="contact"),
    path("gallery-walls", views.gallerywalls, name="walls"),
    path("gallery-walls/<str:picture_title>", views.gwpicture, name="picture"),
    path("cart", views.cart, name="cart"),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_clear_2/<int:id>/', views.item_clear_2, name='item_clear_2'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
