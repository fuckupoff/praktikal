import random
import telebot



bot = telebot.TeleBot('7902473274:AAHknkD97QtQz7Rc-v3FAGfpwtnZ7MxGaKA')

# Список всех карт Clash Royale
CARDS = [
    "Гигант", "Пека", "Ведьма", "Принц", "Дракончик", "Метка", "Огненный дух",
    "Лук", "Шар", "Валькирия", "Рыцарь", "Мушкетёр", "Мини-ПЕККА", "Мега-рыцарь",
    "Принцесса", "Ледяной дух", "Скелеты", "Гоблинский бочонок", "Огненный шар"
]

# Популярные мета-колоды
META_DECKS = {
    "Гигант + Ведьма": ["Гигант", "Ведьма", "Мушкетёр", "Огненный шар", "Валькирия", "Лук", "Гоблинский бочонок",
                        "Ледяной дух"],
    "Мега-рыцарь + Принцесса": ["Мега-рыцарь", "Принцесса", "Мини-ПЕККА", "Шар", "Метка", "Скелеты", "Огненный дух",
                                "Гоблинский бочонок"],
    "Пека + Дракончик": ["Пека", "Дракончик", "Принц", "Огненный шар", "Рыцарь", "Лук", "Ледяной дух", "Метка"]
}


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('🎲 Случайная колода', '🏆 Топовые колоды')
    markup.add('🔍 Колода по карте', '🏟️ Колода под арену')

    bot.send_message(
        message.chat.id,
        "🎮 Привет! Я бот для создания колод в Clash Royale.\nВыбери действие:",
        reply_markup=markup
    )


# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == '🎲 Случайная колода':
        deck = random.sample(CARDS, 8)
        bot.send_message(message.chat.id, "🔮 Случайная колода:\n\n" + "\n".join(f"▪️ {card}" for card in deck))

    elif message.text == '🏆 Топовые колоды':
        response = "🏆 Топовые колоды:\n\n"
        for name, deck in META_DECKS.items():
            response += f"🔹 {name}:\n" + "\n".join(f"▪️ {card}" for card in deck) + "\n\n"
        bot.send_message(message.chat.id, response)

    elif message.text == '🔍 Колода по карте':
        msg = bot.send_message(message.chat.id, "Введите название карты (например, Гигант):")
        bot.register_next_step_handler(msg, process_card_request)

    elif message.text == '🏟️ Колода под арену':
        msg = bot.send_message(message.chat.id, "Введите номер арены (от 1 до 16):")
        bot.register_next_step_handler(msg, process_arena_request)

    else:
        bot.send_message(message.chat.id, "Используйте кнопки для взаимодействия с ботом")


def process_card_request(message):
    card = message.text.strip()
    if card not in CARDS:
        bot.send_message(message.chat.id, "❌ Такой карты нет в базе. Попробуйте ещё раз.")
        return

    other_cards = [c for c in CARDS if c != card]
    deck = [card] + random.sample(other_cards, 7)
    bot.send_message(message.chat.id, f"🃏 Колода с картой {card}:\n\n" + "\n".join(f"▪️ {c}" for c in deck))


def process_arena_request(message):
    try:
        arena = int(message.text)
        if 1 <= arena <= 16:
            deck = random.sample(CARDS, 8)
            bot.send_message(message.chat.id,
                             f"🏟️ Колода для арены {arena}:\n\n" + "\n".join(f"▪️ {card}" for card in deck))
        else:
            bot.send_message(message.chat.id, "❌ Арена должна быть от 1 до 16.")
    except ValueError:
        bot.send_message(message.chat.id, "❌ Пожалуйста, введите число от 1 до 16.")


# Запуск бота
print("Бот запущен...")
bot.infinity_polling()