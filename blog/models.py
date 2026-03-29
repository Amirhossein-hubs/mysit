from django.db import models
from django.contrib.auth.models import User          #?
from django.urls import reverse
from taggit.managers import  TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)                   #	هر آیتم یک نویسنده دارد، هر نویسنده می‌تواند چند آیتم داشته باشد     یک به چند      #on_delete=models.CASCADE = با حذف شدن یوزر پوست های یوزر هم حذف بشه                                   #on_delete=models.SET_NULL = بعد حذف یوزر اون رو خالی کنه
    category = models.ManyToManyField(Category)                                             #   آیتم‌ها و دسته‌ها می‌توانند با هم در ارتباط چندگانه باشند            چند به چند
    title = models.CharField(max_length=255)
    content = models.TextField()
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True) #blank= True #null = جیگاه خالی میتونه باشه
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to= 'blog/', default='blog/default.jpg')
    address_github = models.URLField(max_length=200, blank=True)
    tags = TaggableManager()
    
    class Meta:
        ordering = ['-created_date']
        # verbose_name = 'پوست'
        # verbose_name_plural = 'پوست ها'                                #اسم تیبل رو تغییر میده
    def __str__(self):
        return f"{self.title} _ id={self.id}"



    def snippets(self):
        return self.content[:100] + '...'

    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid':self.id})
    

    


    


