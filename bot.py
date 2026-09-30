import os

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)


# ==================================================
#                 RAILWAY VARIABLES
# ==================================================

TOKEN = os.environ["BOT_TOKEN"]
ADMIN_ID = int(os.environ["ADMIN_ID"])


# ==================================================
#                    MAIN IMAGES
# ==================================================

START_IMAGE = "https://postimg.cc/Bj5kbwsQ"
PREMIUM_IMAGE = "https://postimg.cc/Sn41B78F"


# ==================================================
#                     QR IMAGES
# ==================================================

QR_1 = "https://postimg.cc/K1mQqcSY"
QR_2 = "https://postimg.cc/N5cxFG0G"
QR_3 = "https://postimg.cc/s1ppkFJC"
QR_4 = "https://postimg.cc/bSTSsh6G"


# ==================================================
#                      LINKS
# ==================================================

DEMO_CHANNEL = "https://t.me/predemogroupp"
INFO_CHANNEL = "https://t.me/howtogetpre"
ADMIN_USERNAME = "https://t.me/mms744"


# ==================================================
#                   HOME BUTTONS
# ==================================================

def home_buttons():

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
                url=DEMO_CHANNEL
            )
        ],

        [
            InlineKeyboardButton(
                "📖 INFO",
                url=INFO_CHANNEL
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)


# ==================================================
#                       START
# ==================================================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    caption = (
        "<b>🔥 WELCOME 🔥</b>\n\n"
        "Welcome to the bot.\n\n"
        "👇 Select an option below."
    )

    await update.message.reply_photo(
        photo=START_IMAGE,
        caption=caption,
        parse_mode="HTML",
        reply_markup=home_buttons()
    )


# ==================================================
#                  PREMIUM MENU
# ==================================================

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
                "👑 PLAN 4",
                callback_data="plan_4"
            )
        ],

        [
            InlineKeyboardButton(
                "⬅️ BACK",
                callback_data="home"
            )
        ]

    ]

    await query.message.edit_media(

        media=InputMediaPhoto(
            media=PREMIUM_IMAGE,
            caption="<b>💎 SELECT YOUR PLAN 💎</b>",
            parse_mode="HTML"
        ),

        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ==================================================
#                     QR PAGE
# ==================================================

async def qr_page(query, qr_image, plan_name):

    keyboard = [

        [
            InlineKeyboardButton(
                "👤 CONTACT ADMIN",
                url=ADMIN_USERNAME
            )
        ],

        [
            InlineKeyboardButton(
                "⬅️ BACK",
                callback_data="premium"
            )
        ]

    ]

    await query.message.edit_media(

        media=InputMediaPhoto(
            media=qr_image,
            caption=(
                f"<b>✅ {plan_name}</b>\n\n"
                "Please contact the administrator "
                "for further information."
            ),
            parse_mode="HTML"
        ),

        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ==================================================
#                    HOME PAGE
# ==================================================

async def home_page(query):

    caption = (
        "<b>🔥 WELCOME 🔥</b>\n\n"
        "Welcome to the bot.\n\n"
        "👇 Select an option below."
    )

    await query.message.edit_media(

        media=InputMediaPhoto(
            media=START_IMAGE,
            caption=caption,
            parse_mode="HTML"
        ),

        reply_markup=home_buttons()
    )


# ==================================================
#                  BUTTON HANDLER
# ==================================================

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

        await home_page(query)


    elif data == "plan_1":

        await qr_page(
            query,
            QR_1,
            "PLAN 1"
        )


    elif data == "plan_2":

        await qr_page(
            query,
            QR_2,
            "PLAN 2"
        )


    elif data == "plan_3":

        await qr_page(
            query,
            QR_3,
            "PLAN 3"
        )


    elif data == "plan_4":

        await qr_page(
            query,
            QR_4,
            "PLAN 4"
        )


# ==================================================
#                     ADMIN STATS
# ==================================================

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


# ==================================================
#                       MAIN
# ==================================================

def main():

    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .build()
    )


    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    app.add_handler(
        CommandHandler(
            "stats",
            stats
        )
    )


    app.add_handler(
        CallbackQueryHandler(
            button_handler
        )
    )


    print("Bot started successfully.")


    app.run_polling()


# ==================================================
#                       RUN
# ==================================================

if __name__ == "__main__":
    main()
