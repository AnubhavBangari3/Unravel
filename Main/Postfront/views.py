from django.shortcuts import render
from Post.models import Post,JoinGroup,JoinGroup,PostGroup,GroupChat
from Profile.models import Profile


# Create your views here.

def allPosts(request):
    profile=Profile.objects.get(user=request.user)
    user=request.user
    
    
    return render(request,"Postfront/allPost.html",{
        'profile': profile,
        'user': user,
        'profile_id': profile.id
    })

def group_view(request,pk):
    g=JoinGroup.objects.get(pk=pk)
    profile=Profile.objects.get(user=request.user)
    

   
    posts=PostGroup.objects.all()
    return render(request,"Postfront/group.html",{'g':g,'profile':profile,'posts':posts})


def allGroup(request):
    group=JoinGroup.objects.all()
    profile=Profile.objects.get(user=request.user)
    
    Programming=JoinGroup.objects.filter(category='Programming')
    Sports=JoinGroup.objects.filter(category='Sports')
    Entertainment=JoinGroup.objects.filter(category='Entertainment')
    Health=JoinGroup.objects.filter(category='Health')
    Fitness=JoinGroup.objects.filter(category='Fitness')
    Meditation=JoinGroup.objects.filter(category='Meditation')
    Music=JoinGroup.objects.filter(category='Music')
          
    return render(request,"Postfront/allGroup.html",{
       'groups':group ,
      'profile':profile,
      'Programming':Programming,'Sports':Sports,
      'Entertainment':Entertainment,'Health':Health,'Fitness':Fitness,
      'Meditation':Meditation,'Music':Music
    })

def getPost(request,id):
    post=Post.objects.get(pk=id)
    context={'post':post}
    
    return render(request,"Postfront/getPost.html",context)

def getGroupPost(request,id):
    post=PostGroup.objects.get(pk=id)
    
    context={'post':post}
    
    return render(request,"Postfront/getgroupPost.html",context)

def getGroupchat(request,id):
    group=JoinGroup.objects.get(pk=id)
    messages=GroupChat.objects.filter(group_chat=group)
    
    profile=Profile.objects.get(user=request.user)
    
    context={'group':group, 'profile':profile,'messages':messages}
    return render(request,"Postfront/groupchat.html",context)