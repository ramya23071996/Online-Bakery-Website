from django.shortcuts import render, get_object_or_404,redirect
from .models import Category,Product, Wishlist
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def category_products(request, category_name):
    category = get_object_or_404(Category, name__iexact=category_name)
    products = category.products.all()
    return render(request, f"catalog/{category_name.lower()}.html", {
        "category": category,
        "products": products
    })


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    if created:
        messages.success(request, f"{product.name} added to your wishlist.")
    else:
        messages.info(request, f"{product.name} is already in your wishlist.")
    return redirect(request.META.get("HTTP_REFERER", "catalog:wishlist"))  

@login_required  
def remove_from_wishlist(request, product_id):
    wishlist_item = get_object_or_404(Wishlist, product__id=product_id, user=request.user)
    product_name = wishlist_item.product.name  # Store name before deletion
    wishlist_item.delete()
    messages.success(request, f"{product_name} removed from your wishlist.")  # Added feedback
    return redirect('catalog:wishlist')  # Fixed: added namespace

@login_required
def wishlist(request):
    items = Wishlist.objects.filter(user=request.user).select_related("product")
    return render(request, "catalog/wishlist.html", {"items": items})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    quantities = range(1, 11)  # 1–10
    return render(request, 'catalog/product_detail.html', {'product': product, 'quantities': quantities})

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', {})
    cart[str(product.id)] = cart.get(str(product.id), 0) + 1
    request.session['cart'] = cart
    return redirect('add_to_cart_view')

def buy_now(request, pk):
    product = get_object_or_404(Product, pk=pk)
    request.session['cart'] = {str(product.id): 1}
    return redirect('checkout_page')


def add_to_cart_view(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_items = []
    total = 0

    for product in products:
        qty = cart.get(str(product.id))
        subtotal = product.price * qty
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': qty,
            'subtotal': subtotal,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'catalog/add_to_cart.html', context)


def checkout_page(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    total = sum([product.price * cart[str(product.id)] for product in products])

    if request.method == 'POST':
        request.session['cart'] = {}
        return redirect('order_success')

    return render(request, 'checkout.html', {'total': total})


def order_success(request):
    return render(request, 'order_success.html')