from django.shortcuts import render, redirect
from .models import ServiceCategory, Order
from .forms import ServiceCategoryForm
def index(request):
    categories = ServiceCategory.objects.all()
    return render(request, 'main/index.html', {'categories': categories})

def order(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        phone = request.POST['phone']
        service_id = request.POST['service']
        time = request.POST['time']
        address = request.POST['address']

        try:
            service = ServiceCategory.objects.get(pk=service_id)
        except ServiceCategory.DoesNotExist:
            return render(request, 'main/index.html', {'error': 'Выбранная услуга недействительна. Пожалуйста, выберите услугу из каталога.'})

        order = Order(name=name, surname=surname, phone=phone, service=service, time=time, address=address)
        order.save()

        return render(request, 'main/order_success.html')
    else:
        categories = ServiceCategory.objects.all()
        return render(request, 'main/index.html', {'categories': categories})


def add_category(request):
    if request.method == 'POST':
        form = ServiceCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    else:
        form = ServiceCategoryForm()

    return render(request, 'main/add_category.html', {'form': form})

