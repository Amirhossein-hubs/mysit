import os
import django
import sqlite3

# تنظیمات محیط جنگو برای دسترسی به دیتابیس
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings') # نام پوشه تنظیمات شما اینجاست
django.setup()

from django.conf import settings

# مسیر فایل دیتابیس SQLite
db_path = settings.DATABASES['default']['NAME']

def run_sql():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # لیست migrationهایی که باید به صورت دستی اضافه شوند
    # فرمت: (app_name, migration_name)
    migrations_to_fake = [
        ('contenttypes', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0001_initial'),
        ('admin', '0001_initial'),
        ('admin', '0002_logentry_remove_auto_add'),
        # سایر migrationهایی که قبلا با خطای 'already exists' مواجه شدید را اینجا اضافه کنید
    ]
    
    for app, name in migrations_to_fake:
        try:
            cursor.execute("INSERT INTO django_migrations (app, name, applied) VALUES (?, ?, DATETIME('now'))", (app, name))
            print(f"Added: {app}.{name}")
        except sqlite3.OperationalError as e:
            print(f"Skipped {app}.{name} (Maybe already exists): {e}")

    # حذف رکورد مشکل‌ساز از دیتابیس (اگر هنوز وجود دارد)
    try:
        cursor.execute("DELETE FROM django_admin_log WHERE user_id = 1")
        print("Deleted problematic rows from django_admin_log")
    except Exception as e:
        print(f"Error cleaning django_admin_log: {e}")

    conn.commit()
    conn.close()
    print("Done! Now try 'python manage.py migrate' again.")

if __name__ == "__main__":
    run_sql()
