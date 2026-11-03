# 🤖 Python Telegram Bot Starter (2026 Edition)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Library](https://img.shields.io/badge/python--telegram--bot-v21%2B-2CA5E0?logo=telegram&logoColor=white)](https://github.com/python-telegram-bot/python-telegram-bot)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A clean, modern, and production-ready starter template for building Telegram bots with Python using `python-telegram-bot` (v20+) native asynchronous architecture (`async/await`).

قالب آماده، استاندارد و مدرن برای ساخت ربات‌های تلگرام با پایتون و معماری غیرهمگام (Async).

---

## 🚀 Key Features / ویژگی‌های کلیدی

- ⚡ **100% Async / Await Architecture**: Built on modern `python-telegram-bot` v20+ with zero blocking I/O.
- 🔘 **Interactive Inline Keyboards**: Example buttons with callbacks (`CallbackQueryHandler`) and URL buttons.
- 🔐 **Secure Configuration**: Uses `python-dotenv` to safely keep tokens in `.env` without exposing them in git.
- 🛡️ **Centralized Error Handling**: Logs unhandled exceptions gracefully without crashing the bot process.
- 🧹 **Clean Start**: Configured with `drop_pending_updates=True` to ignore outdated flood messages on launch.

---

## 🛠️ Quick Start / راهنمای راه‌اندازی

### 1. Clone the repository / کلون کردن پروژه
```bash
git clone https://github.com/taha-heidaryfard/python-telegram-bot-starter.git
cd python-telegram-bot-starter
```

### 2. Create and activate a Virtual Environment / ساخت محیط مجازی
- **Windows**:
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```
- **macOS / Linux**:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Install dependencies / نصب وابستگی‌ها
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables / تنظیم توکن
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Open `.env` and replace `TELEGRAM_BOT_TOKEN` with the API token obtained from [@BotFather](https://t.me/BotFather):
```env
TELEGRAM_BOT_TOKEN=123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ
```

### 5. Run the bot / اجرای ربات
```bash
python bot.py
```

Now open Telegram, send `/start` to your bot, and test the interactive inline menu!

---

## 📂 Project Structure / ساختار فایل‌ها

```text
python-telegram-bot-starter/
├── bot.py              # Main bot entry point and async handlers
├── requirements.txt    # Python package dependencies
├── .env.example        # Template for environment secrets
├── .gitignore          # Git exclusion rules
├── LICENSE             # MIT License
└── README.md           # Documentation
```

---

## 📖 Complete Tutorial / آموزش کامل

For an in-depth breakdown of how this bot works, check out the full step-by-step tutorial:
- 🇮🇷 **مقاله فارسی:** [آموزش ساخت ربات تلگرام با پایتون در سال ۲۰۲۶](https://taha-heidaryfard.ir/blog/python/telegram-bot)
- 🌐 **English Guide:** [Building a Telegram Bot with Python: 2026 Guide](https://taha-heidaryfard.ir/en/blog/python/telegram-bot)

---

## 👨‍💻 Author / توسعه‌دهنده

**Mohammad Taha Heidaryfard (محمد طاها حیدری‌فرد)**
- 🌐 Website: [taha-heidaryfard.ir](https://taha-heidaryfard.ir)
- 📂 Projects: [taha-heidaryfard.ir/projects](https://taha-heidaryfard.ir/projects)
- 🐙 GitHub: [@taha-heidaryfard](https://github.com/taha-heidaryfard)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
