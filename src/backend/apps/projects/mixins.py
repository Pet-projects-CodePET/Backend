class RecruitmentStatusMixin:
    def calculate_recruitment_status(self, obj):
        """Метод определения статуса набора в проект."""

        if any(
            specialist.is_required
            for specialist in obj.project_specialists.all()
        ):
            return "Набор открыт"
        return "Набор закрыт"
