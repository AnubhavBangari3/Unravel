from django.db import models
from Profile.models import Profile

# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="profile_posts")
    text=models.TextField()
    image=models.ImageField(upload_to="Profile/Posts",blank=True,null=True)
    video=models.FileField(upload_to="Profile/Video",blank=True,null=True)
    like=models.ManyToManyField(Profile,blank=True,related_name="like")
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Post by {self.author}"
    
    class Meta:
        ordering=['-created']



class Liked(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="user_liked",blank=True,null=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="post_liked")
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} liked the post of  {self.post}"
    
cat=(
    ('Programming','Programming'),
    ('Sports','Sports'),
    ('Entertainment','Entertainment'),
    ('Health','Health'),
    ('Fitness','Fitness'),
    ('Meditation','Meditation'),
    ('Music','Music'),
)

class JoinGroup(models.Model):
    name=models.CharField(max_length=255)
    category=models.CharField(max_length=200,choices=cat)
    owner=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='owner')
    members=models.ManyToManyField(Profile,blank=True)
    description=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return str(self.name)
    
class PostGroup(models.Model):
    group_post=models.ForeignKey(JoinGroup,on_delete=models.CASCADE,related_name='group_post')
    posted_by=models.ForeignKey(Profile, on_delete=models.CASCADE,related_name="posted_by")
    group_text=models.TextField(blank=True,null=True)
    group_image=models.ImageField(upload_to="Group/Posts",blank=True,null=True)
    likegp=models.ManyToManyField(Profile,blank=True,related_name="likegp")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.id} ->{self.group_post}->By {self.posted_by}"
    
    class Meta:
        ordering = ('-created',)
reward=(
    ('pawn',10),
    ('knight',20),
    ('bishop',30),
    ('rook',35),
    ('queen',80),
    ('king',100)
)
class Rewards(models.Model):
    group_post=models.ForeignKey(PostGroup,on_delete=models.CASCADE,related_name='group_post_r')
    person=models.ForeignKey(Profile, on_delete=models.CASCADE,related_name="person")
    reward=models.CharField(max_length=200,choices=reward)
    
    def __str__(self):
        return f"{self.person} gave {self.reward} reward"
    class Meta:
        verbose_name="Rewards"
        
class LikedGroupPost(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="user_likedgrouppost",blank=True,null=True)
    postgroup=models.ForeignKey(PostGroup,on_delete=models.CASCADE,related_name="grouppost_liked")
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} liked the post of  {self.postgroup}"
    
class CommentOnPost(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="commnet_user_profile")
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comment_post")
    body=models.TextField()
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} commented on {self.post}"
    class Meta:
        ordering = ('-created',)
    
class CommentOnGroupPost(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="commnet_guser_profile")
    post=models.ForeignKey(PostGroup,on_delete=models.CASCADE,related_name="comment_gpost")
    body=models.TextField()
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} commented on {self.post}"
    
    class Meta:
        ordering = ('-created',)
        
class GroupChat(models.Model):
    group_chat=models.ForeignKey(JoinGroup,on_delete=models.CASCADE,related_name="group_chat")
    sender=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="sender_message")
    message_body=models.CharField(max_length=250)
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.sender} {self.message_body}"
        

    