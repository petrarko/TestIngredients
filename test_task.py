from unittest import TestCase

from task import parse_input, calculate_amount_to_clean


class Test(TestCase):
    def test_1(self):
        action_list = parse_input("3 2 \n"
                                  "1 1\n"
                                  "1 2\n"
                                  "2 1 2")
        self.assertEqual(calculate_amount_to_clean(action_list), 2)

    def test_2(self):
        action_list = parse_input("1 1 \n"
                                  "1 1\n")
        self.assertEqual(calculate_amount_to_clean(action_list), 1)

    def test_3(self):
        action_list = parse_input("4 4\n"
                                  "1 1\n"
                                  "1 2\n"
                                  "1 3\n"
                                  "1 4\n"
                                  )
        self.assertEqual(calculate_amount_to_clean(action_list), 4)

    def test_4(self):
        action_list = parse_input("4 4\n"
                                  "2 1 2\n"
                                  "1 2\n"
                                  "2 1 3\n"
                                  "1 4\n"
                                  )
        self.assertEqual(calculate_amount_to_clean(action_list), 3)

    def test_5(self):
        action_list = parse_input("4 4\n"
                                  "2 2\n"
                                  "1 1 2\n"
                                  "2 1 3\n"
                                  "1 4\n"
                                  )
        self.assertEqual(calculate_amount_to_clean(action_list), 3)
