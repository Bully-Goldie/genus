import pymorphy2

def replace_endings(text, target_gender):
    morph = pymorphy2.MorphAnalyzer()
    words = text.split()

    for i, word in enumerate(words):
        parsed_word = morph.parse(word)[0]
        base_form_gender = parsed_word.normalized.tag.gender
        if base_form_gender == 'femn' and target_gender == 'masc':
            inflected_word = parsed_word.inflect({'masc'})
        elif base_form_gender != 'femn' and target_gender == 'femn':
            inflected_word = parsed_word.inflect({'femn'})
        else:
            inflected_word = None
                
        if inflected_word:
            words[i] = inflected_word.word

    modified_text = ' '.join(words)
    return modified_text

text = input("Введите предложение: ")

target_gender = input("Введите желаемый грамматический род ('masc' для мужского, 'femn' для женского): ")

modified_text = replace_endings(text, target_gender)

print("Измененное предложение:", modified_text)
