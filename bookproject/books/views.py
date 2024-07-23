from rest_framework import viewsets, permissions, status, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Genre, Book, Review, Favorite
from .serializers import AuthorSerializer, GenreSerializer, BookSerializer, ReviewSerializer, FavoriteSerializer

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genre__name', 'author__name', 'publication_date']
    permission_classes = [permissions.IsAuthenticated]  # Restrict access to authenticated users

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]  # Restrict access to authenticated users

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReviewViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'], url_path='my-reviews')
    def my_reviews(self, request):
        user = request.user
        reviews = Review.objects.filter(author=user)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

class FavoriteViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], url_path='my-favorites')
    def my_favorites(self, request):
        user = request.user
        favorites = Favorite.objects.filter(user=user)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)

