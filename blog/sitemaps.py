from django.contrib import sitemaps
from blog.models import Post
from django.utils import timezone    

class BlogSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.5
    
    def items(self):
        return Post.objects.filter(status=True, published_date__lte = timezone.now())
    