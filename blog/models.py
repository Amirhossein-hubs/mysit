from django.db import models
from django.contrib.auth.models import User          #?

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)              #on_delete=models.CASCADE = با حذف شدن یوزر پوست های یوزر هم حذف بشه                                   #on_delete=models.SET_NULL = بعد حذف یوزر اون رو خالی کنه
    title = models.CharField(max_length=255)
    content = models.TextField()
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True) #blank= True #null = جیگاه خالی میتونه باشه
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_date']
        # verbose_name = 'پوست'
        # verbose_name_plural = 'پوست ها'                                #اسم تیبل رو تغییر میده
    def __str__(self):
        return f"{self.title} _ id={self.id}"
    


