from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# تنظیمات اولیه برای کروم
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # باز کردن کروم در حالت تمام صفحه
# chrome_options.add_argument("--headless")  # اگر نمی‌خوای پنجره مرورگر رو ببینی

# مسیر درایور (با webdriver_manager به صورت خودکار مدیریت میشه)
service = Service(ChromeDriverManager().install())

# ایجاد درایور
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # باز کردن صفحه اول گوگل
    driver.get("https://www.google.com")
    
    # کمی صبر کن تا صفحه کامل لود بشه
    time.sleep(2)
    
    # حالا می‌تونیم المان‌های مختلف رو پیدا کنیم
    # چند مثال:
    
    # 1. پیدا کردن با name
    search_box = driver.find_element(By.NAME, "q")
    print("صفحه گوگل باز شد و باکس جستجو پیدا شد!")
    
    # 2. پیدا کردن با CSS Selector
    logo = driver.find_element(By.CSS_SELECTOR, "img.lnXdpd")
    print("لوگوی گوگل پیدا شد!")
    
    # 3. پیدا کردن با XPath
    # gmail_link = driver.find_element(By.XPATH, "//a[text()='Gmail']")
    # print("لینک Gmail پیدا شد!")
    
    # 4. اگر می‌خوای متن یک المان رو بخونی
    search_box_text = search_box.get_attribute("placeholder")
    print(f"متن placeholder باکس جستجو: {search_box_text}")
    
    # 5. اگر می‌خوای HTML کامل یک المان رو ببینی
    # element_html = search_box.get_attribute("outerHTML")
    # print(f"HTML المان: {element_html}")
    
    # 6. پیدا کردن با کلاس
    # elements_by_class = driver.find_elements(By.CLASS_NAME, "gb_f")
    # print(f"{len(elements_by_class)} المان با این کلاس پیدا شد")
    
except Exception as e:
    print(f"خطا رخ داد: {e}")

finally:
    # بستن مرورگر بعد از 5 ثانیه
    time.sleep(5)
    driver.quit()
    print("مرورگر بسته شد!")


