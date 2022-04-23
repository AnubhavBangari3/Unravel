from django.urls import path

from .views import *

urlpatterns=[
    path("",profile,name="profile"),
    path("<int:id>",getProfile,name="getProfile"),
    path("suggestion",suggestion,name="suggestion"),
    path("accept_request",accept_request,name="accept"),
    path("reject_request",reject_request,name="reject"),
    path("remove_friend",remove_friend,name="unfriend"),
    path("inbox",inbox,name="inbox"),
    path("Message/<int:id>",getSenderMessage,name="getSenderMessage"),
    path("sent",sentMessage,name="sentMessage"),
    path("updateProfile",updateProfile,name="updateProfile"),
    path("searchProfile",searchProfile,name="searchProfile")
    
]