from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(
        label='ФИО',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Иванова Мария Сергеевна'})
    )
    phone = forms.CharField(
        label='Телефон',
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': '+7 (999) 123-45-67'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'example@mail.ru'})
    )
    address = forms.CharField(
        label='Адрес доставки',
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'г. Москва, ул. Ленина, д. 1, кв. 1'})
    )
    comment = forms.CharField(
        label='Комментарий',
        required=False,
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Пожелания к заказу...'})
    )