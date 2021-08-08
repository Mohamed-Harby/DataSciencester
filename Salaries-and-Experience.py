from collections import defaultdict

# predicts average salary for each tenture bucket
# ---simple linear regression

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
    tenure: sum(salary_by_tenure[tenure]) / len(salary_by_tenure[tenure])
    for tenure in salary_by_tenure
    }


def tenture_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "less than five"
    else:
        return "more than five"


salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenture_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)
    
average_salary_by_bucket = {
    bucket: sum(salaries) / len(salaries)
    for bucket, salaries in salary_by_tenure_bucket.items()
    }

print(average_salary_by_bucket)

# output
# {'more than five': 79166.66666666667, 'less than two': 48000.0, 'less than five': 61500.0}



# predicts which users use paid accounts
# ---simple logistic regression
def predict_paid_or_unpaid(years_experience):
  if years_experience < 3.0:
    return "paid"
  elif years_experience < 8.5:
    return "unpaid"
  else:
    return "paid"
  
  
