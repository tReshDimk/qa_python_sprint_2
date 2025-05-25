from miles import HobbitsPriorityStatus


class TestHobbitsPriorityStatus:

    def test_add_miles_and_check_status(self):
        hobbit = 'Голлум'
        hobbits_priority = HobbitsPriorityStatus()
        hobbits_priority.add_new_hobbit(hobbit)
        hobbits_priority.add_miles_to_hobbit(hobbit, 50)
        assert hobbits_priority.hobbits_miles[hobbit] == 50
        assert hobbits_priority.get_status(hobbit) == 'Classic'
