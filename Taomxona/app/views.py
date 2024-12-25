from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Food, Comment
from .forms import FoodForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    foods = Food.objects.all()
    return render(request, 'home.html', {'foods': foods})

def all_foods(request):
    foods = Food.objects.all()
    return render(request, 'all_food.html', {'foods': foods})

def food_detail(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    comments = food.comments.all()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.food = food
            comment.user = request.user
            comment.save()
            return redirect('food_detail', food_id=food.id)
    else:
        form = CommentForm()

    return render(request, 'food_detail.html', {
        'food': food,
        'comments': comments,
        'form': form,
        'user': request.user,
    })

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user or request.user.is_superuser:
        comment.delete()
    return redirect('food_detail', food_id=comment.food.id)

def category_foods(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    foods = Food.objects.filter(category=category)
    return render(request, 'category_foods.html', {'category': category, 'foods': foods})

def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_foods')
    else:
        form = FoodForm()
    return render(request, 'add_food.html', {'form': form})

def edit_food(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_detail', food_id=food.id)
    else:
        form = FoodForm(instance=food)
    return render(request, 'edit_food.html', {'form': form, 'food': food})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})