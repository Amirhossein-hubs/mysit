from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'                                                         #با تنظیم این المان به شما یک شاخص زمان از سال و ماه‌های مرتبط با المان‌های ایجاد شده را نمایش خواهد داد.
    empty_value_display = '-empty-'                                                         #مقدار نمایش پیش‌فرض زمینه‌های خالی رکورد (هیچ‌کدام، رشته خالی و غیره) را لغو می‌کند. مقدار پیش‌فرض - (یک خط تیره) است.
    list_display = ('id', 'title', 'author', 'status', 'login_require', 'counted_views', 'published_date')                   #نمایش فیلد هایی از آیتم هایی که می خواهیم نمایش داده شوند
    list_filter = ('status',)                                                               #قابلیت فیلترکردن داده‌ها و نمایش را در صفحات ادمین مرتبط با مدل به ما می‌دهد
    #ordering = ['created_date']                                                             #مرتب کردن هر پست براساس تاریخ ایجاد شده 
    search_fields = ['title', 'content']                                                    #به شما اجازه جست‌وجو و فیلترکردن المان‌ها بر اساس فیلد نوشتاری را می‌دهد که در متون مختلف آن را بررسی می‌کند.
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'approved', 'created_date')
    date_hierarchy = 'created_date'                                                         #با تنظیم این المان به شما یک شاخص زمان از سال و ماه‌های مرتبط با المان‌های ایجاد شده را نمایش خواهد داد.
    empty_value_display = '-empty-'                                                         #مقدار نمایش پیش‌فرض زمینه‌های خالی رکورد (هیچ‌کدام، رشته خالی و غیره) را لغو می‌کند. مقدار پیش‌فرض - (یک خط تیره) است.
    list_filter = ('approved',)                                                               #قابلیت فیلترکردن داده‌ها و نمایش را در صفحات ادمین مرتبط با مدل به ما می‌دهد
    search_fields = ['name', 'emeil']                                                    #به شما اجازه جست‌وجو و فیلترکردن المان‌ها بر اساس فیلد نوشتاری را می‌دهد که در متون مختلف آن را بررسی می‌کند.
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)



