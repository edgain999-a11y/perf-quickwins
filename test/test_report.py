import unittest

from src.report import summarize_users


class SummarizeUsersTest(unittest.TestCase):
    def test_avoids_repeated_linear_membership_checks(self):
        users = [
            {'id': 'u1', 'active': True, 'tags': ['beta', 'ops']},
            {'id': 'u2', 'active': False, 'tags': ['alpha', 'beta']},
            {'id': 'u3', 'active': True, 'tags': []},
        ]

        result = summarize_users(users, ['alpha', 'beta'])

        self.assertEqual(
            result,
            [
                {'id': 'u1', 'score': 11, 'matching_labels': ['beta']},
                {'id': 'u2', 'score': 11, 'matching_labels': ['alpha', 'beta']},
                {'id': 'u3', 'score': 10, 'matching_labels': []},
            ],
        )


if __name__ == '__main__':
    unittest.main()
