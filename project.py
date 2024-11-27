import getpass
import re

# التحقق من أن النص يحتوي على حروف فقط والمسافات
def is_valid_text(text):
    if not re.match(r"^[a-zA-Z\s]*$", text):  # التحقق من أن النص يحتوي على حروف فقط
        print("Error: Only letters and spaces are allowed.")
        return False
    return True

# 1. تحويل النص إلى أحرف كبيرة وصغيرة
def convert_text_case(text):
    upper_text = text.upper()
    lower_text = text.lower()
    print("\n----- Convert Text Case -----")
    print("Uppercase:", upper_text)
    print("Lowercase:", lower_text)

# 2. حساب عدد الأحرف والكلمات في النص
def count_chars_words(text):
    char_count = len(text)
    word_count = len(text.split())
    print("\n----- Character and Word Count -----")
    print("Character Count (including spaces):", char_count)
    print("Word Count:", word_count)

# 3. حساب طول السلسلة
def calculate_string_length(text):
    length = len(text)
    print("\n----- String Length -----")
    print("String Length:", length)

# 4. استخراج أول وآخر حرف من السلسلة
def first_and_last_character(text):
    if text:
        first_char = text[0]
        last_char = text[-1]
        print("\n----- First and Last Character -----")
        print("First Character:", first_char)
        print("Last Character:", last_char)
    else:
        print("\n----- First and Last Character -----")
        print("The string is empty.")

# 5. التحقق من كلمة مرور قوية
def is_strong_password(password):
    print("\n----- Password Strength Check -----")
    if (any(c.isupper() for c in password) and 
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in "@!" for c in password)):
        print("Result: Strong Password")
    else:
        print("Result: Weak Password")

# 6. حساب عدد الحروف الساكنة والمتحركة
def count_vowels_consonants(text):
    vowels = "AEIOUaeiou"
    vowel_count = sum(1 for c in text if c in vowels)
    consonant_count = sum(1 for c in text if c.isalpha() and c not in vowels)
    print("\n----- Vowel and Consonant Count -----")
    print("Vowel Count:", vowel_count)
    print("Consonant Count:", consonant_count)

# 7. تكرار سلسلة نصية بعدد معين، مع جعل كل تكرار في سطر جديد
def repeat_string(text, times):
    repeated_text = (text + "\n") * times
    print("\n----- Repeated Text -----")
    print("Repeated Text:\n" + repeated_text)

# 8. استخراج الأحرف الفردية والزوجية من النص
def extract_odd_even_characters(text):
    odd_chars = text[::2]
    even_chars = text[1::2]
    print("\n----- Odd and Even Positioned Characters -----")
    print("Odd-positioned Characters:", odd_chars)
    print("Even-positioned Characters:", even_chars)


if __name__ == "__main__":
    text = input("Enter text: ")
    # تحقق من صحة النص قبل تنفيذ أي عمليات
    if not is_valid_text(text):
        exit()  # إذا كان النص غير صالح، نخرج من البرنامج
    
    password = getpass.getpass("Enter password: ")
    repeat_times = int(input("Enter repeat count: "))

    convert_text_case(text)
    count_chars_words(text)
    calculate_string_length(text)
    first_and_last_character(text)
    is_strong_password(password)
    count_vowels_consonants(text)
    repeat_string(text, repeat_times)
    extract_odd_even_characters(text)
