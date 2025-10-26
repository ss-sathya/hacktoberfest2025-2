def can_transform(s, t, k):
    total_moves = 0
    for cs, ct in zip(s, t):
        if ct < cs:
            return "NO"
        total_moves += ord(ct) - ord(cs)
        if total_moves > k:
            return "NO"
    return "YES"
