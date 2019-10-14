# Case 2.

# Developers : Moiseenko V. (35%),
#              Torgasheva A. (37%),
#              Setskov M. (40%).

# This program allows to calculate annual tax of the subject of taxation on American system.
# The taxable amount of money changes depending on the particular taxation.

import local as lc

print(lc.TXT_INTRO_1, lc.TXT_INTRO_2, sep='\n')
print()
print(lc.TXT_SUBJECT)

subject_t = str(input()).lower()
if subject_t == lc.TXT_SUBJECT_1:
    import dataforone as dt
elif subject_t == lc.TXT_SUBJECT_2:
    import datafortwo as dt
elif subject_t == lc.TXT_SUBJECT_3:
    import dataforsingleparent as dt
else:
    print(lc.TXT_ELSE)

print()

name_month = lc.TXT_MONTHS
print(lc.TXT_INCOME_PER_MONTH)

annual_income_all = 0                                                             # Annual income with no annual tax deductions
for month in range(12):
    print('{} {}:'.format(lc.TXT_QUESTION, name_month[month], '?', end=''))
    income = float(input())
    annual_income_all += income
print(lc.TXT_ALL, annual_income_all)

print(lc.TXT_NV)
nv = float(input())
annual_income = annual_income_all - nv                                             # Annual income with tax deductions

if annual_income > 0:
    if annual_income >= dt.first_stage_2:                                          # Interest of the 1st stage.
        income_1 = dt.first_stage_2 * 0.1
    else:                                                                          # Interest if income is in the 1st stage.
        income_1 = annual_income * 0.1

    if annual_income > dt.second_stage_2:                                          # Interest of the 2nd stage.
        income_2 = (dt.second_stage_2 - dt.second_stage_1) * 0.15
    elif dt.second_stage_1 <= annual_income <= dt.second_stage_2:                  # Interest if income is in the 2nd stage.
        income_2 = (annual_income - dt.second_stage_1) * 0.15
    else:
        income_2 = 0

    if annual_income > dt.third_stage_2:                                           # Interest of the 3rd stage.
        income_3 = (dt.third_stage_2 - dt.third_stage_1) * 0.25
    elif dt.third_stage_1 <= annual_income <= dt.third_stage_2:                    # Interest if income is in the 3rd stage.
        income_3 = (annual_income - dt.third_stage_1) * 0.25
    else:
        income_3 = 0

    if annual_income > dt.fourth_stage_2:                                          # Interest of the 4th stage.
        income_4 = (dt.fourth_stage_2 - dt.fourth_stage_1) * 0.28
    elif dt.fourth_stage_1 <= annual_income <= dt.fourth_stage_2:                  # Interest if income is in the 4th stage.
        income_4 = (annual_income - dt.fourth_stage_1) * 0.28
    else:
        income_4 = 0

    if annual_income > dt.fifth_stage_2:                                           # Interest of the 5th stage.
        income_5 = (dt.fifth_stage_2 - dt.fifth_stage_1) * 0.33
    elif dt.fifth_stage_1 <= annual_income <= dt.fifth_stage_2:                    # Interest if income is in the 5th stage.
        income_5 = (annual_income - dt.fifth_stage_1) * 0.33
    else:
        income_5 = 0

    if annual_income > dt.sixth_stage_2:                                           # Interest of the 6th stage.
        income_6 = (dt.sixth_stage_2 - dt.sixth_stage_1) * 0.35
    elif dt.sixth_stage_1 <= annual_income <= dt.sixth_stage_2:                    # Interest if income is in the 6th stage.
        income_6 = (annual_income - dt.sixth_stage_1) * 0.35
    else:
        income_6 = 0

    if annual_income >= dt.seventh_stage:                                          # Interest of the 7th stage.
        income_7 = (annual_income - dt.seventh_stage) * 0.396                      # Interest if income is in the 7th stage.
    else:
        income_7 = 0

    tax = income_1 + income_2 + income_3 + income_4 + income_5 + income_6 + income_7  # Total amount of taxes.
    print(lc.TXT_TAX_SUM, '{:.1f}'.format(tax), lc.TXT_RUB)

else:
    print(lc.TXT_ERROR)
