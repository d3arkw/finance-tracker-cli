import os


def clear():
    os.system('cls' if  os.name == 'nt' else 'clear')

    
sel_language = 'en'


language = {
    'ru': {
        'prin': '-Добро пожаловать в программу по расчёту баланса!\n!!! Выберите действие !!!',
        'menu': 'Меню:\n1. Добавить Доход/Расход\n2. Показать Баланс\n3. История Операций\n4. Выбор страны\n5. Выход\nВыбранная страна:',
        'catdoh': 'Категории дохода:\n1. Работа\n2. Подарок\n3. Выплаты',
        'catras' : 'Категории расхода:\n1. Супермаркет\n2. Развлечения\n3. Об.Платежи',
        'inpdoh' : 'Введите доход:',
        'inpras' : 'Введите расход:',
        'error' : 'Ввод не соответствует условию',
        'sel' : 'Выберите: ',
        'selmenu' : 'Выберите пункт меню:',
        'bal' : 'Ваш баланс:',
        'inpcount' : 'Выберите страну: ',
        'bye' : 'До свидания!',
        'selected': '>Выбрано',
        'china' : 'Китай',
        'ras' : 'Расход:',
        'doh' : 'Доход:',
        'trans' : 'Операция №',
        'cat' : 'Категория: ',
        'other' : 'Прочее'
        },
    'en': {
        'prin': '- Welcome to the balance calculator program!\n!!! Choose an action !!!',
        'menu': 'Menu:\n1. Add Income/Expense\n2. Show Balance\n3. Transaction History\n4. Select Country\n5. Exit\nSelected country: ',
        'catdoh': 'Income categories:\n1. Work\n2. Gift\n3. Payouts',
        'catras': 'Expense categories:\n1. Supermarket\n2. Entertainment\n3. Bills',
        'inpdoh': 'Enter income: ',
        'inpras': 'Enter expense: ',
        'error': 'Invalid input',
        'sel': 'Select: ',
        'selmenu': 'Select a menu item: ',
        'bal': 'Your balance: ',
        'inpcount': 'Select a country: ',
        'bye': 'Goodbye!',
        'selected': '>Selected',
        'china' : 'China',
        'ras' : 'Expense:',
        'doh' : 'Income:',
        'trans' : 'Operation №',
        'cat' : 'Category: ',
        'other' : 'Other'
    }
}


def fun(key):
    return language[sel_language][key]


def sel_lang(sel_language):
    print('Select language(Выберите язык):\n1:Russian(Русский)\n2:English(Английский)')
    d = input(fun('sel'))
    sel_language = 'ru' if d == '1' else 'en' if d == '2' else 'en'
    clear()
    return sel_language


sel_language = sel_lang(sel_language)
data = {
    1: {'balance': 0, 'history': [], 'op': 1},
    2: {'balance': 0, 'history': [], 'op': 1},
    3: {'balance': 0, 'history': [], 'op': 1}
    }
sel_country = 1
cat_d = {'ru': {1: 'Зарплата', 2: 'Пособия', 3: 'Подарки'}, 'en': {1: 'Salary', 2: 'Benefits', 3: 'Gifts'}}
cat_r = {'ru': {1: 'Супермаркет', 2: 'Развлечения', 3: 'Об.Платежи'}, 'en': {1: 'Supermarket', 2: 'Entertainment', 3: 'Bills'}}
sel_d = 0
sel_r = 0


def cat_doh(sel_d):
    print(fun('catdoh'))
    sel_d = int(input(fun('sel')))
    return sel_d


def cat_ras(sel_r):
    print(fun('catras'))
    sel_r = int(input(fun('sel')))
    return sel_r


def get_country(sel_country):
    country = {1: 'Россия', 2: 'USA', 3: fun('china')}
    return country[sel_country]


def menu():
    print(fun('menu') + get_country(sel_country))
    

def get_op(data, sel_country):
    data[sel_country]['op'] += 1


def get_num(data, sel_country):
    return data[sel_country]['op']
    

def get_ter(sel_country):
    a = {1: ' Руб.', 2: ' $', 3: ' ¥'}
    return a[sel_country]


def menu_country(sel_country):
    print('1. Россия'+ (fun('selected') if sel_country == 1 else '' ))
    print('2. USA'+ (fun('selected') if sel_country == 2 else '' ))
    print(f'3. {fun("china")}'+ (fun("selected") if sel_country == 3 else '' ))


def get_sum(data,sel_country,cat_d,cat_r, sel_d,sel_r):
    doh = input(fun('inpdoh')).strip()
    if doh.isdigit():
        sel_d = cat_doh(sel_d)
        ras = input(fun('inpras')).strip()
        if ras.isdigit():
            sel_r = cat_ras(sel_r)
            data[sel_country]['balance'] += int(doh)-int(ras)
            print(f'''\n{fun('doh')}{doh}{get_ter(sel_country)}\n{fun('ras')}{ras}{get_ter(sel_country)}\n{fun('bal')}{data[sel_country]['balance']}{get_ter(sel_country)}''')
            data[sel_country]['history'].append(f'{fun('trans')}{get_num(data, sel_country)}:+{int(doh)}{get_ter(sel_country)},{fun('cat')}{cat_d.get(sel_language,{}).get(sel_d, fun('other'))}')
            get_op(data, sel_country)
            data[sel_country]['history'].append(f'{fun('trans')}{get_num(data, sel_country)}:-{int(ras)}{get_ter(sel_country)},{fun('cat')}{cat_r.get(sel_language,{}).get(sel_r, fun('other'))}')
            get_op(data, sel_country)
        else:
            print(fun('error'))
    else:
        print(fun('error'))
    return data,sel_d,sel_r


def get_bal(data, sel_country):
    print(fun('bal'), data[sel_country]["balance"], get_ter(sel_country))


def get_ist(data, sel_country):
    for i in data[sel_country]['history']:
        print(i)


print(fun('prin'))
while True:
    menu()
    sel_menu = input(fun('selmenu'))
    if sel_menu == '1':
        clear()
        data,sel_d,sel_r = get_sum(data, sel_country,cat_d,cat_r,sel_d,sel_r)
    elif sel_menu == '2':
        clear()
        get_bal(data,sel_country)
    elif sel_menu == '3':
        clear()
        get_ist(data,sel_country)
    elif sel_menu == '4':
        clear()
        menu_country(sel_country)
        sel_country = int(input(fun('inpcount')).strip())
        if sel_country not in data:
            print(fun('error'))
    elif sel_menu == '5':
        print(fun('bye'))
        break
    else:
        print(fun('error'))