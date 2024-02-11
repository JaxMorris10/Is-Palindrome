def is_palindrome(word):
    return word == word[::-1]

def check_palindromes(words, mode='any'):
    if mode == 'any':
        return any(is_palindrome(word) for word in words)
    elif mode == 'all':
        return all(is_palindrome(word) for word in words)
    else:
        raise ValueError("Invalid mode. Please use 'any' or 'all'.")

# Example usage:
word_list = ['level', 'radar', 'madam']

# Check if any word in the list is a palindrome
print("Any palindrome in the list:", check_palindromes(word_list, mode='any'))

# Check if all words in the list are palindromes
print("All palindromes in the list:", check_palindromes(word_list, mode='all'))
