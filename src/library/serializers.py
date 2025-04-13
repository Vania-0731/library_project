from rest_framework import serializers
from .models import Author, AuthorProfile, Book, Category, Publisher, Publication


class AuthorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorProfile
        fields = ['website', 'twitter_handle', 'photo']


class AuthorSerializer(serializers.ModelSerializer):
    profile = AuthorProfileSerializer(read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date', 'biography', 'profile']


class CategorySerializer(serializers.ModelSerializer):
    book_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'book_count']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'website', 'email']


class PublicationSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()

    class Meta:
        model = Publication
        fields = ['date_published', 'country', 'publisher']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    categories = CategorySerializer(many=True)
    publications = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'isbn', 'publication_date',
            'summary', 'author', 'categories', 'publications'
        ]

    def get_publications(self, obj):
        publications = obj.publication_set.select_related('publisher').all()
        return PublicationSerializer(publications, many=True).data
