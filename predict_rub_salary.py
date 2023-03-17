def predict_rub_salary(from_salary=None, to_salary=None):
    if  from_salary and to_salary:
        average_salary = from_salary + to_salary / 2
    elif from_salary:
        average_salary = from_salary * 1.2
    elif to_salary:
        average_salary = to_salary * 0.8
    return average_salary