from django.contrib import admin

from .models import Post, Group, Comment, Follow


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


class GroupAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )


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


class GroupAdmin (admin.ModelAdmin):
    

class CommentAdmin (admin.ModelAdmin):


class FollowAdmin (admin.ModelAdmin):


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment)
admin.site.register(Follow) 
