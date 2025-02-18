# student_code.py

"""
Module: student_code.py
Description:
    This module provides a function to validate the structure and data types
    of a nested dictionary against a given template.
    It is useful for ensuring that input data (e.g., JSON) conforms to an expected format.

Function:
    validate(data, template)
        - data: The dictionary to validate.
        - template: The template dictionary specifying expected keys and types.
        Returns a tuple (state, error) where:
            - state: True if the data matches the template; False otherwise.
            - error: An error message (empty if valid), indicating the first mismatch.
"""

def validate(data, template):
    def check(data, template, path):
        """
        Recursively checks if 'data' conforms to the 'template' structure.
        
        Parameters:
            data (dict or value): The current data segment to check.
            template (dict or type): The template structure or expected type.
            path (str): The current key path (used for error reporting).
        
        Returns:
            (bool, str): A tuple where the first element is True if valid, otherwise False.
                         The second element is an error message (empty if valid).
        """
        # If the template is a dictionary, the data must also be a dictionary.
        if isinstance(template, dict):
            if not isinstance(data, dict):
                # Data is not a dict when one is expected.
                return False, f'bad type: {path}'
            
            # Check that every key in the template exists in the data.
            for key in template:
                if key not in data:
                    # Missing key; build the full path and return error.
                    current_path = f"{path}.{key}" if path else key
                    return False, f'mismatched keys: {current_path}'
            
            # Check that there are no extra keys in the data.
            for key in data:
                if key not in template:
                    current_path = f"{path}.{key}" if path else key
                    return False, f'mismatched keys: {current_path}'
            
            # Recursively validate each key's value.
            for key in template:
                current_path = f"{path}.{key}" if path else key
                valid, error = check(data[key], template[key], current_path)
                if not valid:
                    return valid, error
            return True, ""
        else:
            # If the template is a type (e.g., int, str), check if data is of that type.
            if isinstance(data, template):
                return True, ""
            else:
                return False, f'bad type: {path}'

    # Start the recursive check with an empty key path.
    return check(data, template, "")
