from django.contrib import admin

from .models import Client, Services, Hall, Discount, Position, Worker, Order, Product, ProductOrder, \
    ProductDiscounts, ProductType


class ClientAdmin(admin.ModelAdmin):
    list_display = ('clientID', 'surname', 'name', 'patronymic', 'phoneNumber')
    list_display_links = ('clientID',)
    search_fields = ('surname', 'name')


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('servicesID', 'name', 'price')
    list_display_links = ('servicesID',)
    search_fields = ('name',)


class HallAdmin(admin.ModelAdmin):
    list_display = ('hallID', 'name', 'price')
    list_display_links = ('hallID',)
    search_fields = ('name',)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('discountID', 'servicesID', 'discountAmount')
    list_display_links = ('discountID',)
    search_fields = ('description',)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('positionID', 'name', 'salary')
    list_display_links = ('positionID',)
    search_fields = ('name', 'salary')


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('workerID', 'surname', 'name', 'positionID')
    list_display_links = ('workerID',)
    search_fields = ('surname', 'name', 'positionID')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('orderID', 'clientID', 'date', 'time')
    list_display_links = ('orderID',)
    search_fields = ('date', 'clientID', 'time')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('productID', 'name', 'productTypeID', 'price')
    list_display_links = ('productID',)
    search_fields = ('name', 'price')


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('productTypeID', 'name')
    list_display_links = ('productTypeID',)
    search_fields = ('name',)


class ProductDiscountsAdmin(admin.ModelAdmin):
    list_display = ('discountID', 'discountAmount')
    list_display_links = ('discountID',)
    search_fields = ('discountAmount',)


class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('productOrderID', 'clientID', 'date', 'time')
    list_display_links = ('productOrderID',)
    search_fields = ('clientID', 'date', 'time')


admin.site.register(Client, ClientAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Hall, HallAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(ProductDiscounts, ProductDiscountsAdmin)
admin.site.register(ProductOrder, ProductOrderAdmin)

admin.site.site_header = 'Бюро ритуальных услуг'
admin.site.site_title = 'Бюро ритуальных услуг'
