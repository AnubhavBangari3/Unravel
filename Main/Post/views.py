from django.shortcuts import render, resolve_url,get_object_or_404
from django.http import HttpResponse,JsonResponse

from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializers,LikeSerializer,JoinGroupSerializer,GroupPostSerializer,CreateGroupSerializer,LikeGroupPostSerializer,FriendRequestSerializer,CommentSerializer,CommentGpostSerializer,sendMessageSerializer,groupChatSerializer,RewardSerializer
from rest_framework import status

from rest_framework.parsers import MultiPartParser,FormParser,JSONParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Post,Liked,JoinGroup,PostGroup,LikedGroupPost,CommentOnPost,CommentOnGroupPost,GroupChat,Rewards
from Profile.models import Profile,Relationship,Message

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt

from django.db.models import Q
# Create your views here.

@api_view(["GET"])
def Posting(request):
    post=Post.objects.all()
    serializer=PostSerializers(post,many=True)

    return Response(serializer.data)
@api_view(["GET"])
def SinglePost(request,pk):
    post=Post.objects.filter(pk=pk)
    serializer=PostSerializers(post,many=True)

    return Response(serializer.data)

# @api_view(["POST"])
# def Creating(request):
#     serializer=PostSerializers(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#     else:
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     return Response(serializer.data)
'''
After being struck at this error for 1.5 month. I was able to resolve it on 13-12-2021.
Compund efforts are necessary for acheiving your goal.
'''
class Creating(APIView):

    parser_classes = [MultiPartParser, FormParser]
    permission_classes=[IsAuthenticated]

    def post(self,request,format=None):
        profile=Profile.objects.get(user=request.user)

        serializer=PostSerializers(data=request.data)

        if serializer.is_valid(raise_exception=True):
            #author is the foregin key of Post that contains the primary key of Profile(user)
            serializer.save(author=profile)
           # print("working:",request.data)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
           # print("Not working:",serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


'''
I have solved this problem on 5-1-22.
Compund efforts are necessary for acheiving your goals.
'''
class UpdatePost(ModelViewSet):
    serializer_class=PostSerializers
    parser_classes = [MultiPartParser, FormParser]
    permission_classes=[IsAuthenticated]
    queryset=Post.objects.all()

    def update(self,request,*args, **kwargs):
        instance=self.get_object()
        #print('Up:',instance)
        profile=Profile.objects.get(user=self.request.user)
        serializer=self.get_serializer(instance=instance,data=request.data)
       # print("s:",request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=profile)
        return Response(serializer.data)

#done on 6-1-22
class DeletePost(ModelViewSet):
    serializer_class=PostSerializers
    queryset=Post.objects.all()

    def destroy(self,request,*args,**kwargs):
        instance=self.get_object()
        #print("Working:",instance)
        profile=Profile.objects.get(user=self.request.user)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


#Completed on 20-1-22
class Like(APIView):
    serializer_class=LikeSerializer
    permission_classes=[IsAuthenticated]
    
        
    def post(self,request,pk):
        likeuser=Profile.objects.get(user=self.request.user)
        likepost=get_object_or_404(Post,pk=pk)
        #print(likeuser,likepost,pk)
        serializer=LikeSerializer(data=request.data)
        '''
        if current user has already liked the post then unlike it.
        '''
        if likeuser in likepost.like.all():
            likepost.like.remove(likeuser)
            #print("Unlike")
        else:
            likepost.like.add(likeuser)
            #print("Like")
        #condition to check if liked by the user and that post has been created   
        check=Liked.objects.filter(Q(user=likeuser) & Q(post=likepost))
        if(check.exists()):
            #if already liked then delete the like
            check.delete()
            return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message":"Already Liked"
            })
        #else create a like
        new_like=Liked.objects.create(post=likepost,user=likeuser)
        
        
        new_like.save()
        serializer=LikeSerializer(new_like)
        
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
         
class JoinGroupView(APIView):
    serializer_class=JoinGroupSerializer
    permission_classes=[IsAuthenticated]
    
    def get(self,request,pk):
        group_id=get_object_or_404(JoinGroup,pk=pk)
        serializer=JoinGroupSerializer(group_id,many=False)
        return Response(serializer.data)
    
    def post(self,request,pk):
        group_id=get_object_or_404(JoinGroup,pk=pk)
        new_member=Profile.objects.get(user=self.request.user)
        
        
        if new_member in group_id.members.all():
            group_id.members.remove(new_member)
            #print("Exited from group")
        else:
            group_id.members.add(new_member)
            #print("Joined the group")
        return Response({"Success":"Added"},status=status.HTTP_200_OK)
    

class CreateGroup(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes=[IsAuthenticated]
    
    def post(self, request,format=None):
        
        
        profile=Profile.objects.get(user=request.user)
        serializer=CreateGroupSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save(owner=profile)
            
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            #print("Not working:",serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#22-2-2022
class GroupPostView(APIView):
    #GroupPostSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes=[IsAuthenticated]
    
    def post(self,request,pk,format=None):
        profile=Profile.objects.get(user=request.user)
        groupName=get_object_or_404(JoinGroup,pk=pk)
        
        serializer=GroupPostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(group_post=groupName,posted_by=profile)
            # print("working:",serializer.data)
            # print("working:",request.data)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            
            #print("Not working:",serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#It is working fine. But I have removed it.Instead I have used form for it now.      
class RewardsView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes=[IsAuthenticated]
    
    def post(self,request,pk,format=None):
        profile=Profile.objects.get(user=request.user)
        gp=get_object_or_404(PostGroup,pk=pk)
        print("Profile {}- {}".format(profile,gp))
        serializer=RewardSerializer(data=request.data)
        
        #print(serializer)reward_earner
        #print(request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(group_post=gp,person=profile)
            print("working:",serializer.data)
            print("working:",request.data)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            
            print("Not working:",serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#Done on 27-2-2022.
#Update
class UpdateGroupPost(ModelViewSet):
    serializer_class=GroupPostSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes=[IsAuthenticated]
    queryset=PostGroup.objects.all()
    #print(queryset)
    def update(self,request,*args, **kwargs):
        # print("Request data:",request.data)
        # print('Instance:',instance)
        instance=self.get_object()
        profile=Profile.objects.get(user=self.request.user)
        
        serializer=GroupPostSerializer(instance=instance,data=request.data)
        #serializer=self.get_serializer(instance=instance,data=request.data)
        if serializer.is_valid(raise_exception=True):
          
            
            #serializer.is_valid(raise_exception=True)

            serializer.save(posted_by=profile)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            print("Not working:",serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#Done on 27-2-22      
class DeleteGroupPost(ModelViewSet):
    serializer_class=GroupPostSerializer
    queryset=PostGroup.objects.all()

    def destroy(self,request,*args,**kwargs):
        instance=self.get_object()
        #print("Working:",instance)
        profile=Profile.objects.get(user=self.request.user)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
     
#This was done in 30 minutes by using the logic used earlier for Like.
#3-3-22           
class Like_goup_post(APIView):
    serializer_class=LikeGroupPostSerializer
    permission_classes=[IsAuthenticated]
    
        
    def post(self,request,pk):
        likeuser=Profile.objects.get(user=self.request.user)
        likepost=get_object_or_404(PostGroup,pk=pk)
        #print(likeuser,likepost,pk)
        serializer=LikeGroupPostSerializer(data=request.data)
        '''
        if current user has already liked the post then unlike it.
        '''
        if likeuser in likepost.likegp.all():
            likepost.likegp.remove(likeuser)
            print("Unlike")
        else:
            likepost.likegp.add(likeuser)
            print("Like")
        #condition to check if liked by the user and that post has been created   
        check=LikedGroupPost.objects.filter(Q(user=likeuser) & Q(postgroup=likepost))
        if(check.exists()):
            #if already liked then delete the like
            check.delete()
            return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message":"Already Liked"
            })
        #else create a like
        new_like=LikedGroupPost.objects.create(postgroup=likepost,user=likeuser)
        
        
        new_like.save()
        serializer=LikeGroupPostSerializer(new_like)
        
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    

    
class friendRequest(APIView):
    serializer_class=FriendRequestSerializer
    permission_classes=[IsAuthenticated]
    
    def post(self,request,pk):
        sender=Profile.objects.get(user=request.user)
        receiver=Profile.objects.get(pk=pk)
        print(sender,receiver)
        serializer=FriendRequestSerializer(request.data)
        
        if receiver in sender.friends.all():
            #print("Already a friend!")
            return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message":"Already friend"
            })
        
        already_send=Relationship.objects.filter(Q(sender=sender) & Q(receiver=receiver) & Q(status="send"))
      
        if already_send.exists():
            print("Already sent!")
            
            return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message":"Friend request already sent"
            })
        send_fr=Relationship.objects.create(sender=sender,receiver=receiver,status='send')
        send_fr.save()
        
            
        serializer=FriendRequestSerializer(send_fr)
        #print("Send FR",serializer)
        
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    

class CommentPost(APIView):
    #CommentSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes=[IsAuthenticated]
    
    @csrf_exempt
    def post(self,request,pk,format=None):
        profile=Profile.objects.get(user=request.user)
        P=get_object_or_404(Post,pk=pk)
        print(profile,P)
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=profile,post=P)
            # print("working:",serializer.data)
            # print("working:",request.data)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            
            #print("Not working:",serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
#CommentGpostSerializer
class CommentGPPost(APIView):
    #CommentSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes=[IsAuthenticated]
    
    @csrf_exempt
    def post(self,request,pk,format=None):
        profile=Profile.objects.get(user=request.user)
        P=get_object_or_404(PostGroup,pk=pk)
        print(profile,P)
        serializer=CommentGpostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=profile,post=P)
            #print("working:",serializer.data)
            #print("working:",request.data)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            
            #print("Not working:",serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 

class sendMessage(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes=[IsAuthenticated]
    
    def post(self,request,pk):
        current_user=Profile.objects.get(user=request.user)
        sender=Profile.objects.get(user=request.user)
        receiver=Profile.objects.get(id=pk)
        
        serializer=sendMessageSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=current_user,sender=sender,recepient=receiver)
            #print("working:",serializer.data)
            #print("working:",request.data)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            #print("Not working:",serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#23-3-22 DOne
class DeleteMessage(ModelViewSet):
    serializer_class=sendMessageSerializer
    queryset=Message.objects.all()

    def destroy(self,request,*args,**kwargs):
        instance=self.get_object()
        #print("Working:",instance)
        
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class GroupChatMessage(APIView):
    #groupChatSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes=[IsAuthenticated]
    
    def post(self,request,pk):
        group=get_object_or_404(JoinGroup,pk=pk)
        profile=Profile.objects.get(user=self.request.user)
        
        serializer=groupChatSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(group_chat=group,sender=profile)
            # print("working:",serializer.data)
            # print("working:",request.data)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            #print("Not working:",serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)