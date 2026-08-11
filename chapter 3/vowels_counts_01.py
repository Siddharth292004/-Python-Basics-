def cal_vowel_count(text):
    text = text.lower()
    count = 0

    for char in text:
        if char in "aieou":
            count +=1
    return count


text = input("Enter the string: ")

vowel_count = cal_vowel_count(text)
print(f"Vowel count: {vowel_count}")
