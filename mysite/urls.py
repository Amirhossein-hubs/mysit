from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemaps
from blog.sitemaps import BlogSitemap
import debug_toolbar
sitemaps = {
    'static':StaticViewSitemaps,
    'blog':BlogSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('website.urls')),
    path('accounts/', include('accounts.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('robots.urls')),
    path('__debug__/', include(debug_toolbar.urls)), 
    path('captcha/', include('captcha.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_roo = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = 'mysite.views.custom_page_not_found_view'