import telebot
from telebot import types
import feedparser

token = '7284726306:AAHHNV3tKFNvM3FrCh7xq3PLoR-22EXG8FY'  # توکن رباتتو اینجا بگذار
bot = telebot.TeleBot(token)

# لینک‌های RSS منابع خبری

# Tech News English
google_tech = "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"
BBC_tech = "https://feeds.bbci.co.uk/news/technology/rss.xml"
TechNewsWorld_tech = "https://www.technewsworld.com/rss-feed"
NewYork_tech = "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"

# Tech News Persian
Zoomit_tech = "https://www.zoomit.ir/feed/"
Digiato_tech = "https://digiato.com/topic/tech/feed"
Technolife_tech = "https://www.technolife.com/blog/category/news/feed/"

# Sport News English
BBC_sport = "https://feeds.bbci.co.uk/sport/football/rss.xml"
CNN_sport = "http://rss.cnn.com/rss/edition_sport.rss"
sky_sport = "https://www.skysports.com/rss/12040"

# Sport News Persian
Varzesh3 = "https://www.varzesh3.com/rss"
KhabarVarzeshi_sport = "https://www.khabarvarzeshi.com/rss"
Isna_sport = "https://www.isna.ir/rss/tp/24"

# ساخت دکمه‌های صفحه اصلی با ReplyKeyboardMarkup
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("تکنولوژی 🖥️")
btn2 = types.KeyboardButton("ورزشی 🥇")
markup.add(btn1, btn2)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     """خیلی ممنون که ما رو انتخاب کردی🙌😁
می‌تونی خبرهایی که می‌خوای دنبال کنی رو این زیر انتخاب کنی:""",
                     reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "تکنولوژی 🖥️":
        glass_markup = types.InlineKeyboardMarkup()
        gls1 = types.InlineKeyboardButton("فارسی", callback_data="persian_tech")
        gls2 = types.InlineKeyboardButton("خارجی", callback_data="english_tech")
        back = types.InlineKeyboardButton("بازگشت", callback_data="back")
        glass_markup.add(gls1, gls2)
        glass_markup.add(back)
        bot.send_message(message.chat.id,
                         """چه خوب! پس تو هم علاقه به تکنولوژی داری😍
حالا خبرهای تکنولوژی رو از منابع فارسی می‌خوایی یا خارجی؟""",
                         reply_markup=glass_markup)

    elif message.text == "ورزشی 🥇":
        sport_markup = types.InlineKeyboardMarkup()
        sp1 = types.InlineKeyboardButton("فارسی", callback_data="persian_sport")
        sp2 = types.InlineKeyboardButton("خارجی", callback_data="english_sport")
        back = types.InlineKeyboardButton("بازگشت", callback_data="back")
        sport_markup.add(sp1, sp2)
        sport_markup.add(back)
        bot.send_message(message.chat.id,
                         """عالی! خبرهای ورزشی رو از منابع فارسی می‌خوایی یا خارجی؟""",
                         reply_markup=sport_markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    bot.answer_callback_query(call.id)

    # منوی انتخاب منابع تکنولوژی فارسی
    if call.data == "persian_tech":
        gls_markup = types.InlineKeyboardMarkup()
        gls1 = types.InlineKeyboardButton("زومیت", callback_data="zoomit")
        gls2 = types.InlineKeyboardButton("دیجیاتو", callback_data="digiato")
        gls3 = types.InlineKeyboardButton("تکنولایف", callback_data="technolife")
        back = types.InlineKeyboardButton("بازگشت", callback_data="back")
        gls_markup.add(gls1, gls2, gls3)
        gls_markup.add(back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="ما از این منابع فارسی استفاده می‌کنیم لطفا یکی رو انتخاب کن:",
                              reply_markup=gls_markup)

    # منوی انتخاب منابع تکنولوژی انگلیسی
    elif call.data == "english_tech":
        gls_markup = types.InlineKeyboardMarkup()
        gls1 = types.InlineKeyboardButton("Google", callback_data="google_tech")
        gls2 = types.InlineKeyboardButton("BBC", callback_data="bbc_tech")
        gls3 = types.InlineKeyboardButton("NewYork Times", callback_data="newyork_tech")
        gls4 = types.InlineKeyboardButton("TechNewsWorld", callback_data="technewsworld_tech")
        back = types.InlineKeyboardButton("بازگشت", callback_data="back")
        gls_markup.add(gls1, gls2)
        gls_markup.add(gls3, gls4)
        gls_markup.add(back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="ما از این منابع خارجی استفاده می‌کنیم لطفا یکی رو انتخاب کن:",
                              reply_markup=gls_markup)

    # منوی انتخاب منابع ورزشی فارسی
    elif call.data == "persian_sport":
        sp_markup = types.InlineKeyboardMarkup()
        sp1 = types.InlineKeyboardButton("ورزش ۳", callback_data="varzesh3")
        sp2 = types.InlineKeyboardButton("خبر ورزشی", callback_data="khabarvarzeshi")
        sp3 = types.InlineKeyboardButton("ایسنا", callback_data="isna")
        back = types.InlineKeyboardButton("بازگشت", callback_data="back")
        sp_markup.add(sp1, sp2, sp3)
        sp_markup.add(back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="ما از این منابع ورزشی فارسی استفاده می‌کنیم لطفا یکی رو انتخاب کن:",
                              reply_markup=sp_markup)

    # منوی انتخاب منابع ورزشی انگلیسی
    elif call.data == "english_sport":
        sp_markup = types.InlineKeyboardMarkup()
        sp1 = types.InlineKeyboardButton("BBC Sport", callback_data="bbc_sport")
        sp2 = types.InlineKeyboardButton("CNN", callback_data="cnn_sport")
        sp3 = types.InlineKeyboardButton("sky Sports", callback_data="sky_sport")
        back = types.InlineKeyboardButton("بازگشت", callback_data="back")
        sp_markup.add(sp1, sp2, sp3)
        sp_markup.add(back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="ما از این منابع ورزشی خارجی استفاده می‌کنیم لطفا یکی رو انتخاب کن:",
                              reply_markup=sp_markup)

    # بازگشت به منوی اصلی
    elif call.data == "back":
        text = """خبرهایی که می‌خوای دنبال کنی رو انتخاب کن:"""
        bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=markup)

    # بازگشت به منوی منابع فارسی تکنولوژی
    elif call.data == "back_to_persian_tech":
        gls_markup = types.InlineKeyboardMarkup()
        gls1 = types.InlineKeyboardButton("زومیت", callback_data="zoomit")
        gls2 = types.InlineKeyboardButton("دیجیاتو", callback_data="digiato")
        gls3 = types.InlineKeyboardButton("تکنولایف", callback_data="technolife")
        back = types.InlineKeyboardButton("بازگشت", callback_data="back")
        gls_markup.add(gls1, gls2, gls3)
        gls_markup.add(back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="ما از این منابع فارسی استفاده می‌کنیم لطفا یکی رو انتخاب کن:",
                              reply_markup=gls_markup)

    # بازگشت به منوی منابع انگلیسی تکنولوژی
    elif call.data == "back_to_english_tech":
        gls_markup = types.InlineKeyboardMarkup()
        gls1 = types.InlineKeyboardButton("Google", callback_data="google_tech")
        gls2 = types.InlineKeyboardButton("BBC", callback_data="bbc_tech")
        gls3 = types.InlineKeyboardButton("NewYork Times", callback_data="newyork_tech")
        gls4 = types.InlineKeyboardButton("TechNewsWorld", callback_data="technewsworld_tech")
        back = types.InlineKeyboardButton("بازگشت", callback_data="back")
        gls_markup.add(gls1, gls2)
        gls_markup.add(gls3, gls4)
        gls_markup.add(back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="ما از این منابع خارجی استفاده می‌کنیم لطفا یکی رو انتخاب کن:",
                              reply_markup=gls_markup)

    # بازگشت به منوی منابع فارسی ورزشی
    elif call.data == "back_to_persian_sport":
        sp_markup = types.InlineKeyboardMarkup()
        sp1 = types.InlineKeyboardButton("ورزش ۳", callback_data="varzesh3")
        sp2 = types.InlineKeyboardButton("خبر ورزشی", callback_data="khabarvarzeshi")
        sp3 = types.InlineKeyboardButton("ایسنا", callback_data="isna")
        back = types.InlineKeyboardButton("بازگشت", callback_data="back")
        sp_markup.add(sp1, sp2, sp3)
        sp_markup.add(back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="ما از این منابع ورزشی فارسی استفاده می‌کنیم لطفا یکی رو انتخاب کن:",
                              reply_markup=sp_markup)

    # بازگشت به منوی منابع انگلیسی ورزشی
    elif call.data == "back_to_english_sport":
        sp_markup = types.InlineKeyboardMarkup()
        sp1 = types.InlineKeyboardButton("BBC Sport", callback_data="bbc_sport")
        sp2 = types.InlineKeyboardButton("CNN", callback_data="cnn_sport")
        sp3 = types.InlineKeyboardButton("sky Sports", callback_data="sky_sport")
        back = types.InlineKeyboardButton("بازگشت", callback_data="back")
        sp_markup.add(sp1, sp2, sp3)
        sp_markup.add(back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="ما از این منابع ورزشی خارجی استفاده می‌کنیم لطفا یکی رو انتخاب کن:",
                              reply_markup=sp_markup)

    # نمایش خبرها همراه با دکمه بازگشت به منوی قبلی
    elif call.data == "zoomit":
        send_feed(call, Zoomit_tech, back_to="back_to_persian_tech")

    elif call.data == "digiato":
        send_feed(call, Digiato_tech, back_to="back_to_persian_tech")

    elif call.data == "technolife":
        send_feed(call, Technolife_tech, back_to="back_to_persian_tech")

    elif call.data == "google_tech":
        send_feed(call, google_tech, back_to="back_to_english_tech")

    elif call.data == "bbc_tech":
        send_feed(call, BBC_tech, back_to="back_to_english_tech")

    elif call.data == "newyork_tech":
        send_feed(call, NewYork_tech, back_to="back_to_english_tech")

    elif call.data == "technewsworld_tech":
        send_feed(call, TechNewsWorld_tech, back_to="back_to_english_tech")

    elif call.data == "varzesh3":
        send_feed(call, Varzesh3, back_to="back_to_persian_sport")

    elif call.data == "khabarvarzeshi":
        send_feed(call, KhabarVarzeshi_sport, back_to="back_to_persian_sport")

    elif call.data == "isna":
        send_feed(call, Isna_sport, back_to="back_to_persian_sport")

    elif call.data == "bbc_sport":
        send_feed(call, BBC_sport, back_to="back_to_english_sport")

    elif call.data == "cnn_sport":
        send_feed(call, CNN_sport, back_to="back_to_english_sport")

    elif call.data == "sky_sport":
        send_feed(call, sky_sport, back_to="back_to_english_sport")


def send_feed(call, rss_url, back_to):
    try:
        feed = feedparser.parse(rss_url)
        try:
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        except:
            pass

        text = f"📡 <b>آخرین خبرها از {feed.feed.title}</b>\n\n"
        for entry in feed.entries[:5]:
            text += f"📰 <b>{entry.title}</b>\n"
            text += f"🔗 <a href='{entry.link}'>لینک خبر</a>\n"
            text += "➖➖➖➖➖➖➖\n"

        back_markup = types.InlineKeyboardMarkup()
        back_button = types.InlineKeyboardButton("بازگشت", callback_data=back_to)
        back_markup.add(back_button)

        bot.send_message(chat_id=call.message.chat.id,
                         text=text,
                         parse_mode="HTML",
                         disable_web_page_preview=True,
                         reply_markup=back_markup)
    except Exception as e:
        bot.send_message(chat_id=call.message.chat.id, text=f"خطا در دریافت خبرها: {e}")
        bot.send_message(chat_id=call.message.chat.id,text="به پشتیبانی گزارش دهید. لینک پشتیبانی در بیو هست.")


bot.infinity_polling()
