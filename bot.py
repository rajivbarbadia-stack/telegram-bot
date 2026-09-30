import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.environ["BOT_TOKEN"]
ADMIN_ID = int(os.environ["ADMIN_ID"])


def home_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "💎 PREMIUM",
                callback_data="premium"
            )
        ],
        [
            InlineKeyboardButton(
                "🎬 DEMO",
                url="https://t.me/your_demo_channel"
            )
        ],
        [
            InlineKeyboardButton(
                "📖 INFO",
                url="https://t.me/your_info_channel"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = (
        "<b>🔥 WELCOME 🔥</b>\n\n"
        "Welcome to the bot.\n\n"
        "👇 Select an option below."
    )

    await update.message.reply_text(
        text=text,
        parse_mode="HTML",
        reply_markup=home_keyboard()
    )


async def premium_menu(query):

    keyboard = [
        [
            InlineKeyboardButton(
                "💎 PLAN 1",
                callback_data="plan_1"
            )
        ],
        [
            InlineKeyboardButton(
                "🔥 PLAN 2",
                callback_data="plan_2"
            )
        ],
        [
            InlineKeyboardButton(
                "📦 PLAN 3",
                callback_data="plan_3"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ BACK",
                callback_data="home"
            )
        ],
    ]

    await query.edit_message_text(
        text="<b>💎 SELECT YOUR PLAN 💎</b>",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def plan_page(query, plan_name):

    keyboard = [
        [
            InlineKeyboardButton(
                "👤 CONTACT ADMIN",
                url="https://t.me/your_username"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ BACK",
                callback_data="premium"
            )
        ],
    ]

    await query.edit_message_text(
        text=(
            f"<b>✅ {plan_name}</b>\n\n"
            "For access and further information, "
            "contact the administrator."
        ),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    data = query.data

    if data == "premium":
        await premium_menu(query)

    elif data == "home":

        await query.edit_message_text(
            text=(
                "<b>🔥 WELCOME 🔥</b>\n\n"
                "Welcome to the bot.\n\n"
                "👇 Select an option below."
            ),
            parse_mode="HTML",
            reply_markup=home_keyboard()
        )

    elif data == "plan_1":
        await plan_page(query, "PLAN 1")

    elif data == "plan_2":
        await plan_page(query, "PLAN 2")

    elif data == "plan_3":
        await plan_page(query, "PLAN 3")


async def stats(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if update.effective_user.id != ADMIN_ID:
        return

    await update.message.reply_text(
        "<b>📊 BOT STATUS</b>\n\n"
        "✅ Bot is online.",
        parse_mode="HTML"
    )


def main():

    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .build()
    )

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("stats", stats)
    )

    app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    print("Bot started successfully.")

    app.run_polling()


if __name__ == "__main__":
    main()
