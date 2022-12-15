from django.contrib import admin
from .models import Author, Publisher, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Publisher)
admin.site.register(Language)
#admin.site.register(BookImage)

# Define the admin class


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 
                    'date_of_birth', 'date_of_death')
    fields = ['name', ('date_of_birth', 'date_of_death'), 'intro']

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# @register 데코레이터(decorator) === admin.site.register() 구문과 정확히 똑같이 작동


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'pk', 'create_date', 'display_author', 'publisher', 'display_genre')
    inlines = [BooksInstanceInline]

    # genre는 ManyToManyField이기 때문에 직접적으로 특정할 수 없음.
    # def display_genre(self) 를 models.py에 적용시켜 줘야함


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'user', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

