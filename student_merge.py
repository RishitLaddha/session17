# student_merge.py

"""
Module: student_merge.py
Description:
    This module provides two functions to merge multiple word frequency dictionaries.
    Each input dictionary contains words as keys and their frequency counts as values.
    The functions combine the counts from all dictionaries and return a single merged dictionary.
    The merged dictionary is sorted by frequency (in descending order) and by word (alphabetically ascending for ties).

Functions:
    merge_with_defaultdict(*dicts):
        - Merges dictionaries using collections.defaultdict.
    merge_with_counter(*dicts):
        - Merges dictionaries using collections.Counter.
"""

from collections import defaultdict, Counter

def merge_with_defaultdict(*dicts):
    """
    Merges multiple word frequency dictionaries using collections.defaultdict.
    
    Parameters:
        *dicts: Any number of dictionaries. Each dictionary's keys are words and values are frequencies.
    
    Returns:
        dict: A merged dictionary where the frequencies are summed up.
              The dictionary is sorted by frequency (descending) and then by word (alphabetically for ties).
    
    Example:
        >>> d1 = {'python': 10, 'java': 3}
        >>> d2 = {'python': 5, 'c++': 2}
        >>> merge_with_defaultdict(d1, d2)
        {'python': 15, 'java': 3, 'c++': 2}
    """
    # Create a defaultdict with default int value (0) for each key.
    merged = defaultdict(int)
    # Iterate over each dictionary.
    for d in dicts:
        for word, count in d.items():
            merged[word] += count  # Add the count for the word.
    
    # Sort the merged dictionary:
    # - First, sort by frequency in descending order (using -item[1])
    # - Then, sort alphabetically by word (using item[0]) for ties.
    sorted_items = sorted(merged.items(), key=lambda item: (-item[1], item[0]))
    return dict(sorted_items)

def merge_with_counter(*dicts):
    """
    Merges multiple word frequency dictionaries using collections.Counter.
    
    Parameters:
        *dicts: Any number of dictionaries. Each dictionary's keys are words and values are frequencies.
    
    Returns:
        dict: A merged dictionary where the frequencies are summed.
              The dictionary is sorted by frequency (descending) and then by word (alphabetically for ties).
    
    Example:
        >>> d1 = {'python': 10, 'java': 3}
        >>> d2 = {'python': 5, 'c++': 2}
        >>> merge_with_counter(d1, d2)
        {'python': 15, 'java': 3, 'c++': 2}
    """
    # Create an empty Counter.
    merged = Counter()
    # Manually update the Counter with each dictionary's counts.
    for d in dicts:
        for word, count in d.items():
            merged[word] += count  # This handles negative counts correctly.
    
    # Sort the merged dictionary in the same way:
    # - By frequency (descending) and by word (alphabetically) for ties.
    sorted_items = sorted(merged.items(), key=lambda item: (-item[1], item[0]))
    return dict(sorted_items)
