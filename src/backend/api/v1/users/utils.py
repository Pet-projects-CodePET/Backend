from typing import Optional

from apps.users.models import User as UserType


def get_user_from_request(self) -> Optional[UserType]:
    """Функция получения объекта пользователя по данным из запроса."""

    serializer = self.get_serializer(data=self.request.data)
    serializer.is_valid(raise_exception=True)
    return serializer.get_user()
