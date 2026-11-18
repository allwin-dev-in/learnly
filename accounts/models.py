from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail

from django.contrib.auth.models import AbstractUser

import os
from dotenv import load_dotenv

load_dotenv()

# Create your models here.

class User(AbstractUser):
    phone=models.PositiveBigIntegerField(null=False,unique=True)
    ROLE_CHOICES=(
        ("Student","Student"),
        ("Trainer","Trainer"),
        ("Admin","Admin")
    )
    role=models.CharField(max_length=20,choices=ROLE_CHOICES,null=False)



class TrainerProfile(models.Model):
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    qualification=models.CharField(max_length=200,null=True)
    linkedin_url=models.URLField(null=True)
    user_id=models.OneToOneField(User,on_delete=models.CASCADE)

class StudentProfile(models.Model):
    skills = models.CharField(max_length=200,null=True)
    qualification = models.CharField(max_length=200,null=True)
    passoutyear = models.CharField(max_length=20,null=True)
    githuburl = models.URLField(null=True)
    linkedurl = models.URLField(null=True)
    user_id=models.OneToOneField(User,on_delete=models.CASCADE)


def create_profile(sender,instance,created,*args,**kwargs):
    if created and instance.role=="Trainer":
        TrainerProfile.objects.create(user_id=instance)
    elif created and instance.role=="Student":
        StudentProfile.objects.create(user_id=instance)

post_save.connect(create_profile,sender=User)

def send_account_creation_mail(sender,instance,created,*args,**kwargs):
    if created and instance.role in ("Student","Trainer"):
        send_mail(
            "Account Creation Confirmation.",
            f"""Dear {instance.username},\n\t You have sucessfulyy created account in Learnly Application.\n
            your account details are ...\n
            Username :{instance.username}\n
            Email :{instance.email}\n
            Phone :{instance.phone}\n
            Account Type : {instance.role}\n""",
            {os.getenv("EMAIL_HOST_USER")},
            [instance.email]
        )

post_save.connect(send_account_creation_mail,sender=User)


