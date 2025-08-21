from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    # Wishlist
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),

    # 🔽 Add this line (so your category links work)
    path('category/<str:category_name>/', views.category_products, name='category_products'),

    # Product / cart / order
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('buy-now/<int:pk>/', views.buy_now, name='buy_now'),
    path('cart/', views.add_to_cart_view, name='add_to_cart_view'),
    path('checkout/', views.checkout_page, name='checkout_page'),
    path('order-success/', views.order_success, name='order_success'),
]
