from django.shortcuts import render, redirect
from .models import Pizza
from .forms import CommentForm
# Create your views here.

def index(request):
    """The Home Page for Pizza App"""
    return render(request, 'pizza/index.html')

def pizza(request):
    pizza = Pizza.objects.order_by('date_added')

    context = {'pizza':pizza}

    return render(request, 'pizza/pizza.html', context)

def p(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza':pizza, 'toppings':toppings}

    return render(request, 'pizza/p.html', context)

def new_comment(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():

            new_comment = form.save(commit=False)

            new_comment.pizza = pizza
            new_comment.save()
            form.save()
        
            return redirect('pizza:pizza', pizza_id=pizza_id)

    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizza/new_comment.html', context)
