from django.contrib import admin
from django.urls import path

import pizza.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',pizza.views.home,name='home'),
    path('order',pizza.views.order,name='order'),
    path('pizzas', pizza.views.pizzas,name='pizzas')
]
