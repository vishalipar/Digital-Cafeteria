from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Product, Supplier
from .forms import ProductForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
    
@login_required
def dashboard(request):
    total_products = Product.objects.count()
    total_suppliers = Supplier.objects.count()
    low_stock = Product.objects.filter(quantity__lt=5).count()
    recent_products = Product.objects.order_by('-created_at')[:5]

    context = {
        'total_products': total_products,
        'total_suppliers': total_suppliers,
        'low_stock': low_stock,
        'recent_products': recent_products
    }
    return render(request, 'dashboard.html', context)
    
@login_required
def product_list(request):
    products = Product.objects.all()
    suppliers = Supplier.objects.all()
    return render(request, 'products/list.html', {
        'products': products,
        'suppliers': suppliers
        })
    
@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('product_list')

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/form.html', {'form': form})
    
def logout_view(request):
    logout(request)
    return redirect('login')