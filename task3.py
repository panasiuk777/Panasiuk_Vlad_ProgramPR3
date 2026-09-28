# 1-2. Речення про себе
about = "I study programming at college and I like motorbikes very much."

print("About me:")
print(about)

# 3. Кількість слів, найдовше слово та слова у зворотному порядку
words = about.split()

print("\nNumber of words:", len(words))

longest_word = max(words, key=len)
print("Longest word:", longest_word)

print("Words in reverse order:")
print(" ".join(words[::-1]))

# 4. Кількість літер 'a' без урахування регістру
a_count = about.lower().count("a")

print("\nNumber of 'a' letters:", a_count)

# 5. Кожне слово з великої літери
capitalized_sentence = about.title()

print("\nCapitalized sentence:")
print(capitalized_sentence)

# Замінюємо пробіли на _
underscored_sentence = about.replace(" ", "_")

print("\nSentence with underscores:")
print(underscored_sentence)

# 6. Функція перевірки паліндрому
def is_palindrome(text):
    cleaned_text = "".join(text.lower().split())
    return cleaned_text == cleaned_text[::-1]


print("\nIs my name a palindrome:", is_palindrome("Vlad"))
print("Is 'Never odd or even' a palindrome:",
      is_palindrome("Never odd or even"))

# 7. Шифр Цезаря
day = 27


def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


my_name = "Vlad"

encrypted = caesar_encrypt(my_name, day)
decrypted = caesar_decrypt(encrypted, day)

print("\nOriginal name:", my_name)
print("Encrypted name:", encrypted)
print("Decrypted name:", decrypted)
