#!/usr/bin/python3
"""text_indentation module

A module that contains two functions ``text_indentation()`` and ``get_line()``
-> text_indentation() - is a function that prints a text with 2 new lines after
                        each of these characters: ., ? and :

-> get_line() - returns a list of lines from a string
"""


def get_line(txt):
    """A helper function

    Returns a new list containing words delimited by ., ?, or :

    Args:
        txt (str): the string to search
    Return:
        Returns a new list containing words delimited by ., ?, or :
    """
    word_list = []
    new_delimited_line = ""
    count = 0
    for char in txt:
        count += 1
        new_delimited_line = new_delimited_line + char
        if char in ['.', '?', ':']:
            word_list.append(new_delimited_line)
            new_delimited_line = ""
        if char not in ['.', '?', ':'] and count == len(txt):
            word_list.append(new_delimited_line)
    return word_list


def split_line(line):
    """A function that splits a line ``line`` into words

    Returns a list containing the words
    Returns an emply list if no wordis found
    """
    words_list = []
    n_str = ""
    count = 0
    for char in line:
        count += 1
        if char != " ":
            n_str += char
        elif char == " ":
            if n_str != "":
                words_list.append(n_str)
            n_str = ""
        if char != " " and count == len(line):
            words_list.append(n_str)
    return words_list

def text_indentation(text):
    """A function that prints ``text`` with 2 newlines after `.` or `?`
    or `:`

    Args:
        text (str): the first argument to the function.
            It must be a string.

    Return:
        Returns nothing. It only prints the converted text on the screen.
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    if text == "":
        return

    delimited_lines = get_line(text)

    count = 0
    for line in delimited_lines:
        count += 1
        line = line.strip()
        words = split_line(line)
        line = " ".join(words)
        print(line, end="")
        if count == len(delimited_lines):
            print("", end="")
        else:
            print('\n')

if __name__ == "__main__":
    text_indentation = __import__('5-text_indentation').text_indentation

    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
    Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
    Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
    Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
    rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
    stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
    cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
    beatiorem! Iam ruinas videres""")

    text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
    Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
    Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
    Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
    rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
    stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
    cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
    beatiorem! Iam ruinas videres")

    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing \
    elit. \
    Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
    Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
    Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
    rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
    stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
    cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
    beatiorem! Iam \nruinas videres""")


