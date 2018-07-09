from django.db import models

# Create your models here.
class NewsCategory(models.Model):
    name = models.CharField(max_length=100)


#aware time 清醒的时间（知道自己是哪个时区的）
#navie time 幼稚时间（不知道自己是哪个时区的时间）

class News(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    thumbnail = models.URLField()
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey('NewsCategory',on_delete=models.SET_NULL,null=True)
    author = models.ForeignKey('xfzauth.User',on_delete=models.SET_NULL,null=True)