from django.contrib import admin

from .models import Post

class PostAdmin (admin.ModelAdmin):
    model = Post
    list_display = ('text',
                    'pub_date',
                    'author',
                    "group",
                    )
    list_editable = ("group",)
    search_fields = ('text',)
    list_filter = ('pub_date',)