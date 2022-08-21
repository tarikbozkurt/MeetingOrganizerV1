import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.

class Meeting(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='whoCreate')

    title = models.CharField(max_length=120,blank=True,null=True)
    subject = models.TextField(blank=True,null=True)

    meeting_date = models.DateField(blank=True,null=True)
    meeting_start_time = models.TimeField(blank=True,null=True)
    meeting_end_time = models.TimeField(blank=True,null=True)


    meeting_members = models.ManyToManyField(User,related_name='members',blank=True,null=True)



    meeting_created_date = models.DateTimeField(editable=False)
    meeting_modified_date = models.DateTimeField()
    draft = models.BooleanField()
    slug = models.SlugField(unique=True,max_length=150,editable=False,default = uuid.uuid1)
    meeting_image = models.ImageField(upload_to='media/meetings',blank=True)

    modified_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='Modified_By')


    def __str__(self):
        return self.title


    def get_slug(self):
        slug = slugify(self.title.replace('ı','i'))
        unique = slug
        number = 1

        while Meeting.objects.filter(slug = unique).exists():
            unique = '{}-{}'.format(slug,number)
            number += 1

        return unique

    def save(self,*args,**kwargs):
        if not self.id:
            self.meeting_created_date = timezone.now()

        self.meeting_modified_date = timezone.now()
        self.slug = self.get_slug()

        return super(Meeting,self).save(*args,**kwargs)


