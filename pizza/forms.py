from django import forms
from .models import Pizza
# class PizzaForm(forms.Form):
#     SIZE_CHOICES = [('Small', 'Small'),('Large', 'Large'), ('Large', 'Large')]
#     topping1 = forms.CharField(max_length=100, label="Topping 1:")
#     topping2 = forms.CharField(max_length=100, label="Topping 2:")
#     size = forms.ChoiceField(choices=SIZE_CHOICES, label="Size")

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {'topping1':'Topping 1', 'tooping2':'Topping 2'}
        
        
class MultipleForm(forms.Form):
    
    number = forms.IntegerField(min_value=2,max_value=6)
    