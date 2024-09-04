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

