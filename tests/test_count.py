from unittest import TestCase
from Day2 import count


class Test(TestCase):
    def test_count_zeros(self):
        assert count.count([0, 0, 0], 0) == 3

    def test_count_string(self):
        assert count.count(["a", "a", "a"], "a") == 3
