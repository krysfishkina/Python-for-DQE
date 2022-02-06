# 1. You NEED TO normalize it fROM letter CASEs point oF View.

import re

initial_text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix “iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# 1.  normalize it fROM letter CASEs point oF View

new_text = ""
for i in re.split(r'([.:]\s*|\n\t)', initial_text):  # split the text into sentences. Use ".:" for the second line, as discussed at the Q&A session
    new_text += i.capitalize()  # normalize each sentence
print("""Normal case text is:
""", new_text)

# 2. create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

last_words = re.findall(r'\w+(?=[.])', new_text)  # find the last word in the sentence
new_sentence = (' '.join(last_words))  # combine words into the sentence
final_sentence = new_sentence.capitalize()  # capitalize the sentence
end_of_paragraph = 'the end of this paragraph'
list_of_text = re.split(r'(^|[.]\s|\n\t)', new_text)

for index, i in enumerate(list_of_text):  # find a paragraph which needs to add the sentence
    if end_of_paragraph in i:
        list_of_text[index] = i + '. ' + final_sentence
        final_text = ''.join(list_of_text)
        pass
print("""Text with new sentence is:
""", final_text)

# 3 fix “iZ” with correct “is”, but ONLY when it Iz a mistAKE

change_Iz = ""
for i in final_text:
    change_Iz = final_text.replace(' iz ', ' is ')  # use spaces to fix only the right places
print(""" Text without "Iz" mistake is:
""", change_Iz)

# 4 calculate number of whitespace characters in this text

white_spaces = len(re.findall(r'\x20', change_Iz))  # use regular expression to count whitespaces
print("""Total number of whitespaces is:
""", white_spaces)