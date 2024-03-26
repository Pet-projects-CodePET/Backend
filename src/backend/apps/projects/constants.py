MAX_LENGTH_DESCRIPTION = 750
MIN_LENGTH_DESCRIPTION = 50
LENGTH_DESCRIPTION_ERROR_TEXT = (
    f"Длина поля от {MIN_LENGTH_DESCRIPTION} до {MAX_LENGTH_DESCRIPTION} "
    "символов."
)

MAX_LENGTH_PROJECT_NAME = 100
MIN_LENGTH_PROJECT_NAME = 5
LENGTH_PROJECT_NAME_ERROR_TEXT = (
    f"Длина поля от {MIN_LENGTH_PROJECT_NAME} до {MAX_LENGTH_PROJECT_NAME} "
    "символов."
)
REGEX_PROJECT_NAME = r"(^[+/:,.0-9A-Za-zА-Яа-яЁё\-–—]+)\Z"
REGEX_PROJECT_NAME_ERROR_TEXT = (
    "Название проекта может содержать: кириллические и латинские символы, "
    "цифры и символы .,-—+/:"
)

MAX_LENGTH_DIRECTION_NAME = 20
MIN_LENGTH_DIRECTION_NAME = 2
LENGTH_DIRECTION_NAME_ERROR_TEXT = (
    f"Длина поля от {MIN_LENGTH_PROJECT_NAME} до {MAX_LENGTH_PROJECT_NAME} "
    "символов."
)
REGEX_DIRECTION_NAME = r"(^[A-Za-zА-Яа-яЁё]+)\Z"
REGEX_DIRECTION_NAME_ERROR_TEXT = (
    "Направление разработки может содержать: кириллические и латинские "
    "символы."
)

MAX_LENGTH_LINK = 256
MIN_LENGTH_LINK = 5
LENGTH_LINK_ERROR_TEXT = (
    f"Длина поля от {MIN_LENGTH_LINK} до {MAX_LENGTH_LINK} символов."
)

BUSYNESS_CHOICES = (
    (1, 10),
    (2, 20),
    (3, 30),
    (4, 40),
)
STATUS_CHOICES = (
    (1, "Активен"),
    (2, "Завершен"),
    (3, "Черновик"),
)


PROJECTS_PER_PAGE = 10
