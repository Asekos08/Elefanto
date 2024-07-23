from django.contrib import admin
from .models import Author, Genre, Book, Review, Favorite

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'author', 'publication_date', 'average_rating')
    search_fields = ('title', 'genre__name', 'author__name')
    list_filter = ('genre', 'author', 'publication_date')
    inlines = [ReviewInline]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'author', 'rating', 'text')
    search_fields = ('book__title', 'author__username')
    list_filter = ('rating',)

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'book')
    search_fields = ('user__username', 'book__title')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Favorite, FavoriteAdmin)
