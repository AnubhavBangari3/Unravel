from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile,Relationship,Message
from Post.models import Post,Liked,CommentOnPost
from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileFOrm

# Create your views here.
@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    posts=Post.objects.filter(author=profile)
    form =ProfileFOrm(request.POST or None,request.FILES or None,instance=profile)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    l=[]
   
    p=[]
    all_post=Post.objects.filter(author=profile)
    for i in all_post:
        l.append(i.like.count())
        p.append(i.id)
    #Total friends of this profile
    no_of_friends=profile.friends.count()

    #TO keep count of total likes received by the profile
    total_likes=0
    for i in l:
        total_likes+=i
    #print("Total likes:",total_likes)
    comment_on_user_post=[] 
    for i in p:
        comment_on_user=CommentOnPost.objects.filter( Q(post=i)).count()
        comment_on_user_post.append(comment_on_user)
        
    #TO keep count of total comments received by the post created from this profile
    total_comments=0
    for i in comment_on_user_post:
        total_comments+=i
    #print("TOtal comments:",total_comments)    
    #engagement_rate=(total_likes+total_comments)/no_of_friends*100
    
    
    context={
        'profile': profile,'posts': posts,'post_count': len(posts),'user':request.user,'p':p,'l':l,'form':form,"total_likes":total_likes,
        "total_comments":total_comments,
        
    }
    return render(request,"Profile/profile.html",context)
#For showing unique profile
'''
DOne on 7-3-22
'''
@login_required
def getProfile(request,id):
    profile=Profile.objects.get(id=id)
    posts=Post.objects.filter(author=profile)
    print(posts)
    current_profile=Profile.objects.get(user=request.user)

    receive_by=Relationship.objects.filter(receiver=current_profile)#current profile is the receiver
    send_by=Relationship.objects.filter(sender=current_profile)
    #print("Sender",send_by)
    received_by=[]
    sended_by=[]
    
    for item in receive_by:
        #It contains all the frien request sender
        received_by.append(item.sender.user)
    for item in send_by:
        sended_by.append(item.receiver.user)
    #print("Received by:",received_by)
    #print("Sender:",sended_by)
    l=[]
    p=[]
    for i in posts:
        l.append(i.like.count())
        p.append(i.id)
    

    #TO keep count of total likes received by the profile
    total_likes=0
    for i in l:
        total_likes+=i
    #print("Total likes:",total_likes)
    comment_on_user_post=[] 
    for i in p:
        comment_on_user=CommentOnPost.objects.filter( Q(post=i)).count()
        comment_on_user_post.append(comment_on_user)
        
    #TO keep count of total comments received by the post created from this profile
    total_comments=0
    for i in comment_on_user_post:
        total_comments+=i
    #print("TOtal comments:",total_comments) 
    
    context={
        'profile': profile,'posts': posts,'post_count': len(posts),'user':request.user,'current_profile':current_profile,
        'received_by':received_by,'sended_by':sended_by,"total_likes":total_likes,"total_comments":total_comments
    }
    return render(request,"Profile/getProfile.html",context)
    
#TO show profiles and friend request

@login_required
def suggestion(request):
    profile=Profile.objects.all().exclude(user=request.user)
    current_profile=Profile.objects.get(user=request.user)
    
    qs=Relationship.objects.invite_receive(current_profile)
    
    
    receive_by=Relationship.objects.filter(receiver=current_profile)#current profile is the receiver
    send_by=Relationship.objects.filter(sender=current_profile)
    
    received_by=[]
    sended_by=[]
    
    for item in receive_by:
        #It contains all the frien request sender
        received_by.append(item.sender.user)
    
    for item in send_by:
        sended_by.append(item.receiver.user)
    #print("List:",received_by)
    # print("Sender",sended_by)
    # print("Receiver:",received_by)
    results=list(map(lambda x:x.sender,qs))
    isEmpty=False
    if len(results) == 0:
        isEmpty=True
    context={'profile':profile,
             'results':results,
        'isEmpty':isEmpty,'received_by':received_by,'current_profile':current_profile,'sended_by':sended_by}
    
    return render(request,"Profile/suggestion.html",context)
@login_required
def accept_request(request):
    if request.method == 'POST':
        pk=request.POST.get('pro')
        sender=Profile.objects.get(pk=pk)
        receiver=Profile.objects.get(user=request.user)
        
        rel=get_object_or_404(Relationship,sender=sender,receiver=receiver)
        
        if rel.status == 'send':
            rel.status ='accept'
            
            rel.save()
    return redirect('suggestion')

@login_required
def reject_request(request):
    if request.method == 'POST':
        pk=request.POST.get('prof')
        sender=Profile.objects.get(pk=pk)
        receiver=Profile.objects.get(user=request.user)
        
        rel=get_object_or_404(Relationship,sender=sender,receiver=receiver,status="send")
        rel.delete()
    return redirect('suggestion')

@login_required
def remove_friend(request):
    if request.method == 'POST':
        pk=request.POST.get("getPro")
        sender=Profile.objects.get(user=request.user)
        receiver=Profile.objects.get(pk=pk)
        
        rel=Relationship.objects.filter(Q(sender=sender)& Q(receiver=receiver) | Q(sender=receiver) & Q(receiver=sender))
        
        rel.delete()
    return redirect('suggestion')

##Everything is working fine.Need to change Inbox -> Send message and received message
@login_required
def inbox(request):
    profile=Profile.objects.get(user=request.user)
    received_message=Message.objects.filter(recepient=profile)
    
    if received_message:
        message=received_message[0]
        direct=Message.objects.filter(recepient=profile).order_by('-created')
        direct.update(is_read=True)
    else:
        direct={}
    #print(received_message)
    context={
        'profile': profile,'received_message': received_message,'direct':direct
    }
    
    return render(request,"Profile/inbox.html",context)

'''
I have removed this from template. SO it is usless right now.
It consist of message received from sender and receiver reply
'''
def getSenderMessage(request,id):
    sender=Profile.objects.get(id=id)
    receipient=Profile.objects.get(user=request.user)
    message=Message.objects.filter(Q(recepient=receipient) & Q(sender=sender))
    message_sended_by_user=Message.objects.filter(Q(recepient=sender) & Q(sender=receipient))
    #print(message)
    context={
        'sender': sender,'receipient':receipient,"message":message,
        'message_sended_by_user':message_sended_by_user
    }
    
    return render(request,"Profile/getSenderMessage.html",context)



def sentMessage(request):
    profile=Profile.objects.get(user=request.user)
    sent=Message.objects.filter(sender=profile).order_by('-created')
    
    context={
        'profile':profile,'sent':sent
    }
    
    return render(request,"Profile/sentMessage.html",context)

@login_required
def updateProfile(request):
    profile = Profile.objects.get(user=request.user)
    posts=Post.objects.filter(author=profile)
    form =ProfileFOrm(request.POST or None,request.FILES or None,instance=profile)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    context={
        "form":form,"profile":profile
    }
    return render(request,"Profile/updateProfile.html",context)
@login_required
def searchProfile(request):
    if request.method == 'POST':
        search=request.POST.get("searchName")
        #print(search)
        profile=Profile.objects.filter(Q(user__username__icontains=search)).exclude(user=request.user)
        
        context={
        "search":search,"profile":profile
    }
        return render(request,"Profile/search.html",context)

'''
#Update the layout now
22-4-22 til 26-4-22
Improve
1) What you can. Eg Updating
2) Add features that can be added. Eg Reward,best post etc
3) Messaging 
4)Like unlike button
'''

    

    
    
    


    
    
