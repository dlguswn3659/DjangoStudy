from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance

# 모델 등록
# admin.site.register(Book)
# Register the Admin classes for Book using the decorator


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)  # 등록
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
# admin.site.register(Author)
# Define the admin class


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
# admin.site.register(BookInstance)
# Register the Admin classes for BookInstance using the decorator


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
    # pass    # 현재 모든 관리자 클래스가 비어있으므로 관리자 동작은 변경되지 않는다.
    # 이를 확장하여 모델 별 관리자 동작을 정의할 수 있다.
