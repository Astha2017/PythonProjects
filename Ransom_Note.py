def can_construct(ransomNote, magazine):
    magazine_chars = {}
    
    # Count the occurrences of each character in magazine
    for char in magazine:
        magazine_chars[char] = magazine_chars.get(char, 0) + 1
    
    # Check if ransomNote can be constructed
    for char in ransomNote:
        if char not in magazine_chars or magazine_chars[char] == 0:
            return False
        magazine_chars[char] -= 1
    
    return True

# Example usage:
ransomNote = "a"
magazine = "b"
print(can_construct(ransomNote, magazine))  # Output: False

