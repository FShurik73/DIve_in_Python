# 📌Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов. 
# 📌Возвращается строка в нижнем регистре.

from string import ascii_lowercase
import doctest

def clear_text(text: str):
    """ 
    Clear text
    >>> clear_text('text') == 'text'   
    True
    >>> clear_text('TexT') == 'text'
    True
    >>> clear_text('te..xT') == 'text'
    True
    >>> clear_text('TeЯ..xT') == 'text'
    True
    >>> clear_text('TeююЯЯ..xT') == 'text'
    True
    """
    result = ''
    if text is not  None:
        for i in text:
            if i.lower() in ascii_lowercase + ' ':
                result += i
        return result.lower()
    raise ValueError('Incorrect text')

if __name__ == '__main__':
    doctest.testmod(verbose=True)



    

