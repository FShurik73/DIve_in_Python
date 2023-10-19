"""
Напишите для задачи 1 тесты pytest. Проверьте следующие варианты: 
📌возврат строки без изменений 
📌возврат строки с преобразованием регистра без потери символов 
📌возврат строки с удалением знаков пунктуации 
📌возврат строки с удалением букв других алфавитов 
📌возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""
from task_1 import clear_text
import pytest

def test1():
    assert clear_text('text') == 'text'

def test2():
    assert clear_text('TexT') == 'text'

def test3():
    assert clear_text('te..xT') == 'text'

def test4():
    assert clear_text('TeЯ..xT') == 'text'

def test5():
    assert clear_text('TeююЯЯ..xT') == 'text'

if __name__ == '__main__':
    pytest.main(['-v'])



