MIN_LEN = 2
MAX_LEN_NICKNAME = 30
NICKNAME_ERROR_MESSAGE = f"Количество вводимых символов должно быть от {MIN_LEN} до {MAX_LEN_NICKNAME}"
TEXT_ERROR_MESSAGE = f"В этом поле должны быть только киррилические или латинские буквы и спецсимволы"

MIN_LEN_ABOUT = 50
MAX_LEN_ABOUT = 750
ABOUT_ERROR_MESSAGE = f"Количество вводимых символов должно быть от {MIN_LEN_ABOUT} до {MAX_LEN_ABOUT}"
MIN_LEN_PORTFOLIO = 5
MAX_LEN_PORTFOLIO = 256
PORTFOLIO_ERROR_MESSAGE = (
    f"Длина поля от {MIN_LEN_PORTFOLIO} до {MAX_LEN_PORTFOLIO}"
)
PHONE_ERROR_MESSAGE = (
    f"В этом поле должны быть только цифры и от 7 до 10 символов"
)
# TELEGRAM_ERROR_MESSAGE=(f'В этом поле должны быть только цифры и от 7 до 10 символов')
CONTACTS_ERROR_MESSAGE = (
    f"Длина поля от  {MIN_LEN_PORTFOLIO} до {MAX_LEN_PORTFOLIO}"
)
BOOL_CHOICES = [(True, "Готов"), (False, "Не готов")]
LEVEL_CHOICES = [(1, "junior"), (2, "middle"), (3, "senior"), (4, "lead")]
