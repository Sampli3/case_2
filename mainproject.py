# Case 2.

# Developers : Moiseenko V. (%),
#              Torgasheva A. (%),
#              Setskov M. (%).

# This program allows to calculate annual tax of the subject of taxation on American system.
# The taxable amount of money changes depending on the particular taxation.

import local as lc

print(lc.TXT_INTRO_1, lc.TXT_INTRO_2, sep='\n')
print()
print(lc.TXT_SUBJECT, end=' ')

subject_t = str(input()).lower()
if subject_t == lc.TXT_SUBJECT_1:
    import dataforone as dt
elif subject_t == lc.TXT_SUBJECT_2:
    import datafortwo as dt
elif subject_t == lc.TXT_SUBJECT_3:
    import dataforsingleparent as dt
else:
    print(lc.TXT_ELSE)

print(lc.TXT_INCOME_PER_MONTH)
salary_1m = float(input(lc.TXT_1ST_MONTH))                                  # Subject salary for the 1st month.
salary_2m = float(input(lc.TXT_2ND_MONTH))                                  # Subject salary for the 2nd month.
salary_3m = float(input(lc.TXT_3RD_MONTH))                                  # Subject salary for the 3rd month.
salary_4m = float(input(lc.TXT_4TH_MONTH))                                  # Subject salary for the 4th month.
salary_5m = float(input(lc.TXT_5TH_MONTH))                                  # Subject salary for the 5th month.
salary_6m = float(input(lc.TXT_6TH_MONTH))                                  # Subject salary for the 6th month.
salary_7m = float(input(lc.TXT_7TH_MONTH))                                  # Subject salary for the 7th month.
salary_8m = float(input(lc.TXT_8TH_MONTH))                                  # Subject salary for the 8th month.
salary_9m = float(input(lc.TXT_9TH_MONTH))                                  # Subject salary for the 9th month.
salary_10m = float(input(lc.TXT_10TH_MONTH))                                # Subject salary for the 10th month.
salary_11m = float(input(lc.TXT_11TH_MONTH))                                # Subject salary for the 11th month.
salary_12m = float(input(lc.TXT_12TH_MONTH))                                # Subject salary for the 12th month.
tax_dy = float(input(lc.TXT_TAX_DEDUCTION))                                 # The amount of tax deductions per year.

income_1 = salary_1m + salary_2m + salary_3m + salary_4m + salary_5m + salary_6m
income_2 = salary_7m + salary_8m + salary_9m + salary_10m + salary_11m + salary_12m
income = income_1 + income_2 - tax_dy                                       # Amount of taxable money.

if income > 0:
    if income >= dt.first_stage_2:                                          # Interest of the 1st stage.
        income_1 = dt.first_stage_2 * 0.1
    else:                                                                   # Interest if income is in the 1st stage.
        income_1 = income * 0.1

    if income > dt.second_stage_2:                                          # Interest of the 2nd stage.
        income_2 = (dt.second_stage_2 - dt.second_stage_1) * 0.15
    elif dt.second_stage_1 <= income <= dt.second_stage_2:                  # Interest if income is in the 2nd stage.
        income_2 = (income - dt.second_stage_1) * 0.15
    else:
        income_2 = 0

    if income > dt.third_stage_2:                                           # Interest of the 3rd stage.
        income_3 = (dt.third_stage_2 - dt.third_stage_1) * 0.25
    elif dt.third_stage_1 <= income <= dt.third_stage_2:                    # Interest if income is in the 3rd stage.
        income_3 = (income - dt.third_stage_1) * 0.25
    else:
        income_3 = 0

    if income > dt.fourth_stage_2:                                          # Interest of the 4th stage.
        income_4 = (dt.fourth_stage_2 - dt.fourth_stage_1) * 0.28
    elif dt.fourth_stage_1 <= income <= dt.fourth_stage_2:                  # Interest if income is in the 4th stage.
        income_4 = (income - dt.fourth_stage_1) * 0.28
    else:
        income_4 = 0

    if income > dt.fifth_stage_2:                                           # Interest of the 5th stage.
        income_5 = (dt.fifth_stage_2 - dt.fifth_stage_1) * 0.33
    elif dt.fifth_stage_1 <= income <= dt.fifth_stage_2:                    # Interest if income is in the 5th stage.
        income_5 = (income - dt.fifth_stage_1) * 0.33
    else:
        income_5 = 0

    if income > dt.sixth_stage_2:                                           # Interest of the 6th stage.
        income_6 = (dt.sixth_stage_2 - dt.sixth_stage_1) * 0.35
    elif dt.sixth_stage_1 <= income <= dt.sixth_stage_2:                    # Interest if income is in the 6th stage.
        income_6 = (income - dt.sixth_stage_1) * 0.35
    else:
        income_6 = 0

    if income >= dt.seventh_stage:                                          # Interest of the 7th stage.
        income_7 = (income - dt.seventh_stage) * 0.396                      # Interest if income is in the 7th stage.
    else:
        income_7 = 0

    tax = income_1 + income_2 + income_3 + income_4 + income_5 + income_6 + income_7  # Total amount of taxes.
    print(':.1f'.format(tax))

else:
    print(lc.TXT_ERROR)
