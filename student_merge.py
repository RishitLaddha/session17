from collections import defaultdict, Counter

def merge_with_defaultdict(*dicts):
    merged = defaultdict(int)
    for d in dicts:
        for word, count in d.items():
            merged[word] += count
    # Bonus: sort by frequency descending; for ties, sort alphabetically ascending
    sorted_items = sorted(merged.items(), key=lambda item: (-item[1], item[0]))
    return dict(sorted_items)

def merge_with_counter(*dicts):
    merged = Counter()
    for d in dicts:
        for word, count in d.items():
            merged[word] += count
    # Bonus: sort by frequency descending; for ties, sort alphabetically ascending
    sorted_items = sorted(merged.items(), key=lambda item: (-item[1], item[0]))
    return dict(sorted_items)
