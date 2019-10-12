# Case 2.

# Developers : Moiseenko V. (%),
#              Torgasheva A. (%),
#              Setskov M. (%).

    # *imports:
# import local as lc                  # Это нужно сделать.

# Данная программа позволяет вычислить годовой налог субъекта налогооблажения по американской системе.
# Облагаемая налогом сумма денег меняется в зависимости от особенностей субъектов налогообложения.



print('Добрый день, уважаемый пользователь. Данная программа позволяет вычислить годовой налог субъекта'
      ' налогооблажения по американской системе.\nОблагаемая налогом сумма денег меняется в зависимости'
      ' от особенностей субъектов налогообложения.')
print('Напишите, пожалуйста, на какой субъект будет рассчитан налог:')
subjeсt = input('один субъект, супружесая пара, родитель-одиночка')
if subjeсt == 'один субъект':
    import localforone as lc1
elif subjeсt == 'супружесая пара':
    import localfortwo as lc1
elif subjeсt == 'родитель-одиночка':
    import localforsingleparent as lc1
else:
    print('Выберите, пожалуйста, один из предложенных пунктов.')

# Здесь должен быть фрагмент программы, который будет узнавать зарплату пользователя в каждом месяце и просуммирует ее.
# Здесь надо спросить про сумму общих налоговых вычетов.
# Здесь нужно из годового дохода вычесть налоговые вычеты и поместить результат в пересенную "income".

income = 100000

if income > 0:
    if income >= lc1.first_stage_2:
        income1 = lc1.first_stage_2 * 0.1                               # Проценты по всей первой ступени.
    else:                                                               # Проценты, если доход в первой ступени.
        income1 = income * 0.1

    if income > lc1.second_stage_2:
        income2 = (lc1.second_stage_2 - lc1.second_stage_1) * 0.15      # Проценты по всей второй ступени.
    elif lc1.second_stage_1 <= income <= lc1.second_stage_2:            # Проценты, если доход во второй ступени.
        income2 = (income - lc1.second_stage_1) * 0.15
    else:
        income2 = 0

    if income > lc1.third_stage_2:                                      # Проценты по всей третьей ступени.
        income3 = (lc1.third_stage_2 - lc1.third_stage_1) * 0.25
    elif lc1.third_stage_1 <= income <= lc1.third_stage_2:              # Проценты, если доход в третьей ступени.
        income3 = (income - lc1.third_stage_1) * 0.25
    else:
        income3 = 0

    if income > lc1.fourth_stage_2:                                     # Проценты по всей четвертой ступени.
        income4 = (lc1.fourth_stage_2 - lc1.fourth_stage_1) * 0.28
    elif lc1.fourth_stage_1 <= income <= lc1.fourth_stage_2:            # Проценты, если доход в четвертой ступени.
        income4 = (income - lc1.fourth_stage_1) * 0.28
    else:
        income4 = 0

    if income > lc1.fifth_stage_2:                                      # Проценты по всей пятой ступени.
        income5 = (lc1.fifth_stage_2 - lc1.fifth_stage_1) * 0.33
    elif lc1.fifth_stage_1 <= income <= lc1.fifth_stage_2:              # Проценты, если доход в пятой ступени.
        income5 = (income - lc1.fifth_stage_1) * 0.33
    else:
        income5 = 0

    if income > lc1.sixth_stage_2:                                      # Проценты по всей второй ступени.
        income6 = (lc1.sixth_stage_2 - lc1.sixth_stage_1) * 0.35
    elif lc1.sixth_stage_1 <= income <= lc1.sixth_stage_2:              # Проценты, если доход в шестой ступени.
        income6 = (income - lc1.sixth_stage_1) * 0.35
    else:
        income6 = 0

    if income >= lc1.seventh_stage:                                     # Проценты, по седьмой ступени.
        income7 = (income - lc1.seventh_stage) * 0.396
    else:
        income7 = 0

    # Сумма налогов по каждой из ступеней.
    tax = income1 + income2 + income3 + income4 + income5+ income6 + income7
    print(tax)

else:
    print('Введите, пожалуйста, настоящую имеющуюся у вас налоговую базу.')








