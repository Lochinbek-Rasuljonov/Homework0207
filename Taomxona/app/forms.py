from django import forms
from .models import Food, Comment

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'description', 'category', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Taom nomi'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Taom tavsifi',
                'rows': 3
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Narxi'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Izohingizni kiriting...', 'rows': 3}),
        }