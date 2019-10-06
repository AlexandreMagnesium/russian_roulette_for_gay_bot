import telebot
import random

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Срать хочу, давай швидше.')
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('Перший постріл')
    bot.send_message(message.from_user.id, 'Вставляємо в револьвер патрон. Розкручуємо барабан ...', reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def rus_roulette(message):

	if message.text == 'Перший постріл':
		var=random.randint(1,6)
		if var == 1:
			user_markup = telebot.types.ReplyKeyboardMarkup()
			user_markup.row('Розпочати заново')
			bot.send_message(message.from_user.id, '̶̶̶Ї̶б̶а̶т̶ь̶ ̶т̶и̶ ̶л̶о̶х̶)̶)̶')
			bot.send_message(message.from_user.id, 'Ти помер, розпочни заново.', reply_markup=user_markup)
		else:
			user_markup = telebot.types.ReplyKeyboardMarkup()
			user_markup.row('Другий постріл')
			bot.send_message(message.from_user.id, '*Клац..*', reply_markup=user_markup)

	elif message.text == 'Другий постріл':
		var=random.randint(1,5)
		if var == 1:
			user_markup = telebot.types.ReplyKeyboardMarkup()
			user_markup.row('Розпочати заново')
			bot.send_message(message.from_user.id, 'Ти помер, розпочни заново.', reply_markup=user_markup)
		else:
			user_markup = telebot.types.ReplyKeyboardMarkup()
			user_markup.row('Третій постріл')
			bot.send_message(message.from_user.id, '*Клац..*', reply_markup=user_markup)

	elif message.text == 'Третій постріл':
		var=random.randint(1,4)
		if var == 1:
			user_markup = telebot.types.ReplyKeyboardMarkup()
			user_markup.row('Розпочати заново')
			bot.send_message(message.from_user.id, 'Ти помер, розпочни заново.', reply_markup=user_markup)
		else:
			user_markup = telebot.types.ReplyKeyboardMarkup()
			user_markup.row('Четвертий постріл')
			bot.send_message(message.from_user.id, '*Клац..*', reply_markup=user_markup)

	elif message.text == 'Четвертий постріл':
		var=random.randint(1,3)
		if var == 1:
			user_markup = telebot.types.ReplyKeyboardMarkup()
			user_markup.row('Розпочати заново')
			bot.send_message(message.from_user.id, 'Ти помер, розпочни заново.', reply_markup=user_markup)
		else:
			user_markup = telebot.types.ReplyKeyboardMarkup()
			user_markup.row("П'ятий постріл")
			bot.send_message(message.from_user.id, '*Клац..*', reply_markup=user_markup)

	elif message.text == "П'ятий постріл":
		var=random.randint(1,2)
		if var == 1:
			user_markup = telebot.types.ReplyKeyboardMarkup()
			user_markup.row('Розпочати заново')
			bot.send_message(message.from_user.id, 'Ти помер, розпочни заново.', reply_markup=user_markup)
		else:
			user_markup = telebot.types.ReplyKeyboardMarkup()
			user_markup.row('Шостий постріл')
			user_markup.row('Розкрутити барабан заново.')
			bot.send_message(message.from_user.id, '*Клац..*', reply_markup=user_markup)

	elif message.text == "Шостий постріл":
		user_markup = telebot.types.ReplyKeyboardMarkup()
		user_markup.row('Розпочати заново')
		bot.send_message(message.from_user.id, '̶О̶й̶,̶ ̶д̶у̶р̶а̶к̶.̶.')
		bot.send_message(message.from_user.id, 'Ти помер, розпочни заново.', reply_markup=user_markup)

	elif message.text == 'Розкрутити барабан заново.' :
		user_markup = telebot.types.ReplyKeyboardMarkup()
		user_markup.row('Перший постріл')
		bot.send_message(message.from_user.id, 'Розкручуємо барабан ..', reply_markup=user_markup)

	elif message.text == 'Розпочати заново' :
		user_markup = telebot.types.ReplyKeyboardMarkup()
		user_markup.row('Перший постріл')
		bot.send_message(message.from_user.id, 'Вставляємо в револьвер патрон. Розкручуємо барабан ...', reply_markup=user_markup)

	else :
		bot.send_message(message.from_user.id, '̶Т̶и̶,̶ ̶б̶л̶я̶т̶ь̶,̶ ̶т̶у̶п̶и̶й̶ ̶?̶?̶?̶')
		bot.send_message(message.from_user.id, 'Вибач, але я тебе не розумію.')


@bot.message_handler(content_types=['document','audio','photo','voice','video','sticker','venue','file','location','contact'])
def for_idiots(message):
    bot.send_message(message.chat.id, "Вибач, але я тебе не розумію.")


bot.polling()