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


class CommentAdmin (admin.ModelAdmin):
    model = Comment
    list_display = ('author',
                    'post',
                    'text',
                    "created",
                    )
    list_editable = ("post",)
    search_fields = ('text',)
    list_filter = ('created',)


class FollowAdmin (admin.ModelAdmin):
    model = Follow
    list_display = ('user',
                    'following',
                    )
    list_editable = ("following",)
    search_fields = ('user',)

admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin) 
