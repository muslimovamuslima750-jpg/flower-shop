from .forms import OrderForm
from django.shortcuts import render

def index(request):
    # Берём 4 товара для блока "Популярное"
    popular = FLOWERS[:4]
    return render(request, 'shop/index.html', {'popular': popular})

from .data import FLOWERS, CATEGORIES

def catalog(request):
    query = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()
    price_from = request.GET.get('price_from', '').strip()
    price_to = request.GET.get('price_to', '').strip()

    flowers = FLOWERS

    # Поиск по названию
    if query:
        flowers = [f for f in flowers if query.lower() in f['name'].lower()]

    # Фильтр по категории
    if category:
        flowers = [f for f in flowers if f['category'] == category]

    # Фильтр по цене
    if price_from.isdigit():
        flowers = [f for f in flowers if f['price'] >= int(price_from)]
    if price_to.isdigit():
        flowers = [f for f in flowers if f['price'] <= int(price_to)]

    return render(request, 'shop/catalog.html', {
        'flowers': flowers,
        'categories': CATEGORIES,
        'query': query,
        'selected_category': category,
        'price_from': price_from,
        'price_to': price_to,
    })

def cart(request):
    cart_data = request.session.get('cart', {})
    items = []
    total = 0

    for flower_id, quantity in cart_data.items():
        flower = next((f for f in FLOWERS if f['id'] == int(flower_id)), None)
        if flower:
            summa = flower['price'] * quantity
            total += summa
            items.append({
                'flower': flower,
                'quantity': quantity,
                'summa': summa,
            })

    return render(request, 'shop/cart.html', {
        'items': items,
        'total': total,
    })

def checkout(request):
    cart_data = request.session.get('cart', {})
    items = []
    total = 0

    for flower_id, quantity in cart_data.items():
        flower = next((f for f in FLOWERS if f['id'] == int(flower_id)), None)
        if flower:
            summa = flower['price'] * quantity
            total += summa
            items.append({'flower': flower, 'quantity': quantity, 'summa': summa})

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Очищаем корзину после "оформления"
            request.session['cart'] = {}
            return render(request, 'shop/order_success.html', {
                'name': form.cleaned_data['name'],
                'total': total,
            })
    else:
        form = OrderForm()

    return render(request, 'shop/checkout.html', {
        'form': form,
        'items': items,
        'total': total,
    })

def about(request):
    return render(request, 'shop/about.html')

def contacts(request):
    return render(request, 'shop/contacts.html')

def product(request, product_id):
    flower = next((f for f in FLOWERS if f["id"] == product_id), None)
    return render(request, 'shop/product.html', {'flower': flower})

from django.shortcuts import redirect

def add_to_cart(request, product_id):
    cart_data = request.session.get('cart', {})
    product_id_str = str(product_id)
    cart_data[product_id_str] = cart_data.get(product_id_str, 0) + 1
    request.session['cart'] = cart_data
    return redirect('cart')

def increase_quantity(request, product_id):
    cart_data = request.session.get('cart', {})
    pid = str(product_id)
    cart_data[pid] = cart_data.get(pid, 0) + 1
    request.session['cart'] = cart_data
    return redirect('cart')


def decrease_quantity(request, product_id):
    cart_data = request.session.get('cart', {})
    pid = str(product_id)
    if pid in cart_data:
        cart_data[pid] -= 1
        if cart_data[pid] <= 0:
            del cart_data[pid]
    request.session['cart'] = cart_data
    return redirect('cart')


def remove_from_cart(request, product_id):
    cart_data = request.session.get('cart', {})
    pid = str(product_id)
    if pid in cart_data:
        del cart_data[pid]
    request.session['cart'] = cart_data
    return redirect('cart')

def privacy(request):
    return render(request, 'shop/privacy.html')