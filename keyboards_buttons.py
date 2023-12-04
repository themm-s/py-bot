from aiogram import types

buttonWeb = [
    types.InlineKeyboardButton(text="Мобильная разработка", callback_data="web_mobile"),
    types.InlineKeyboardButton(text="Сайты/Веб-Приложения", callback_data="web_web"),
    types.InlineKeyboardButton(text="Десктопные приложения", callback_data="web_desktop"),
    types.InlineKeyboardButton(text="Игры", callback_data="web_games")
]

buttonOOP = [
    types.InlineKeyboardButton(text="Да", callback_data="OOP_yes"),
    types.InlineKeyboardButton(text="Нет", callback_data="OOP_no"),
]

buttonPerformance = [
    types.InlineKeyboardButton(text="1", callback_data="performance_1"),
    types.InlineKeyboardButton(text="2", callback_data="performance_2"),
    types.InlineKeyboardButton(text="3", callback_data="performance_3"),
]

buttonSecurity = [
    types.InlineKeyboardButton(text="1", callback_data="security_1"),
    types.InlineKeyboardButton(text="2", callback_data="security_2"),
    types.InlineKeyboardButton(text="3", callback_data="security_3"),
]

buttonEntryLevel = [
    types.InlineKeyboardButton(text="Низкий", callback_data="entry_level_low"),
    types.InlineKeyboardButton(text="Высокий", callback_data="entry_level_high"),
]

buttonDevSpeed = [
    types.InlineKeyboardButton(text="1", callback_data="development_speed_1"),
    types.InlineKeyboardButton(text="2", callback_data="development_speed_2"),
    types.InlineKeyboardButton(text="3", callback_data="development_speed_3"),
]

buttonCrossPlatform = [
    types.InlineKeyboardButton(text="Да", callback_data="cross_platform_yes"),
    types.InlineKeyboardButton(text="Нет", callback_data="cross_platform_no"),
]

buttonFrameworks = [
    types.InlineKeyboardButton(text="1", callback_data="frameworks_1"),
    types.InlineKeyboardButton(text="2", callback_data="frameworks_2"),
    types.InlineKeyboardButton(text="3", callback_data="frameworks_3"),
]

buttonPart = [
    types.InlineKeyboardButton(text="Серверная", callback_data="select_part_server"),
    types.InlineKeyboardButton(text="Клиентская", callback_data="select_part_client"),
]


# {
#   0: "mobile",
#   1: "yes",
#   2: "1",
#   3: "1",
#   4: "low",
#   5: "1",
#   6: "yes",
#   7: "server",
# }