[![Python Tests](https://github.com/RishitLaddha/session17/actions/workflows/python-tests.yml/badge.svg)](https://github.com/RishitLaddha/session17/actions/workflows/python-tests.yml) 

<img width="1225" alt="Screenshot 2025-02-18 at 20 38 50" src="https://github.com/user-attachments/assets/67c5715f-da80-48d5-9680-a4310b2d933e" />

# Dictionary Validation and Merging Word Frequencies Project

Welcome to the **Dictionary Validation and Merging Word Frequencies** project. This repository contains two separate Python modules that solve two common tasks often encountered in software development, particularly when handling JSON data and processing text data. In this project, you will find:

1. **student_code.py** – A module that validates the structure of a nested dictionary against a given template. This is crucial when you need to ensure that the data received from external sources (like APIs) conforms to an expected format before further processing.
2. **student_merge.py** – A module that merges multiple word frequency dictionaries into a single dictionary. It provides two implementations: one using `collections.defaultdict` and another using `collections.Counter`. This kind of merging is common when aggregating data from multiple sources.

Both modules include thorough documentation, detailed inline comments, and example usage. Additionally, there are automated tests configured using GitHub Actions to ensure that any changes continue to work as expected.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Module 1: student_code.py](#module-1-student_codepy)
  - [Assignment Description](#assignment-description)
  - [Functionality Overview](#functionality-overview)
  - [Implementation Details](#implementation-details)
  - [Example Usage](#example-usage)
- [Module 2: student_merge.py](#module-2-student_mergepy)
  - [Assignment Description](#assignment-description-1)
  - [Functionality Overview](#functionality-overview-1)
  - [Implementation Details](#implementation-details-1)
  - [Example Usage](#example-usage-1)
- [Testing and GitHub Actions Workflow](#testing-and-github-actions-workflow)
- [Conclusion](#conclusion)

---

## Project Overview

This project is divided into two major assignments:

1. **Dictionary Validation:**  
   Many applications need to ensure that incoming data (typically in the form of dictionaries or JSON objects) meets a specified format. Here, a recursive validation function is implemented to compare a data dictionary with a template that defines the required keys and expected data types.

2. **Merging Word Frequency Dictionaries:**  
   In text data processing—such as analyzing logs or aggregating search queries—different data sources may produce word frequency dictionaries. The challenge is to merge these dictionaries so that the frequency of each word is summed across all sources. This is achieved using two methods:
   - One using `defaultdict` for its simplicity and automatic key initialization.
   - One using `Counter`, which is ideal for tallying counts, including negative values.

Automated tests (using `pytest`) and a GitHub Actions workflow ensure that both modules work correctly on every push or pull request.

---

## Module 1: student_code.py

### Assignment Description

The task for `student_code.py` is to build a function named `validate` that checks whether a given data dictionary conforms to a pre-defined template. In this template:
- Each key represents a required field.
- The corresponding value is either another dictionary (for nested data) or a Python type (e.g., `int`, `str`), indicating the expected type.

The function ensures:
- **Completeness:** All keys in the template must be present in the data.
- **No Extras:** The data should not contain keys that aren’t specified in the template.
- **Type Matching:** Every value in the data must be of the type indicated by the template.

If the data matches the template, the function returns `(True, '')`; otherwise, it returns `(False, error_message)`, with the error message indicating the problematic key using dot notation (e.g., `"mismatched keys: bio.birthplace.city"`).

### Functionality Overview

- **Recursive Validation:**  
  A recursive helper function traverses the nested dictionary, checking for required keys and verifying that each value is of the expected type.
  
- **Error Reporting:**  
  The function immediately returns an error message when it encounters the first mismatch, clearly indicating the location of the issue using dot notation.

### Implementation Details

The implementation relies on a helper function (commonly called `check`) that:
- Confirms the data is a dictionary when the template expects one.
- Iterates through the template’s keys, ensuring they exist in the data.
- Recursively validates nested dictionaries.
- Uses Python’s `isinstance` to verify that each value matches the expected type.

### Example Usage

Imagine you have a template for a user profile that includes fields like user ID, name (with first and last names), and bio (with date of birth and birthplace). When you pass a well-formed user profile dictionary to the `validate` function, it checks that all required keys are present and that each value is of the correct type. For instance, if the profile is complete and correctly formatted, the function returns `True` with no error message. However, if a field (such as the city in the birthplace) is missing or of the wrong type, it returns `False` along with an error message like `"mismatched keys: bio.birthplace.city"`.

---

## Module 2: student_merge.py

### Assignment Description

The goal for `student_merge.py` is to merge multiple word frequency dictionaries into a single dictionary. Two functions are provided:

- **merge_with_defaultdict:**  
  This function employs `collections.defaultdict` to automatically initialize word counts. It iterates through each provided dictionary and adds up the frequencies for each word.

- **merge_with_counter:**  
  This function uses `collections.Counter` to merge dictionaries. It manually updates the Counter to ensure even negative counts are processed correctly. In both cases, the final merged dictionary is sorted by descending frequency, with alphabetical order used to resolve ties.

### Functionality Overview

- **Defaultdict Approach:**  
  A defaultdict of integers is created to accumulate counts. As each dictionary is processed, the counts for each word are added together. Finally, the result is sorted so that words with the highest frequency come first.

- **Counter Approach:**  
  An empty Counter is initialized and manually updated with counts from each dictionary. This method is robust against negative counts and similarly sorts the merged results by frequency (and alphabetically for words with equal counts).

### Implementation Details

The merging process involves three main steps:
1. **Initialization:**  
   - For `merge_with_defaultdict`, initialize a defaultdict with a default integer value.
   - For `merge_with_counter`, initialize an empty Counter.
2. **Iteration and Merging:**  
   - Loop through each dictionary and add the counts for each word.
3. **Sorting the Result:**  
   - Sort the merged dictionary using a custom key that orders items by descending frequency (using negative values) and then alphabetically.

### Example Usage

Consider receiving word frequency data from three different servers:
- **Server 1** might report that "python" appears 10 times and "javascript" appears 15 times.
- **Server 2** might show "python" appears 6 times along with counts for "java" and "c++".
- **Server 3** might include additional words such as "erlang" or "haskell".

By calling either `merge_with_defaultdict` or `merge_with_counter` and passing these dictionaries as arguments, the function sums the counts for each word across all servers. The final output is a single, sorted dictionary where, for example, the word "python" (if it has the highest total frequency) appears first. This sorted result makes it easy to see which words are most common across all datasets.

---

## Testing and GitHub Actions Workflow

Automated tests (using `pytest`) ensure that both modules function correctly. The tests cover scenarios such as:
- Validating dictionaries against a template.
- Merging dictionaries with both positive and negative counts.
- Handling cases with no input dictionaries.
- Verifying that the final output is correctly sorted.

A GitHub Actions workflow is configured to automatically run these tests on every push or pull request, ensuring continuous integration and code quality.

---

## Conclusion

This project demonstrates practical techniques for two common challenges:
- **Validating Nested Dictionaries:** Ensuring that input data adheres to a specified structure and type requirements.
- **Merging Word Frequency Dictionaries:** Combining multiple datasets into a single, sorted dictionary using both `defaultdict` and `Counter`.

The modules `student_code.py` and `student_merge.py` come with comprehensive documentation and example usage explanations, making them valuable tools for projects involving JSON data validation and text analysis.
