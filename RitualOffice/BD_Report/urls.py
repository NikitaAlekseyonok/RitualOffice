from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeOrder.as_view(), name='home'),
    path('clients/', HomeClients.as_view(), name='clients'),
    path('edit_client/<int:pk>/', ClientUpdate.as_view(), name='edit_client'),
    path('delete_client/<int:pk>/', ClientDelete.as_view(), name='delete_client'),
    path('products/', HomeProduct.as_view(), name='products'),
    path('productsOrders/', HomeOrderProduct.as_view(), name='productorder'),
    path('productType/<int:productType_ID>/', ProductByType.as_view(), name='productType'),
    path('product/<int:pk>/', ViewProduct.as_view(), name='view_product'),
    path('productOrder/<int:pk>/', ViewProductOrder.as_view(), name='view_productorder'),
    path('edit_productOrder/<int:pk>/', ProductOrderUpdate.as_view(), name='edit_productorder'),
    path('delete_productOrder/<int:pk>/', ProductOrderDelete.as_view(), name='delete_productorder'),
    path('clients/<int:pk>/', ViewClient.as_view(), name='view_client'),
    path('orders/<int:pk>/', ViewOrder.as_view(), name='view_order'),
    path('edit_order/<int:pk>/', OrderUpdate.as_view(), name='edit_order'),
    path('delete_order/<int:pk>/', OrderDelete.as_view(), name='delete_order'),
    path('add_client/', CreateClient.as_view(), name='add_client'),
    path('add_order/', CreateOrder.as_view(), name='add_order'),
    path('add_productorder/', CreateProductOrder.as_view(), name='add_productorder'),

    path('request_1/', Request_1.as_view(), name='request_1'),
    path('request_2/', Request_2, name='request_2'),
    path('request_3/', Request_3, name='request_3'),
    path('request_4/', Request_4, name='request_4'),
]