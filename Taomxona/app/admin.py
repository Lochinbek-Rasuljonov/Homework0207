from django.contrib import admin
from .models import Category, Food, Comment

admin.site.register(Category)
admin.site.register(Food)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('food', 'user', 'text', 'created_at')
    search_fields = ('food__name', 'user__username', 'text')