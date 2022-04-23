
from .models import Profile,Message,Relationship

def message_received(request):
    
    if request.user.is_authenticated:
        profile=Profile.objects.get(user=request.user)
        re=Message.objects.filter(recepient=profile).count()
        return {"re":re,"prof":profile}
    return {}    

def invitations_no(request):
    if request.user.is_authenticated:
        profile=Profile.objects.get(user=request.user)
        no=Relationship.objects.invite_receive(profile).count()
        return {"no":no}
    return {}
