from django.db import models
# from django.contrib.auth.models import User
from account.models import CustomUser

# Create your models here.
# author's profile 
class AuthourProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) # AuthourProfile is connected to the built-in User model using a ForeignKey relationship, allowing us to associate each author profile with a specific user account.
    profile_picture = models.ImageField(upload_to='authors/')
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class BlogPostCategory(models.Model):
    name = models.CharField(max_length=10, unique=True) 
    description = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

import uuid   # 32-character hexadecimal string that is unique across all space and time, making it an ideal choice for primary keys in a database, especially in distributed systems where multiple instances of the application may be generating new records simultaneously.
# e.g. 550e8400-e29b-41d4-a716-446655440000

class BlogPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # using UUID as the primary key for the BlogPost model, which provides a unique identifier for each blog post and enhances security by making it harder to guess the IDs of other posts.
    # id = models.BigAutoField(primary_key=True) # using BigAutoField as the primary key for the BlogPost model, which automatically increments the ID for each new blog post and allows for a larger range of IDs compared to the default AutoField.

    category = models.ForeignKey(BlogPostCategory, on_delete=models.CASCADE)   

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    body = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE)  # to connect a blog post to an authenticated user
    author = models.ForeignKey(AuthourProfile, on_delete=models.CASCADE, blank=True, null=True)  # using the author profile instead of the user model directly, to get data related to the author like profile picture and bio

    created_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Blog Title: {self.title}'
    
