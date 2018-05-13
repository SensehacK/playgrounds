# PF-Assgn-47
def encrypt_sentence(sentence):
    encrypted_sentence = ""
    for index, word in enumerate(sentence.split(" ")):
        # for words at even position
        if index % 2 == 0:
            for character in reversed(word):
                encrypted_sentence += character
            encrypted_sentence += " "
        else:
            vowels = ""
            consonants = ""
            for character in word:
                if character in "aeiou":
                    vowels += character
                else:
                    consonants += character
            encrypted_sentence += consonants
            encrypted_sentence += vowels
            encrypted_sentence+=" "
    # strip() removes blank space from both ends
    return encrypted_sentence.strip()
sentence = "The sun rises in the east"
encrypted_sentence = encrypt_sentence(sentence)
print(encrypted_sentence)
