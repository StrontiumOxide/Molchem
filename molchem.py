from random import choice

all_elements = {
    "H": 1.00797,
    "He": 4.0026,
    "Li": 6.939,
    "Be": 9.0122,
    "B": 10.811,
    "C": 12.01115,
    "N": 14.0067,
    "O": 15.9994,
    "F": 18.9984,
    "Ne": 20.183,
    "Na": 22.9898,
    "Mg": 24.312,
    "Al": 26.9815,
    "Si": 28.086,
    "P": 30.9738,
    "S": 32.064,
    "Cl": 35.453,
    "Ar": 39.948,
    "K": 39.102,
    "Ca": 40.08,
    "Sc": 44.956,
    "Ti": 47.90,
    "V": 50.942,
    "Cr": 51.996,
    "Mn": 54.938,
    "Fe": 55.847,
    "Co": 58.9332,
    "Ni": 58.71,
    "Cu": 63.546,
    "Zn": 65.37,
    "Ga": 69.72,
    "Ge": 72.59,
    "As": 74.9216,
    "Se": 78.96,
    "Br": 79.904,
    "Kr": 83.80,
    "Rb": 85.47,
    "Sr": 87.62,
    "Y": 88.905,
    "Zr": 91.22,
    "Nb": 92.906,
    "Mo": 95.94,
    "Tc": 99,
    "Ru": 101.07,
    "Rh": 102.905,
    "Pd": 106.4,
    "Ag": 107.868,
    "Cd": 112.40,
    "In": 114.82,
    "Sn": 118.69,
    "Sb": 121.75,
    "Te": 127.60,
    "I": 126.9044,
    "Xe": 131.30,
    "Cs": 132.905,
    "Ba": 137.34,
    "La": 138.81,
    "Ce": 140.12,
    "Pr": 140.907,
    "Nd": 144.24,
    "Pm": 145,
    "Sm": 150.35,
    "Eu": 151.96,
    "Gd": 157.25,
    "Tb": 158.924,
    "Dy": 162.50,
    "Ho": 164.930,
    "Er": 167.26,
    "Tm": 168.934,
    "Yb": 173.04,
    "Lu": 174.97,
    "Hf": 178.49,
    "Ta":180.948,
    "W": 183.85,
    "Re": 186.2,
    "Os": 190.2,
    "Ir": 192.2,
    "Pt": 195.09,
    "Au": 196.967,
    "Hg": 200.59,
    "Tl": 204.37,
    "Pb": 207.19,
    "Bi": 208.980,
    "Po": 210,
    "At": 210,
    "Rn": 222,
    "Fr": 223,
    "Ra": 226,
    "Ac": 227,
    "Th": 232.038,
    "Pa": 231,
    "U": 238.03,
    "Np": 237,
    "Pu": 242,
    "Am": 243,
    "Cm": 247,
    "Bk": 247,
    "Cf": 249,
    "Es": 254,
    "Fm": 253,
    "Md": 256,
    "No": 255,
    "Lr": 257,
    "Rf": 261,
    "Db": 262,
    "Sg": 263,
    "Bh": 262,
    "Hs": 265,
    "Mt": 266,
    "Ds": 281,
    "Rg": 282,
    "Cn": 285,
    "Nh": 286,
    "Fl": 289.190,
    "Mc": 290,
    "Lv": 293,
    "Ts": 294,
    "Og": 294
    }

def definition_substance(str_substance: str) -> list:
    """
    Данная функция определяет какие элементы находятся в веществе
    """
        # Перевод строки в кортеж символов химического соединения
    substance_symbol = tuple(str_substance)

        # Сортировка на строчные и заглавные буквы:
    substance_element = []

        # Объявление лямбда-функций для сортировки символов:
    func_append_new = lambda symbol: substance_element.append([symbol]) # Добавление символа в новый список списка
    func_append_old = lambda symbol: substance_element[-1].append(symbol) # Добавление символа в последний список списка

    for symbol in substance_symbol:
         
            # Процесс сортировки
        if symbol in ["(", ")", "[", "]", "{", "}"]: func_append_new(symbol) # Если символ содержится в списке
        if symbol.isupper(): func_append_new(symbol) # Если символ - буква в верхнем регистре
        if symbol.islower(): func_append_old(symbol) # Если символ - буква в нижнем регистре
        if symbol.isdigit(): # Если символ - цифра
            if substance_element[-1][0].isdigit(): # Если предыдущий элемент - цифра
                func_append_old(symbol)
            else: # Если предыдущий элемент - не цифра
                func_append_new(symbol)

     # Объединение внутренних списков. Создание готового вещества в виде списка. Отправка на анализ
    substance = []
    for element in substance_element:
        substance.append("".join(element))

    return substance


def calcmol(str_substance: str) -> int:
    """
    Данная функция считает молярные массы веществ
    """
    list_substance = definition_substance(str_substance)

    # Перебор всех структурных единиц в списке
    all_molar_mass = []
    level_solution = 0  # Уровень вычислений
    """
    all_molar_mass - список, в котором содержаться уровни вычислений.
    Уровень вычислений - список с атомной массой (индекс 0) и молярной массой (индекс 1) вещества.
        -Нулевой уровень (индекс 0) - простой счёт молярной массы. (H2O, H2SO4, NaOH и тд)
        -Ненулевой уровень (индекс > 0) - уровни предназначенные для расчёта молярных масс внутри скобок. (Cu(NO3)2 и тд)
    Чем больше скобочек в вещества, тем более глубокий уровень рассчёта. (Na2[Zn(OH4)])
    """
    all_molar_mass.append([0.0, 0.0])
    for element in list_substance:

            # Определение уровня вычислений
        if element in ["(", "[", "{"]:
            all_molar_mass.append([0.0, 0.0])
            level_solution += 1

        if element in [")", "]", "}"]:
            all_molar_mass[level_solution - 1][0] = all_molar_mass[level_solution][1]
            all_molar_mass[level_solution - 1][1] += all_molar_mass[level_solution][1]
            del all_molar_mass[level_solution]
            level_solution -= 1

            # Вычисление атомных и молярных масс, согласно переменной level_solution
        if element in all_elements:
            all_molar_mass[level_solution][0] = all_elements[element]
        else:
            try:
                all_molar_mass[level_solution][0] *= (float(element) - 1)
            except ValueError: pass

        if element not in ["(", ")", "[", "]", "{", "}"]:
            all_molar_mass[level_solution][1] += all_molar_mass[level_solution][0]

        print(f'Символ: "{element}". Уровень вычислений: {all_molar_mass}')  # Раскоментировать для понятия процесса

    return round(all_molar_mass[level_solution][1], 4)
    

def elrandom(): 
    return choice(list(all_elements.keys()))


if __name__ == "__main__":
    print()
    print("""Hello, dear user!
This module is designed for calculating the molar masses of a substance
and for other needs!
To use, import into your file!!!""")
    print()
    

