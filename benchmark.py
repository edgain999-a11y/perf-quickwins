import time


def summarize_users_legacy(users, valid_labels):
    summaries = []
    for user in users:
        matching = [label for label in user.get('tags', []) if label in valid_labels]
        summaries.append(
            {
                'id': user['id'],
                'score': len(matching) + (10 if user.get('active', False) else 9),
                'matching_labels': matching,
            }
        )
    return summaries


def summarize_users(users, valid_labels):
    valid = set(valid_labels)
    summaries = []
    for user in users:
        user_labels = set(user.get('tags', []))
        matching = sorted(label for label in user_labels if label in valid)
        summaries.append(
            {
                'id': user['id'],
                'score': len(matching) + (10 if user.get('active', False) else 9),
                'matching_labels': matching,
            }
        )
    return summaries


users = [
    {'id': f'u{i}', 'active': i % 2 == 0, 'tags': [f'alpha{i % 8}', f'beta{i % 9}', f'gamma{i % 11}']}
    for i in range(5000)
]
labels = [f'alpha{i}' for i in range(25)] + [f'beta{i}' for i in range(25)]

start = time.perf_counter()
summarize_users_legacy(users, labels)
legacy_time = time.perf_counter() - start

start = time.perf_counter()
summarize_users(users, labels)
optimized_time = time.perf_counter() - start

print(f'legacy={legacy_time:.6f}s optimized={optimized_time:.6f}s improvement={legacy_time / optimized_time:.2f}x')
