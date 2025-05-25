import pytest

from miles import HobbitsPriorityStatus


hobbits_priority_statuses: list[list[str]] = [
    ['Фродо', 'Platinum'],
    ['Сэм', 'Gold'],
    ['Мэри', 'Silver'],
    ['Пиппин', 'Silver'],
]


class TestHobbitsPriorityStatus:
    @pytest.mark.parametrize(
            'hobbit, priority_status',
            hobbits_priority_statuses
        )
    def test_priority_status(self, hobbit: str, priority_status: str):
        assert HobbitsPriorityStatus().get_status(hobbit) == priority_status
