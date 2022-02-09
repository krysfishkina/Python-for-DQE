import re
import random
import string

# 1. function for creating a list with random dicts and random consisting (from 2 to 10)


def new_random_dict(min_dicts=2, max_dicts=10):
    list_of_dicts = []
    random_dict = {}
    for i in range(random.randint(min_dicts, max_dicts)):
        for j in range(random.randint(1, 20)):
            random_dict[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
        new_dict = random_dict.copy()
        list_of_dicts.append(new_dict)
        random_dict.clear()
    print(f'\n The list of random number of dicts (from 2 to 10) where numbers of keys is letter:\n {list_of_dicts}')
    return list_of_dicts

# 2. get previously generated list of dicts and create one common dict


def dict_from_list_of_dicts(list_for_input):
    final_dict = {}
    if type(list_for_input) == list:
        common_dict = {}
        key_entry = {}
        for index, each_dict in enumerate(list_for_input):
            for key in each_dict.keys():
                if key not in common_dict:
                    common_dict[key] = each_dict[key]
                    key_entry[key] = 1
                elif common_dict[key] < each_dict[key]:
                    key_entry[key] = index + 1
                    common_dict[key] = each_dict[key]
        for i in common_dict:
            if key_entry.get(i) > 1:
                final_dict[str(i) + '_' + str(key_entry.get(i))] = common_dict.get(i)
            else:
                final_dict[i] = common_dict.get(i)
        print(f'\n The final dict:\n {final_dict}')
        return final_dict


list_of_random_dicts = new_random_dict()
one_common_dict = dict_from_list_of_dicts(list_of_random_dicts)

# 3. You need to normalize text from letter cases point of view.


def normalize_text(text_for_input=''):
    if text_for_input == '':
        print("Enter text into function")
    else:
        new_text = ""
        for i in re.split(r'([.:]\s*|\n\t)', initial_text):
            new_text += i.capitalize()
        print(f'\n Normal case text is:\n {new_text}')
        return new_text

# 4. Create one more sentence with last words of each existing sentence and add it to the end of this paragraph


def add_sentence_to_paragraph(end_of_paragraph='', text_for_input=''):
    if text_for_input == '':
        print("Enter text into function")
    else:
        last_words = re.findall(r'\w+(?=[.])', text_for_input)
        new_sentence = (' '.join(last_words))
        final_sentence = new_sentence.capitalize()
        end_of_paragraph = 'the end of this paragraph'
        list_of_text = re.split(r'(^|[.]\s|\n\t)', text_for_input)
        for index, i in enumerate(list_of_text):
            if end_of_paragraph in i:
                list_of_text[index] = i + '. ' + final_sentence
                final_text = ''.join(list_of_text)
                pass
                print(f'\n Text with new sentence is: \n {final_text}')
                return final_text

# 5. Fix“iz” with correct “is”, but only when it is a mistake


def change_iz_is(text_for_input=''):
    if text_for_input == '':
        print("Enter text into function")
    else:
        change_iz = text_for_input.replace(' iz ', ' is ')
        print(f'\n Text without "Iz" mistake is: \n {change_iz}')
        return change_iz

# 6. Calculate number of whitespace characters in this text


def count_spaces(text_for_input=''):
    if text_for_input == '':
        print("Enter text into function")
    else:
        white_spaces = len(re.findall(r'\x20', text_for_input))
        print(f'\n Total number of whitespaces is: \n {white_spaces}')
        return white_spaces


if __name__ == '__main__':
    initial_text = """homework:
        tHis iz your homeWork, copy these Text to variable. 
        You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
        it iZ misspeLLing here. fix “iZ” with correct “is”, but ONLY when it Iz a mistAKE. 
        last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

    text_with_norm_case = normalize_text(initial_text)
    new_s = add_sentence_to_paragraph('end of this paragraph', text_with_norm_case)
    changeIS = change_iz_is(new_s)
    count_white_spaces = count_spaces(changeIS)

