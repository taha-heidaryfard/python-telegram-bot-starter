# 🤖 استارتر ربات تلگرام با پایتون (نسخه ۲۰۲۶)

<p align="center">
  <a href="README.fa.md">🇮🇷 راهنمای فارسی</a> •
  <a href="README.md">🌐 English Guide</a>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/پایتون-۳.۱۰%2B-blue?logo=python&logoColor=white" alt="پایتون"></a>
  <a href="https://github.com/python-telegram-bot/python-telegram-bot"><img src="https://img.shields.io/badge/کتابخانه-python--telegram--bot-2CA5E0?logo=telegram&logoColor=white" alt="کتابخانه"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/مجوز-MIT-green.svg" alt="مجوز"></a>
</p>

یک قالب آماده، استاندارد، ماژولار و پروداکشن برای ساخت ربات‌های تلگرام در پایتون با استفاده از معماری نوین و غیرهمگام (**Async/Await**) فریم‌ورک `python-telegram-bot` (نسخه ۲۰ به بالا).

---

## 🚀 ویژگی‌های کلیدی

- ⚡ **معماری ۱۰۰٪ غیرهمگام (Async/Await)**: توسعه داده‌شده با فریم‌ورک مدرن `python-telegram-bot v20+` بدون مسدود کردن تردها و منابع سیستم.
- 🔘 **دکمه‌های شیشه‌ای تعاملی (Inline Keyboard)**: نمونه دکمه‌های شیشه‌ای با کال‌بک (`CallbackQueryHandler`) و دکمه‌های لینک‌دار.
- 🔐 **مدیریت امن متغیرهای حساس**: استفاده از `python-dotenv` جهت ذخیره امن توکن در فایل `.env` و جلوگیری از نشت اطلاعات در گیت.
- 🛡️ **مدیریت مرکزی و یکپارچه خطاها**: ثبت و لاگ کردن خطاهای پیش‌بینی‌نشده بدون توقف یا کرش کردن ربات.
- 🧹 **شروع تمیز (Clean Start)**: تنظیم شده با `drop_pending_updates=True` برای نادیده‌گرفتن پیام‌های قدیمی انباشته‌شده در زمان خاموشی سرور.

---

## 🛠️ راهنمای سریع راه‌اندازی و اجرا

### ۱. کلون کردن مخزن
```bash
git clone https://github.com/taha-heidaryfard/python-telegram-bot-starter.git
cd python-telegram-bot-starter
```

### ۲. ساخت و فعال‌سازی محیط مجازی (Virtual Environment)
- **ویندوز**:
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```
- **لینوکس / مک**:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### ۳. نصب وابستگی‌ها و پکیج‌ها
```bash
pip install -r requirements.txt
```

### ۴. پیکربندی توکن ربات
یک کپی از فایل `.env.example` بسازید و نام آن را به `.env` تغییر دهید:
```bash
cp .env.example .env
```
فایل `.env` را باز کرده و توکن اختصاصی دریافتی از [@BotFather](https://t.me/BotFather) را در آن قرار دهید:
```env
TELEGRAM_BOT_TOKEN=123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ
```

### ۵. اجرای ربات
```bash
python bot.py
```

اکنون وارد تلگرام شوید، به ربات خود پیام `/start` بدهید و منوی شیشه‌ای و دکمه‌های تعاملی را تست کنید!

---

## 📂 ساختار فایل‌های پروژه

```text
python-telegram-bot-starter/
├── bot.py              # نقطه ورود و کدهای اصلی ربات و هندلرهای async
├── requirements.txt    # پکیج‌ها و وابستگی‌های پایتون
├── .env.example        # الگوی متغیرهای محیطی برای کلیدها
├── .gitignore          # قوانین نادیده‌گیری فایل‌های محرمانه در گیت
├── LICENSE             # مجوز متن‌باز MIT
├── README.md           # مستندات انگلیسی
└── README.fa.md        # مستندات کامل فارسی
```

---

## 📖 آموزش کامل و گام‌به‌گام

برای مطالعه توضیحات عمیق و خط‌به‌خط ساخت این ربات، به مقاله وبلاگ مراجعه کنید:
- 🇮🇷 **مقاله فارسی:** [آموزش ساخت ربات تلگرام با پایتون در سال ۲۰۲۶](https://taha-heidaryfard.ir/blog/python/telegram-bot)
- 🌐 **English Guide:** [Building a Telegram Bot with Python: 2026 Guide](https://taha-heidaryfard.ir/en/blog/python/telegram-bot)

---

## 👨‍💻 توسعه‌دهنده

**محمد طاها حیدری‌فرد (Mohammad Taha Heidaryfard)**
- 🌐 وب‌سایت شخصی: [taha-heidaryfard.ir](https://taha-heidaryfard.ir)
- 📂 پروژه‌ها و نمونه‌کارها: [taha-heidaryfard.ir/projects](https://taha-heidaryfard.ir/projects)
- 🐙 گیت‌هاب: [@taha-heidaryfard](https://github.com/taha-heidaryfard)

---

## 📄 مجوز انتشار (License)

این پروژه تحت مجوز متن‌باز [MIT License](LICENSE) منتشر شده است.
