from rest_framework import serializers
from .models import Author, Genre, Book, Review, Favorite
from django.core.validators import MaxValueValidator, MinValueValidator


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'rating', 'text', 'book', 'author']
        read_only_fields = ['author']

    def validate_rating(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Rating must be between 1 and 5")
        return value
    
    def validate(self, data):
        request = self.context.get('request')
        if request and request.method == 'POST':
            user = request.user
            book = data.get('book')
            if Review.objects.filter(author=user, book=book).exists():
                raise serializers.ValidationError("You have already reviewed this book.")
        return data


class BookSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    author = AuthorSerializer()
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ['id', 'book', 'user']
        read_only_fields = ['user']

    def validate(self, data):
        request = self.context.get('request')
        if request and request.method == 'POST':
            user = request.user
            book = data.get('book')
            if Favorite.objects.filter(user=user, book=book).exists():
                raise serializers.ValidationError("You have already marked this book as favorite.")
        return data