from django.views.generic import ListView
from .models import Product, CategoryProduct
from cart.forms import CartAddProductForm
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages


def index(request):
    category = None
    categories = CategoryProduct.objects.all()
    products = Product.objects.order_by('-views').filter(available=True)[:12]

    return render(request,
                  'index.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


class Productlist(ListView):
    template_name = 'product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.filter(available=True)


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    product.views += 1
    product.save(update_fields=['views'])
    return render(request, 'product_detail.html', {'product': product, 'cart_product_form': cart_product_form})


def about(request):
    return render(request, 'about.html', )


def contacts(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = '{} ({})'.format(cd['subject'], cd['email'])
            mail = send_mail(subject, form.cleaned_data['content'],
                             'Golubev.V56@yandex.ru', ['mr.gazik@mail.ru'],
                             fail_silently=True)
            if mail:
                messages.success(request, 'Сообщение успешно отправлено.')
                return redirect('contacts')
            else:
                messages.error(request, 'Ошибка отправки, попробуйте снова.')
        else:
            messages.error(request, 'Ошибка!')
    else:
        form = ContactForm()
    return render(request, 'contacts.html', {'form': form})
