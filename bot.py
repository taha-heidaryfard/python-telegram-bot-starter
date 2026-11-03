"""
Python Telegram Bot Starter (2026 Edition)
Author: Mohammad Taha Heidaryfard (https://taha-heidaryfard.ir)
License: MIT
"""

import logging
import os
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# Load configuration from .env file
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


# /start command handler
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the /start command."""
    user = update.effective_user
    welcome_text = (
        f"سلام {user.first_name} عزیز! 👋\n\n"
        "به ربات پایتونی نمونه خوش آمدید.\n"
        "از دکمه‌های شیشه‌ای زیر برای آزمایش امکانات استفاده کنید:"
    )

    # Inline Keyboard Buttons
    keyboard = [
        [
            InlineKeyboardButton("🌐 وب‌سایت من", url="https://taha-heidaryfard.ir"),
            InlineKeyboardButton("📂 نمونه‌کارها", url="https://taha-heidaryfard.ir/projects"),
        ],
        [
            InlineKeyboardButton("⚡ وضعیت سرور", callback_data="status_check"),
            InlineKeyboardButton("ℹ️ درباره ربات", callback_data="about_bot"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        text=welcome_text,
        reply_markup=reply_markup,
    )


# /help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the /help command."""
    help_text = (
        "📖 **راهنمای دستورات ربات:**\n\n"
        "• `/start` — راه‌اندازی و باز کردن منوی اصلی\n"
        "• `/help` — مشاهده راهنما\n"
        "• ارسال هر پیام متنی ساده برای دریافت اکو از سرور"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")


# Inline callback query handler
async def button_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Processes inline keyboard button clicks."""
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "status_check":
        await query.edit_message_text(
            text="✅ **وضعیت سرور:** ربات به صورت کاملاً غیرهمگام (Async)، آنلاین و آماده به کار است.",
            parse_mode="Markdown",
        )
    elif data == "about_bot":
        await query.edit_message_text(
            text=(
                "🤖 **درباره پروژه:**\n"
                "یک الگوی استاندارد، مدرن و ماژولار برای ساخت ربات‌های تلگرام با پایتون ۳ و کتابخانه python-telegram-bot v20+.\n\n"
                "👨‍💻 توسعه‌دهنده: محمد طاها حیدری‌فرد\n"
                "🌐 وب‌سایت: https://taha-heidaryfard.ir"
            ),
            parse_mode="Markdown",
        )


# Echo text message handler
async def echo_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echoes user text messages."""
    received = update.message.text
    response = f"پیام شما دریافت شد: «{received}»"
    await update.message.reply_text(response)


# Centralized error handler
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Logs unhandled exceptions."""
    logger.error("خطای سیستمی:", exc_info=context.error)


def main() -> None:
    """Initializes and runs the bot."""
    if not BOT_TOKEN:
        raise ValueError("خطا: مقدار TELEGRAM_BOT_TOKEN در فایل .env تنظیم نشده است!")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button_callback_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_message_handler))

    # Error handling
    app.add_error_handler(error_handler)

    print("🚀 ربات با موفقیت فعال شد. در حال دریافت پیام‌ها...")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
