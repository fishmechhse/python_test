##A (10). Контест
##Ограничение времени	1 секунда
##Ограничение памяти	64.0 Мб
##Ввод	стандартный ввод или input.txt
##Вывод	стандартный вывод или output.txt
##Попробуйте представить, что вы участвовали в разработке Яндекс Контеста.
# Помогите посчитать результаты тестирования!
##
##Формат ввода
##Вводится число N - число посылок в контест от студентов.
# Далее вводится N строк: Фамилия студента, номер задачи и вердикт Яндекс контеста через пробел.
# Задача считается сданной, если получила вердикт "OK".
# Студент мог сдавать задачу несколько раз: если хотя бы одна попытка получила вердикт "ОК", задача считается сданной.
##
##Формат вывода
##Информация о каждом студенте: фамилия, количество отправленных посылок, количество сданных задач.
# Студенты должны быть отсортированы в алфавитном порядке.
##
##Пример 1
##Ввод	Вывод
##10
##Ivanov 1 WA
##Petrov 2 WA
##Ivanov 3 CE
##Ivanov 1 OK
##Petrov 3 OK
##Ivanov 3 OK
##Ivanov 2 OK
##Sidorov 3 OK
##Sidorov 3 OK
##Sidorov 3 CE
##

source_file = open('input.txt', 'r')
n = source_file.readline().strip()  # read N == 10
users = dict()
OK_TASK = "ok_task"
TOTAL_TASK = "total_task"
for line in source_file:
    user_commit = line.split()
    profile = users.get(user_commit[0])
    if profile is None:
        profile = {
            TOTAL_TASK: 0,
            OK_TASK: {
            },
        }
    if user_commit[2] == "OK":
        profile[OK_TASK][user_commit[1]] = None
    profile[TOTAL_TASK] = profile[TOTAL_TASK] + 1
    users[user_commit[0]] = profile

source_file.close()

for key, value in sorted(users.items()):
    profile = users[key]
    print ("%s %s %s" % (key, profile[TOTAL_TASK], len(profile[OK_TASK])))

