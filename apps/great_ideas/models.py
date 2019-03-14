from django.db import models
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2 or not postData['first_name'].isalpha():
            errors["first_name"] = "First name must be at least 2 characters, and use only alphabetical characters."
        if len(postData['last_name']) < 2 or not postData['last_name'].isalpha():
            errors["last_name"] = "Last name must be at least 2 characters, and use only alphabetical characters."
        if EMAIL_REGEX.match(postData['email']) == None:
            errors['email_fmt'] = "Email must be in valid format."
        emails_query = self.filter(email = postData['email'])
        if len(emails_query) > 0:
            errors["email"] = "User with that email already exists"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if postData['password']!= postData['pw_confirm']:
            errors['pw_conf'] = "Password and Confirm PW must match"
        return errors
    def log_validator(self, postData):
        user = User.objects.filter(email = postData['log_email'])
        errors = {}
        if not user:
            errors['email'] = "Enter a valid email."
        if len(postData['log_password']) == 0:
            errors['pw_enter'] = "Please enter your password."
        if user and not bcrypt.checkpw(postData['log_password'].encode(), user[0].password.encode()):
            errors['password'] = "Invalid password."
        return errors
    def validator(self, postData):
        errors = {}
        if len(postData['content']) < 10:
            errors['content'] = "Idea must be at least 10 characters."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Idea(models.Model):
    content = models.TextField(max_length = 700 )
    posted = models.ForeignKey(User, related_name = "posted_by")
    likes = models.ManyToManyField(User, related_name = "liked_ideas")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()