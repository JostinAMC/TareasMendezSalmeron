# Aaron Salmeron Gamboa 2020168052
# Jostin Mendez Castro 2020034338

from Tarea1 import divide_string
from Tarea1 import mesure_area

# Pytest


def test_divide_string():
    assert divide_string('AbCdEf1$', 1) == 'ACE1 bdf$'
    assert divide_string('Este_es_un_ejemplo', 2) == 'Este_es_u  n_ejemplo'
    assert divide_string(1, 1) == 'Error 001'
    assert divide_string('AaronSalmeon', 1.5) == 'Error 002'
    assert mesure_area(5) == '78.53981633974483 25'
    assert mesure_area('JostinMendez') == 'Error 002'
