from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import *
from .forms import ClientForm, OrderForm, ProductOrderForm, Request2Form, Request4Form


class HomeOrder(ListView):
    model = Order
    template_name = 'BD_Report/index.html'
    context_object_name = 'orders'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список заказов'
        return context


class HomeProduct(ListView):
    model = Product
    template_name = 'BD_Report/products.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список товаров'
        context['productTypes'] = ProductType.objects.all()
        return context


class HomeOrderProduct(ListView):
    model = ProductOrder
    template_name = 'BD_Report/productorder.html'
    context_object_name = 'productorders'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список заказов товаров'
        return context


class ProductByType(ListView):
    model = Product
    template_name = 'BD_Report/products.html'
    context_object_name = 'products'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ProductType.objects.get(pk=self.kwargs['productType_ID'])
        context['productTypes'] = ProductType.objects.all()
        return context

    def get_queryset(self):
        return Product.objects.filter(productTypeID=self.kwargs['productType_ID'])


class HomeClients(ListView):
    model = Client
    template_name = 'BD_Report/clients.html'
    context_object_name = 'clients'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Клиенты'
        return context


class ViewClient(DetailView):
    model = Client
    context_object_name = 'client_item'
    template_name = 'BD_Report/view_client.html'


class ViewProduct(DetailView):
    model = Product
    context_object_name = 'product_item'
    template_name = 'BD_Report/view_product.html'


class ViewProductOrder(DetailView):
    model = ProductOrder
    context_object_name = 'item'
    template_name = 'BD_Report/view_productorder.html'


class ViewOrder(DetailView):
    model = Order
    context_object_name = 'order_item'
    template_name = 'BD_Report/view_order.html'


class CreateClient(CreateView):
    form_class = ClientForm
    template_name = 'BD_Report/add_client.html'


class CreateOrder(CreateView):
    form_class = OrderForm
    template_name = 'BD_Report/add_order.html'


class CreateProductOrder(CreateView):
    form_class = ProductOrderForm
    template_name = 'BD_Report/add_productorder.html'


class ClientUpdate(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'BD_Report/edit_client.html'


class ClientDelete(DeleteView):
    model = Client
    template_name = 'BD_Report/delete_client.html'
    success_url = reverse_lazy('clients')


class OrderUpdate(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'BD_Report/edit_order.html'


class OrderDelete(DeleteView):
    model = Order
    template_name = 'BD_Report/delete_order.html'
    success_url = reverse_lazy('orders')


class ProductOrderUpdate(UpdateView):
    model = ProductOrder
    form_class = ProductOrderForm
    template_name = 'BD_Report/edit_productorder.html'


class ProductOrderDelete(DeleteView):
    model = ProductOrder
    template_name = 'BD_Report/delete_productorder.html'
    success_url = reverse_lazy('productorder')


class Request_1(ListView):
    model = ProductType
    template_name = 'BD_Report/request_1.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запрос №1'
        productTypes = ProductType.objects.all()
        counts = []
        for i in productTypes:
            counts.append(Product.objects.filter(productTypeID=i.productTypeID).count())

        context['zip'] = zip(productTypes, counts)
        return context


def Request_2(request):
    if request.method == 'POST':
        order = request.POST.get("orders")
        result = Order.objects.get(orderID=order)
        context = {'title': 'Запрос №2',
                   'worker': result.workerID
                   }
        return render(request, template_name='BD_Report/request_2_result.html', context=context)
    else:
        query_form = Request2Form()
        orders = Order.objects.all()
        query_form.fields['orders'].choices = [(item.orderID, item.orderID) for item in orders]
        context = {'title': 'Запрос №2',
                   'form': query_form,
                   }
        return render(request, template_name='BD_Report/request_2.html', context=context)


def Request_3(request):
    positions = Position.objects.all()
    counts = []
    for i in positions:
        counts.append(Worker.objects.filter(positionID=i.positionID).count())

    context = {'title': 'Запрос №3',
               'zip': zip(positions, counts)
               }
    return render(request, template_name='BD_Report/request_3.html', context=context)


def Request_4(request):
    if request.method == 'POST':
        date1 = request.POST.get("date1")
        date2 = request.POST.get("date2")
        orders = Order.objects.filter(Q(date__gte=date1) & Q(date__lte=date2))
        workers = Worker.objects.all()
        counts = []
        result = 0
        for w in workers:
            count = 0
            for i in orders:
                if w.workerID == i.workerID.workerID:
                    count += 1
            counts.append(count)

        for i in range(1, len(counts)):
            if counts[i] > counts[result]:
                result = i

        context = {'title': 'Запрос №4',
                   'worker': workers[result],
                   'count': counts[result]
                   }
        return render(request, template_name='BD_Report/request_4_result.html', context=context)
    else:
        query_form = Request4Form()
        context = {'title': 'Запрос №4',
                   'form': query_form,
                   }
        return render(request, template_name='BD_Report/request_4.html', context=context)

