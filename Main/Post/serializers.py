from rest_framework import serializers
from .models import Post,JoinGroup,PostGroup,LikedGroupPost,CommentOnPost,CommentOnGroupPost,GroupChat,Rewards
from Profile.models import Profile,Relationship,Message
from .models import Liked
from django.contrib.auth.models import User


class PostSerializers(serializers.ModelSerializer):
    
    image=serializers.ImageField()
    author =serializers.PrimaryKeyRelatedField(read_only=True)
    total_likes=serializers.SerializerMethodField()
    username=serializers.SerializerMethodField("getName")
    commentC=serializers.SerializerMethodField("getCommentCount")
    class Meta:
        model=Post
        
        fields=("id","author","text","image","like","total_likes","username","commentC",)
        #video
    
    def get_total_likes(self,instance):
        return instance.like.all().count()
    def getName(self,instance):
        return instance.author.user.username
    def getCommentCount(self,instance):
        return instance.comment_post.count()
   
        
class LikeSerializer(serializers.ModelSerializer):
    post=serializers.PrimaryKeyRelatedField(read_only=True)
    user=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Liked
        fields=('user','post',)
    
class JoinGroupSerializer(serializers.ModelSerializer):
    #owner=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=JoinGroup
        fields=('id','owner','members',)
        #read_only_fields=('owner_id','owner',)
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['owner'] = JoinGroupSerializer(instance.program).data
        return response
    
class GroupPostSerializer(serializers.ModelSerializer):
    group_image=serializers.ImageField()
    group_post=serializers.PrimaryKeyRelatedField(read_only=True)
    posted_by=serializers.PrimaryKeyRelatedField(read_only=True)
    #group_post_total_likes=serializers.SerializerMethodField()
    
    class Meta:
        model=PostGroup
        fields=('id','group_post','posted_by','group_text','group_image',)
    # def group_post_total_likes(self,instance):
    #         return instance.likegp.all().count()
        
class CreateGroupSerializer(serializers.ModelSerializer):
    owner=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=JoinGroup
        fields=('name','category','owner','description',)
#Not using it. I have removed it      
class RewardSerializer(serializers.ModelSerializer):
    group_post=serializers.PrimaryKeyRelatedField(read_only=True)
    person=serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model=Rewards
        fields=('group_post','person','reward',)
 
class LikeGroupPostSerializer(serializers.ModelSerializer):
    postgroup=serializers.PrimaryKeyRelatedField(read_only=True)
    user=serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model=LikedGroupPost
        fields=('user','postgroup',)
        
class FriendRequestSerializer(serializers.ModelSerializer):
    sender=serializers.PrimaryKeyRelatedField(read_only=True)
    receiver=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Relationship
        fields=('sender','receiver',)
        
class AcceptRequestSerializer(serializers.ModelSerializer):
    sender=serializers.PrimaryKeyRelatedField(read_only=True)
    receiver=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Relationship
        fields=('id','sender','receiver','status',)
        
class CommentSerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(read_only=True)
    post=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=CommentOnPost
        fields=('user','post','body',)


class CommentGpostSerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(read_only=True)
    post=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=CommentOnGroupPost
        fields=('user','post','body',)
        
class sendMessageSerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(read_only=True)
    sender=serializers.PrimaryKeyRelatedField(read_only=True)
    recepient=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Message
        fields=('user','sender','recepient','body',)
        
class groupChatSerializer(serializers.ModelSerializer):
    group_chat=serializers.PrimaryKeyRelatedField(read_only=True)
    sender=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=GroupChat
        fields=('group_chat','sender','message_body',)