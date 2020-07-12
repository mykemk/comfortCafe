from django import forms

class PizzaForm(forms.Form):
    SIZE_CHOICES = [('Small', 'Small'),('Large', 'Large'), ('Large', 'Large')]
    topping1 = forms.CharField(max_length=100, label="Topping 1:")
    topping2 = forms.CharField(max_length=100, label="Topping 2:")
    size = forms.ChoiceField(choices=SIZE_CHOICES, label="Size")
    