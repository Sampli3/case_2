# Case 2.

# Developers : Moiseenko V. (%), Torgasheva A. (%), Setskov M. (%).

# Данная программа позволяет вычислить годовой налог субъекта налогообложения по американской системе.
# Облагаемая налогом сумма денег меняется в зависимости от особенностей налогообложения.

import localforone
import localforsingleparent
import localfortwo

print('Добрый день, уважаемый пользователь. '
      'Данная программа позволяет вычислить годовой налог субъекта '
      'налогообложения по американской системе.\n'
      'Облагаемая налогом сумма денег меняется в зависимости '
      ' от особенностей субъектов налогообложения.')
print('Напишите, пожалуйста, на какой субъект будет рассчитан налог: один субъект, супружеская пара'
      ' или родитель-одиночка')

subject_t = str(input(''))
if subject_t == 'один субъект':
    import localforone as lc1
elif subject_t == 'супружеская пара':
    import localfortwo as lc1
elif subject_t == 'родитель-одиночка':
    import localforsingleparent as lc1
else:
    print('Выберите, пожалуйста, один из предложенных пунктов.')

print('Распишите ваши доходы по месяцам и напишите сумму годовых налоговых вычетов:')
salary_1m = float(input())  # Зарплата субъекта за первый месяц
salary_2m = float(input())  # Зарплата субъекта за второй месяц
salary_3m = float(input())  # Зарплата субъека за третий месяц
salary_4m = float(input())  # Зарплата субъекта за четвертый месяц
salary_5m = float(input())  # Зарплата субъекта за пятый месяц
salary_6m = float(input())  # Зарплата субъекта за шестой месяц
salary_7m = float(input())  # Зарплата субъекта за седьмой месяц
salary_8m = float(input())  # Зарплата субъекта за восьмой месяц
salary_9m = float(input())  # Зарплата субъекта за девятый месяц
salary_10m = float(input())  # Зарплата субъекта за десятый месяц
salary_11m = float(input())  # Зарплата субъекта за одиннадцатый месяц
salary_12m = float(input())  # Зарплата субъекта за двенадцатый месяц
tax_dy = float(input())  # Сумма налоговых вычетов в год

income1 = salary_1m + salary_2m + salary_3m + salary_4m + salary_5m + salary_6m
income2 = salary_7m + salary_8m + salary_9m + salary_10m + salary_11m + salary_12m
income = income1 + income2 - tax_dy  # Сумма денег, подлежащая налогообожению

if income > 0:
    if income >= lc1.first_stage_2:
        income1 = lc1.first_stage_2 * 0.1  # Проценты по всей первой ступени.
    else:  # Проценты, если доход в первой ступени.
        income1 = income * 0.1

    if income > lc1.second_stage_2:
        income2 = (lc1.second_stage_2 - lc1.second_stage_1) * 0.15  # Проценты по всей второй ступени.
    elif lc1.second_stage_1 <= income <= lc1.second_stage_2:  # Проценты, если доход во второй ступени.
        income2 = (income - lc1.second_stage_1) * 0.15
    else:
        income2 = 0

    if income > lc1.third_stage_2:  # Проценты по всей третьей ступени.
        income3 = (lc1.third_stage_2 - lc1.third_stage_1) * 0.25
    elif lc1.third_stage_1 <= income <= lc1.third_stage_2:  # Проценты, если доход в третьей ступени.
        income3 = (income - lc1.third_stage_1) * 0.25
    else:
        income3 = 0

    if income > lc1.fourth_stage_2:  # Проценты по всей четвертой ступени.
        income4 = (lc1.fourth_stage_2 - lc1.fourth_stage_1) * 0.28
    elif lc1.fourth_stage_1 <= income <= lc1.fourth_stage_2:  # Проценты, если доход в четвертой ступени.
        income4 = (income - lc1.fourth_stage_1) * 0.28
    else:
        income4 = 0

    if income > lc1.fifth_stage_2:  # Проценты по всей пятой ступени.
        income5 = (lc1.fifth_stage_2 - lc1.fifth_stage_1) * 0.33
    elif lc1.fifth_stage_1 <= income <= lc1.fifth_stage_2:  # Проценты, если доход в пятой ступени.
        income5 = (income - lc1.fifth_stage_1) * 0.33
    else:
        income5 = 0

    if income > lc1.sixth_stage_2:  # Проценты по всей второй ступени.
        income6 = (lc1.sixth_stage_2 - lc1.sixth_stage_1) * 0.35
    elif lc1.sixth_stage_1 <= income <= lc1.sixth_stage_2:  # Проценты, если доход в шестой ступени.
        income6 = (income - lc1.sixth_stage_1) * 0.35
    else:
        income6 = 0

    if income >= lc1.seventh_stage:  # Проценты, по седьмой ступени.
        income7 = (income - lc1.seventh_stage) * 0.396
    else:
        income7 = 0

    tax = income1 + income2 + income3 + income4 + income5 + income6 + income7  # Сумма налогов по каждой из ступеней.
    print(tax)

else:
    print('Введите, пожалуйста, настоящую имеющуюся у вас налоговую базу.')
