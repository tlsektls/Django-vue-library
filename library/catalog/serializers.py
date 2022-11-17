from rest_framework import serializers
from .models import Book, Genre, BookInstance, Author, Publisher, NewsBoard


class genreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)


class BookSerializer(serializers.ModelSerializer):
    language = serializers.ReadOnlyField(source='language.name')
    genre = genreSerializer(many=True, allow_null=True)
    image = serializers.ImageField(use_url=True)

    author = serializers.SerializerMethodField()
    def get_author(self, obj):
        return f'{obj.author.last_name} {obj.author.first_name}'

    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'language', 'image')


class BookInstanceSerializer(serializers.ModelSerializer):
    book = serializers.ReadOnlyField(source='book.name')

    class Meta:
        model = BookInstance
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"


class NewsBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsBoard
        fields = "__all__"


