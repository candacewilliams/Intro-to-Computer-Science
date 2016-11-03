my_str = input('Enter a String :')

def CountVowels(my_str):
    num_vowels = 0
    for char in my_str:
        if char == 'a':
            num_vowels +=1
        elif char == 'e':
            num_vowels +=1
        elif char == 'i':
            num_vowels +=1
        elif char == 'o':
            num_vowels +=1
        elif char == 'u':
            num_vowels +=1
    print(num_vowels)


CountVowels(my_str)
