from rest_framework import serializers
from catalog.models import Book, Genre, Author, BookInstance


class genreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)


class BookSerializer(serializers.ModelSerializer):

    language = serializers.ReadOnlyField(source='language.name')

    genre = genreSerializer(many=True, allow_null=True)

    author = serializers.SerializerMethodField()
    def get_author(self, obj):
        return f'{obj.author.last_name} {obj.author.first_name}'

    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'language', 'image')


class BookInstanceSerializer(serializers.ModelSerializer):

    book = serializers.ReadOnlyField(source='book.name')

    class Meta:
        model = BookInstance
        fields = "__all__"



        
#class GenreSerializer(serializers.ModelSerializer):
#    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

#    class Meta:
#        model = Genre
#        fields = ['name', 'books']



#class LanguageSerializer(serializers.ModelSerializer):
#    books = BookSerializer(many=True, read_only=True)

#    class Meta:
#        model = Language
