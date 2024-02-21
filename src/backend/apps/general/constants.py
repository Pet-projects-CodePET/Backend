MAX_LENGTH_SKILL_NAME = 100
MAX_LENGTH_SPECIALIZATION_NAME = 100
LEVEL_CHOICES = [
    (1, "intern"),
    (2, "junior"),
    (3, "middle"),
    (4, "senior"),
    (5, "lead"),
]
TITLE_LENGTH = 100
DESCRIPRION_LENGTH = 250
MAX_LENGTH_EMAIL = 256
EMAIL_HELP_TEXT = (
    "Допускается локальная часть 2 - 192 символа, доменная часть 3 - 63 "
    "символа, только латинские буквы в нижнем регистре, цифры и символы "
    "@/./+/-/_"
)
EMAIL_ERROR_TEXT = "Не корректный email."
