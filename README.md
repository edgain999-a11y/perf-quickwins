# Performance Quick Wins

This project demonstrates a fast, low-risk optimization pattern in a hot path.

## 10 performance improvements to consider

1. Replace repeated list membership checks with a `set`.
2. Cache expensive regex compilation and reuse compiled patterns.
3. Move repeated object construction out of loops.
4. Avoid O(n^2) nested scans by indexing once.
5. Batch DOM writes instead of touching the tree for each item.
6. Debounce high-frequency input handlers.
7. Lazy-load expensive assets and data until they are actually needed.
8. Reuse memoized derived values across renders.
9. Stream large responses instead of buffering everything in memory.
10. Use indexes or pre-sorted structures for common lookups.

## High-impact, low-effort win

The code in `src/report.py` converts the valid-label list to a set and converts each user's tag list to a set before filtering. This removes repeated linear scans from the hot path while keeping the logic readable and predictable.

## Validation

```bash
python3 -m unittest discover -s test -p 'test_*.py'
```
