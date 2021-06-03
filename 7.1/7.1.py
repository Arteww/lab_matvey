with open("infile.txt", "r", encoding="UTF-8") as file:
    workers_list = file.readlines()
max_salary_male = 0
name_male = ""
max_salary_female = 0
name_female = ""

for worker in workers_list:
    worker_atr_list = worker.split(" ")
    name = worker_atr_list[0]
    salary = int(worker_atr_list[1])
    sex = worker_atr_list[2].rstrip('\n')
    if sex == "Мужской":
        if max_salary_male < salary:
            max_salary_male = salary
            name_male = name
    else:
        if max_salary_female < salary:
            max_salary_female = salary
            name_female = name
print("Мужчина с самой высокой зарплатой: ", name_male)
print("Женщина с самой высокой зарплатой: ", name_female)
print()

sum_salary_male = 0
count_male = 0
sum_salary_female = 0
count_female = 0

for worker in workers_list:
    worker_atr_list = worker.split(" ")
    salary = int(worker_atr_list[1])
    sex = worker_atr_list[2].rstrip('\n')
    if sex == "Мужской":
        count_male += 1
        sum_salary_male += salary
    else:
        count_female += 1
        sum_salary_female += salary

print("Средняя зарплата мужчин: ", round(sum_salary_male / count_male, 3), "р.")
print("Средняя зарплата женщин: ", round(sum_salary_female / count_female, 3), "р.")