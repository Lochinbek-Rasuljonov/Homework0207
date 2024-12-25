from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('foods/', views.all_foods, name='all_foods'),
    path('food/<int:food_id>/', views.food_detail, name='food_detail'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('category/<int:category_id>/', views.category_foods, name='category_foods'),
    path('food/add/', views.add_food, name='add_food'),
    path('food/edit/<int:food_id>/', views.edit_food, name='edit_food'),
]