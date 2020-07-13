from django.shortcuts import render
from .forms import PizzaForm
def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            cleaned_data = filled_form.cleaned_data
            note = 'Thanks for ordering. Your {} {} and {} pizza is on its way!'.format(cleaned_data['size'],cleaned_data['topping1'],cleaned_data['topping2'])
            new_form = PizzaForm()    
            return render(request, 'pizza/order.html',{'pizzaform':new_form, 'note':note})
    pizzaForm = PizzaForm()
    return render(request, 'pizza/order.html', {'pizzaform' : pizzaForm})
