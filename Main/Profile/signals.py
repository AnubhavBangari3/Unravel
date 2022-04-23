from .models import  Profile,Relationship
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_delete
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save,sender=Relationship)
def add_friend(sender,instance,created,**kwargs):
    send=instance.sender
    receive=instance.receiver
    # print('sender:',send)
    # print("receiver:",receive)
    if instance.status == 'accept':
        send.friends.add(receive.user)
        receive.friends.add(send.user)
        
        send.save()
        receive.save()

        
@receiver(pre_delete,sender=Relationship)
def unfriend(sender,instance,**kwargs):
    sender=instance.sender
    receive=instance.receiver
    sender.friends.remove(receive.user)
    receive.friends.remove(sender.user)