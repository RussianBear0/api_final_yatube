from django.contrib import admin
from posts.models import Follow

class FollowAdmin(admin.ModelAdmin):
    model = Follow
    list_display = ('user',
                    'following')
    search_fields = ('user',)


admin.site.register(Follow, FollowAdmin)