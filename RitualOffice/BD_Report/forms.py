from django import forms

from .models import Client, Order, ProductOrder, Product


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'}),
            'deceased_surname': forms.TextInput(attrs={'class': 'form-control'}),
            'deceased_name': forms.TextInput(attrs={'class': 'form-control'}),
            'deceased_patronymic': forms.TextInput(attrs={'class': 'form-control'}),
            'phoneNumber': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    # category = forms.ModelChoiceField(queryset=Category.objects.all())


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'clientID': forms.Select(attrs={'class': 'form-control'}),
            'workerID': forms.Select(attrs={'class': 'form-control'}),
            'hallID': forms.Select(attrs={'class': 'form-control'}),
            'servicesID': forms.Select(attrs={'class': 'form-control'}),
            'discountID': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'is_paid': forms.CheckboxInput(attrs={'class': 'form-control'})
        }


class ProductOrderForm(forms.ModelForm):
    class Meta:
        model = ProductOrder
        fields = '__all__'
        widgets = {
            'clientID': forms.Select(attrs={'class': 'form-control'}),
            'productID': forms.Select(attrs={'class': 'form-control'}),
            'discountID': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'is_paid': forms.CheckboxInput(attrs={'class': 'form-control'})
        }


class Request2Form(forms.Form):
    orders = forms.ChoiceField()


class DateInput(forms.DateInput):
    input_type = 'date'


class Request4Form(forms.Form):
    date1 = forms.DateField(label='C ', widget=DateInput)
    date2 = forms.DateField(label='по ', widget=DateInput)
