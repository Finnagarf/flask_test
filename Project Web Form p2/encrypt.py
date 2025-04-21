# Paste in the requested functions from your Coded Messages assignment.
# If you didn't complete that assignment, use the code from the
# LCHS-web-form-part-2 GitHub repository: https://github.com/LaunchCodeEducation/LCHS-web-form-part-2
import string

def alphabet_position(char):
    return string.ascii_lowercase.find(char.lower())

def shift_character(char, shift):
    if char.lower() not in string.ascii_lowercase:
        return char
    new_index = (alphabet_position(char) + shift)%26
    new_char = string.ascii_lowercase[new_index]
    if char.isupper():
        return new_char.upper()
    else:
        return new_char

def encrypt_with_shift(text, shift):
    new_message = ''
    for char in text:
        new_message += shift_character(char, shift)
    return new_message

def build_keyword_alphabet(keyword):
    keyword = ''.join(sorted(set(keyword), key=keyword.index))  # Remove duplicates, keep order
    keyword = keyword.lower()
    remaining_letters = [c for c in string.ascii_lowercase if c not in keyword]
    return keyword + ''.join(remaining_letters)

def encrypt_with_keyword(text, shift, keyword):
    if not keyword:
        print("No keyword provided, using standard Caesar cipher.")
        return encrypt_with_shift(text, shift)
    print(f"Using keyword alphabet with: {keyword}")
    keyword_alphabet = build_keyword_alphabet(keyword)
    standard_alphabet = string.ascii_lowercase
    result = ''
    
    for char in text:
        if char.lower() not in standard_alphabet:
            result += char
        else:
            is_upper = char.isupper()
            original_index = (standard_alphabet.index(char.lower()) + shift) % 26
            new_char = keyword_alphabet[original_index]
            result += new_char.upper() if is_upper else new_char
            
    return result
