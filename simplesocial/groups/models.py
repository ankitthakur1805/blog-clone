from django.db import models
from django.utils.text import slugify
# Create your models here.
import mistune 

from django.contrib.auth import get_user_model
User = get_user_model()
from django.urls import reverse

from django import template
register = template.Library()

class Group(models.Model):

    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description =models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

   
    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = mistune.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug":self.slug})


class GroupMember(models.Model):
    group= models.ForeignKey(Group, related_name='membership', on_delete=models.CASCADE)
    user= models.ForeignKey(User,related_name='user_groups', on_delete=models.CASCADE)    

    class Meta:
        unique_together = ('group','user')

    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse("GroupMember_detail", kwargs={"pk": self.pk})
