import requests

phone_number = input("لطفاً شماره تلفن خود را وارد کنید: ")

# ارسال درخواست GET به صفحه ثبت نام برای گرفتن اطلاعات ضروری
response = requests.get("https://asangem.com/register/")
csrf_token = ""  

# دریافت مقدار توکن CSRF از صفحه
if response.status_code == 200:
    csrf_token = response.cookies["csrftoken"]
else:
    print("مشکلی در دریافت اطلاعات وجود دارد. لطفاً مجدداً تلاش کنید.")

# ارسال شماره تلفن و CSRF توکن به صفحه ثبت نام
response = requests.post(
    "https://asangem.com/register/",
    headers={"X-CSRFToken": csrf_token},
    data={"phone_number": phone_number}
)

# بررسی وضعیت پاسخ دریافتی
if response.status_code == 200:
    print("درخواست با موفقیت انجام شد و کد تایید به شماره تلفن شما ارسال شد.")
else:
    print("مشکلی در ارسال درخواست وجود دارد. لطفاً مجدداً تلاش کنید.")
