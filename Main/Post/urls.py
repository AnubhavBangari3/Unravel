from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("Update",UpdatePost,basename="update")
router.register("Delete",DeletePost,basename="delete")
router.register("UpdateGroupPost",UpdateGroupPost,basename="updateGroupPost")
router.register("DeleteGroupPost",DeleteGroupPost,basename="deleteGroupPost")
router.register("DeleteMessage",DeleteMessage,basename="deleteMessage")

urlpatterns=[
    path("Posts",Posting,name="posting"),
    path("Posts/<int:pk>",SinglePost,name="singlepost"),
    path("Posts/<int:pk>/comment",CommentPost.as_view(),name="commentPost"),
    path("Create",Creating.as_view(),name="create"),
    path("Posts/<int:pk>/like",Like.as_view(),name="like"),
    path("Groups/join/<int:pk>/",JoinGroupView.as_view(),name="joingroup"),
    path("Groups/join/<int:pk>/post/",GroupPostView.as_view(),name="grouppost"),
    path("Groups/join/post/<int:pk>/like_group_post",Like_goup_post.as_view(),name="grouppost_like"),
    path("CreateGroup",CreateGroup.as_view(),name="creategroup"),
    path("Group/<int:pk>/comment",CommentGPPost.as_view(),name="comment_on_gp"),
    path("FriendRequest/<int:pk>",friendRequest.as_view(),name="sendfriendRequest"),
    path("sendingMessage/<int:pk>",sendMessage.as_view(),name="sendMessage"),#RewardsView
    path("Groups/join/post/<int:pk>/reward",RewardsView.as_view(),name="reward"),
    path("Group/<int:pk>/chat",GroupChatMessage.as_view(),name="groupchats"),
    path('',include(router.urls)),
    
    
]