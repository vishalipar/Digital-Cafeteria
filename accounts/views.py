from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Product, Supplier

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
    
def logout_view(request):
    logout(request)
    return redirect('login')