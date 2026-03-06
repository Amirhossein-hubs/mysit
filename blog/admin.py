from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'                                                         #با تنظیم این المان به شما یک شاخص زمان از سال و ماه‌های مرتبط با المان‌های ایجاد شده را نمایش خواهد داد.
    empty_value_display = '-empty-'                                                         #مقدار نمایش پیش‌فرض زمینه‌های خالی رکورد (هیچ‌کدام، رشته خالی و غیره) را لغو می‌کند. مقدار پیش‌فرض - (یک خط تیره) است.
    list_display = ('id', 'title', 'author', 'status', 'counted_views', 'published_date')                   #نمایش فیلد هایی از آیتم هایی که می خواهیم نمایش داده شوند
    list_filter = ('status',)                                                               #قابلیت فیلترکردن داده‌ها و نمایش را در صفحات ادمین مرتبط با مدل به ما می‌دهد
    #ordering = ['created_date']                                                             #مرتب کردن هر پست براساس تاریخ ایجاد شده 
    search_fields = ['title', 'content']                                                    #به شما اجازه جست‌وجو و فیلترکردن المان‌ها بر اساس فیلد نوشتاری را می‌دهد که در متون مختلف آن را بررسی می‌کند.
admin.site.register(Post, PostAdmin)
