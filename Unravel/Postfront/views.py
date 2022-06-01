from django.shortcuts import render,redirect
from django.urls import reverse
from Post.models import Post,JoinGroup,JoinGroup,PostGroup,GroupChat,Rewards
from Profile.models import Profile
from Profile.forms import RewardForm
from collections import defaultdict
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def allPosts(request):
    profile=Profile.objects.get(user=request.user)
    user=request.user
    
    
    return render(request,"Postfront/allPost.html",{
        'profile': profile,
        'user': user,
        'profile_id': profile.id
    })
@login_required
def group_view(request,pk):
    g=JoinGroup.objects.get(pk=pk)
    profile=Profile.objects.get(user=request.user)
    L={}
    posts=PostGroup.objects.all()
    if request.method == 'POST':
        form=RewardForm(request.POST)
        post_id=request.POST.get('post_id')
        print(post_id,form)
        if form.is_valid():
            a=form.save(commit=False)
            a.person=profile
            a.group_post=PostGroup.objects.get(id=post_id)
            print(a)
            a.save()
            return redirect(reverse('group_view', kwargs={"pk": pk}))
    else:
        form=RewardForm()
        pass
        
    
    for p in posts:
        if p.group_post == g:
            
            L[p.id]=p.likegp.count()
    s = sorted(L.items(), key=lambda x: x[1], reverse=True)
    
    rewards=Rewards.objects.all()
    #It contains post id and rewards list it has received
    d=defaultdict(list)
    for re in rewards:
        #print(re.reward,re.group_post.group_post.id)
        #Checking the rewards received by the post int this group
        if pk == re.group_post.group_post.id:
        
            if re.group_post.id not in d:
                d[re.group_post.id].append(re.reward)
            else:
                d[re.group_post.id].append(re.reward)
   
    
    #For highest
    id_and_point=defaultdict(list)
    for k,v in d.items():
        #print(k,v)
        for i in v:
            
            if i == "pawn":
                id_and_point[k].append(10)
            elif i == "rook":
                id_and_point[k].append(35)
            elif i == "bishop":
                id_and_point[k].append(30)
            elif i == "knight":
                id_and_point[k].append(20)
            elif i == "queen":
                id_and_point[k].append(80)
            else:
                id_and_point[k].append(100)
    #print(id_and_point)
    best=0
    #It containe id and sum of all rewards 
    reward_sum=defaultdict(int)
    for k,v in id_and_point.items():
        if k:
            reward_sum[k]=sum(v)
    #print(reward_sum)
    #Highest reward
    if id_and_point.values():
        best=max(zip(reward_sum.values(), reward_sum.keys()))[1]
        
    #print("Best ",best)
    
    ans=defaultdict(set)
    for k,v in d.items():
        #pawn, rook, bishop, knight, queen king
        
        for i in v:
            if i not in ans:
                ans[k].add(str(i)+" "+"X" +" "+str(v.count(i)))
            else:
                ans[k].add(str(i)+" "+"X" +" "+str(v.count(i)))
    #print(dict(ans))
    
    return render(request,"Postfront/group.html",{'g':g,'profile':profile,'posts':posts,'best':best,'rewards':rewards,'form':form,
                                                  'ans':dict(ans)})

@login_required
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
@login_required
def getPost(request,id):
    post=Post.objects.get(pk=id)
    context={'post':post}
    
    return render(request,"Postfront/getPost.html",context)
@login_required
def getGroupPost(request,id):
    post=PostGroup.objects.get(pk=id)
    
    context={'post':post}
    
    return render(request,"Postfront/getgroupPost.html",context)
@login_required
def getGroupchat(request,id):
    group=JoinGroup.objects.get(pk=id)
    messages=GroupChat.objects.filter(group_chat=group)
    
    profile=Profile.objects.get(user=request.user)
    
    context={'group':group, 'profile':profile,'messages':messages}
    return render(request,"Postfront/groupchat.html",context)