import telebot


#telebot.apihelper.proxy = {'https':'socks5://swcbbabh:aYEbh6q5gQ@178.32.218.16:3306'}
token = "526438480:AAFGQw3uv-2sC2rojii41wwBHXG-8fz9nsk"
bot = telebot.TeleBot(token)
bot_about = """
Я - бот ЗПШ. Я помогу тебе узнать расписание, список курсов и другую информацию о школе.
Сайт школы - zpsh.ru
"""
admins = [218952152]
pupils = set()

@bot.message_handler(commands=['start', 'info'])
def info(msg):
    print('new user', msg.from_user.id)
    pupils.add(msg.from_user.id)
    bot.reply_to(msg, str(bot_about))

@bot.message_handler()
def send_info(msg):
    if msg.from_user.id in admins and 'notify_everybody' in msg.text:
        for pupil in pupils:
            bot.send_message(pupil, msg.text[16:])
bot.polling()
