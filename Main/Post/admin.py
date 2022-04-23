from django.contrib import admin
from .models import Post,Liked,JoinGroup,PostGroup,LikedGroupPost,CommentOnPost,CommentOnGroupPost,GroupChat

# Register your models here.

admin.site.register(Post)
admin.site.register(Liked)
admin.site.register(JoinGroup)
admin.site.register(PostGroup)
admin.site.register(LikedGroupPost)
admin.site.register(CommentOnPost)
admin.site.register(CommentOnGroupPost)
#admin.site.register(Rewards)
admin.site.register(GroupChat)
