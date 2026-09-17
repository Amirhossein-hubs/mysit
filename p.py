import os
import django
import sys

# تنظیمات Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings') # اسم پروژه شما ممکنه متفاوت باشه
django.setup()

from django.db import connection

cursor = connection.cursor()

# حذف رکوردهای مربوط به contenttypes از جدول django_migrations
try:
    cursor.execute("DELETE FROM django_migrations WHERE app = 'contenttypes';")
    print("Records for 'contenttypes' deleted from django_migrations.")
except Exception as e:
    print(f"Error deleting from django_migrations: {e}")

# حذف جدول django_content_type اگر وجود دارد (با احتیاط استفاده شود)
# اگر از اجرای دستور قبل مطمئن نیستید، این قسمت را کامنت کنید
try:
    cursor.execute("DROP TABLE IF EXISTS django_content_type;")
    print("Table 'django_content_type' dropped if it existed.")
except Exception as e:
    print(f"Error dropping table django_content_type: {e}")

connection.commit()
cursor.close()
