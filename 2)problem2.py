def reverse_vowels(s: str) -> str:
    vowels = [c for c in s if c in "aeiouAEIOU"]
    return ''.join(c if c not in "aeiouAEIOU" else vowels.pop() for c in s)
print(reverse_vowels("hello world"))
