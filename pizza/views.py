from django.shortcuts import render
from .forms import PizzaForm, MultipleForm
from django.forms import formset_factory
from .models import Pizza

def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_form = MultipleForm()
    
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.pk
            cleaned_data = filled_form.cleaned_data
            note = 'Thanks for ordering. Your {} {} and {} pizza is on its way!'.format(cleaned_data['size'],cleaned_data['topping1'],cleaned_data['topping2'])
            new_form = PizzaForm()    
            return render(request, 'pizza/order.html',{'created_pizza_pk':created_pizza_pk,'pizzaform':new_form, 'note':note, 'multiple_form':multiple_form})
    pizzaForm = PizzaForm()
    return render(request, 'pizza/order.html', {'pizzaform' : pizzaForm,'multiple_form':multiple_form})


def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultipleForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = 'Pizzas has been ordered'
        else:
            note = 'Order was not created, please try again'
        return render(request, 'pizza/pizzas.html',{'note':note, 'formset':formset})
    else:
        return render(request, 'pizza/pizzas.html',{'formset':formset})
        

def edit_order(request,pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Order has been updated successfully.'
            return render(request, 'pizza/edit-order.html',{'pizzaform':form, 'pizza':pizza,'note':note})
    return render(request, 'pizza/edit-order.html',{'pizzaform':form, 'pizza':pizza})