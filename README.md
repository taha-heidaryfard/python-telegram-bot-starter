# 🤖 Python Telegram Bot Starter (2026 Edition)

<p align="center">
  <a href="README.fa.md">🇮🇷 راهنمای فارسی</a> •
  <a href="README.md">🌐 English Guide</a>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python"></a>
  <a href="https://github.com/python-telegram-bot/python-telegram-bot"><img src="https://img.shields.io/badge/python--telegram--bot-v21%2B-2CA5E0?logo=telegram&logoColor=white" alt="Library"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
</p>

A clean, modern, and production-ready starter template for building Telegram bots with Python using `python-telegram-bot` (v20+) native asynchronous architecture (`async/await`).

---

## 🚀 Key Features

- ⚡ **100% Async / Await Architecture**: Built on modern `python-telegram-bot` v20+ with zero blocking I/O.
- 🔘 **Interactive Inline Keyboards**: Example buttons with callbacks (`CallbackQueryHandler`) and URL buttons.
- 🔐 **Secure Configuration**: Uses `python-dotenv` to safely keep tokens in `.env` without exposing them in git.
- 🛡️ **Centralized Error Handling**: Logs unhandled exceptions gracefully without crashing the bot process.
- 🧹 **Clean Start**: Configured with `drop_pending_updates=True` to ignore outdated flood messages on launch.

---

## 🛠️ Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/taha-heidaryfard/python-telegram-bot-starter.git
cd python-telegram-bot-starter
```

### 2. Create and activate a Virtual Environment
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

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Open `.env` and replace `TELEGRAM_BOT_TOKEN` with the API token obtained from [@BotFather](https://t.me/BotFather):
```env
TELEGRAM_BOT_TOKEN=123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ
```

### 5. Run the bot
```bash
python bot.py
```

Now open Telegram, send `/start` to your bot, and test the interactive inline menu!

---

## 📂 Project Structure

```text
python-telegram-bot-starter/
├── bot.py              # Main bot entry point and async handlers
├── requirements.txt    # Python package dependencies
├── .env.example        # Template for environment secrets
├── .gitignore          # Git exclusion rules
├── LICENSE             # MIT License
├── README.md           # English Documentation
└── README.fa.md        # Persian Documentation (راهنمای فارسی)
```

---

## 📖 Complete Tutorial

For an in-depth breakdown of how this bot works, check out the full step-by-step tutorial:
- 🌐 **English Guide:** [Building a Telegram Bot with Python: 2026 Guide](https://taha-heidaryfard.ir/en/blog/python/telegram-bot)
- 🇮🇷 **مقاله فارسی:** [آموزش ساخت ربات تلگرام با پایتون در سال ۲۰۲۶](https://taha-heidaryfard.ir/blog/python/telegram-bot)

---

## 👨‍💻 Author

**Mohammad Taha Heidaryfard**
- 🌐 Website: [taha-heidaryfard.ir](https://taha-heidaryfard.ir/en)
- 📂 Projects: [taha-heidaryfard.ir/projects](https://taha-heidaryfard.ir/en/projects)
- 🐙 GitHub: [@taha-heidaryfard](https://github.com/taha-heidaryfard)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
