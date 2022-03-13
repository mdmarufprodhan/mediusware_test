from itertools import product

from django.shortcuts import render
from django.views import generic
from product.models import Variant



class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


def productdetails(request):
    if request.method == 'POST':
     title = request.POST('title')
     sku = request.POST('sku')
     description = request.POST('description')

    allproduct = product(ptitle= title,psku = sku,pdescription = description)
    allproduct.save()
    return render(request,'products/list.html')



def productvarinttools(request):
    product_variant_one = request.POST('product_variant_one')
    product_variant_two = request.POST('product_variant_two')
    product_variant_three = request.POST('product_variant_three')
    price = request.POST('price')
    stock = request.POST('stock')
    product = request.POST('product')

    allproductvarinttools = productVariantPrice(p_varint_one = product_variant_one,p_varint_two = product_variant_two,p_varint_three = product_variant_three,p_price = price,p_stock = stock,p_product = product )
    allproductvarinttools.save()


    return render(request,'products/list.html')