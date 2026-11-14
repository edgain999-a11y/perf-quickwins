from __future__ import annotations


def summarize_users(users, valid_labels=None):
    valid_labels = set(valid_labels or [])
    summaries = []

    for user in users:
        user_labels = set(user.get('tags', []))
        matching = sorted(label for label in user_labels if label in valid_labels)
        score = len(matching) + (10 if user.get('active', False) else 9)
        summaries.append(
            {
                'id': user['id'],
                'score': score,
                'matching_labels': matching,
            }
        )

    return summaries
