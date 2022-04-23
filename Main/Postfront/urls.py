from django.urls import path
from .views import *

urlpatterns=[
    path("",allPosts,name="allPosts"),
    path("groups",allGroup,name="groups"),
    path("groups/<int:pk>/",group_view,name="group_view"),
    path("single_post/<int:id>",getPost,name="getPost"),
    path("groupPost/<int:id>",getGroupPost,name="getGroupPost"),
    path("groups/<int:id>/groupchat",getGroupchat,name="getGroupchat")
    
]