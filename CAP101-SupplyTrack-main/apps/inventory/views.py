from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@login_required
def admin_dashboard(request):
    return render(request, "inventory/admin/admin_dashboard.html")

@login_required
def manager_dashboard(request):
    return render(request, "inventory/manager/manager_dashboard.html")

@login_required
def staff_dashboard(request):
    return render(request, "inventory/staff/staff_dashboard.html")


@login_required
def inventory_list(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:inventory_list')  # Redirect back to the inventory list
    else:
        form = ProductForm()

    context = {
        'products': products,
        'form': form
    }
    return render(request, 'inventory/inventory_list/inventory_list.html', context)
    
@csrf_exempt
def delete_products(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ids = data.get('ids', [])
        
        if ids:
            Product.objects.filter(id__in=ids).delete()
            return JsonResponse({'status': 'success'})
        
        return JsonResponse({'status': 'no ids provided'}, status=400)
    
    return JsonResponse({'status': 'invalid method'}, status=405)