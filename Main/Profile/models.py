from django.db import models
from django.contrib.auth.models import User
#for slugs
from .utils import  get_random_code
from django.template.defaultfilters import slugify

# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="profile_users")
    first_name=models.CharField(max_length=200,null=True,blank=True)
    last_name=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(max_length=200,null=True,blank=True)
    about=models.TextField(max_length=255,default="No description")
    
    background=models.ImageField(default="cover4.jpg",upload_to="Profile_background",blank=True,null=True)
    main_photo=models.ImageField(default="cover2.jpg",upload_to="Profile_main",blank=True,null=True)
    
    slug=models.SlugField(unique=True,blank=True)
    
    friends=models.ManyToManyField(User,related_name="friends",blank=True)
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    def get_friends_count(self):
        return self.friends.count()
    
    
    '''save method is the helper method to create dynamic slugs for names'''
    def save(self, *args, **kwargs):
        ex=False
        if self.first_name and self.last_name:
            to_slug=slugify(str(self.first_name)+""+str(self.last_name))
            ex=Profile.objects.filter(slug=to_slug).exists()
            
            while ex:
                to_slug=slugify(to_slug+""+str(get_random_code()))
                ex=Profile.objects.filter(slug=to_slug).exists()
        else:
            to_slug=str(self.user)
        self.slug=to_slug
        super().save(*args,**kwargs)
                
    
    '''
    
    TO do 
    
    1)Country
    2)Message 
    3)Group
    '''
    
    def __str__(self):
        return str(self.user.username)
    
    '''
    To create models-
    1)Friends 
    2)Group 
    3)Message 
    
    '''
    
choices=(
    ('send','send'),
    ('accept','accept')
    )   
#To show that the current user has received friend request
class RelationshipManager(models.Manager):
    def invite_receive(self,receiver):
        qs=Relationship.objects.filter(receiver=receiver,status='send')
        return qs   
    
class Relationship(models.Model):
    sender=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="sender")
    receiver=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="receiver")
    status=models.CharField(max_length=10,choices=choices)
    objects=RelationshipManager()
    
    def __str__(self):
        return f"Sender:{self.sender} - Receiver- {self.receiver}"

class Message(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True,related_name="user_me")
    sender=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True,related_name="from_user")
    recepient=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True,related_name="to_user")
    body=models.TextField(max_length=250)
    created=models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField(default=False)
    
    def __str__(self):
        return f"Sender:{self.sender} :Receiver{self.recepient} ID:{self.id}."
    
    def get_messages(user):
        users=[]  ##user__user means Message(user) calling Profile(user) Foreign key
        messages=Message.objects.filter(user__user=user).values('recepient').order_by('-created')
        for message in messages:
            users.append({
                'user':Profile.objects.get(pk=message['recepient']),
                
                
                })
        return users
    class Meta:
        ordering=['created',]
    
        
    
        
    
    