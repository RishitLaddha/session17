def validate(data, template):
    def check(data, template, path):
        # If the template expects a dictionary, data must also be a dictionary.
        if isinstance(template, dict):
            if not isinstance(data, dict):
                return False, f'bad type: {path}'
            # Check that every key in the template is present in data.
            for key in template:
                if key not in data:
                    current_path = f"{path}.{key}" if path else key
                    return False, f'mismatched keys: {current_path}'
            # Ensure that there are no extra keys in data.
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
            # When template is a type, check if data is of that type.
            if isinstance(data, template):
                return True, ""
            else:
                return False, f'bad type: {path}'

    return check(data, template, "")
