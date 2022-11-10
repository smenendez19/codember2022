import re

users_data_raw = []
users_dict = []
users_valid = 0

users_columns = {
    "usr": None,
    "eme": None,
    "psw": None,
    "age": None,
    "loc": None,
    "fll": None,
}

with open("users.txt", "r") as users_file:
    user = ""
    for line in users_file:
        if line == "\n":
            users_data_raw.append(user)
            user = ""
            continue
        user += line.replace("\n", " ")

user_name = None

for row in users_data_raw:
    user = users_columns.copy()

    regex_usr = re.search(r"usr:(@\w+)", row)
    if regex_usr:
        user_name = regex_usr.group(1)
        user["usr"] = user_name
    else:
        continue

    regex_eme = re.search(r"eme:([\w\d]+@[\w]+\..+)(?=\ )", row)
    if regex_eme:
        user_email = regex_eme.group(1)
        user["eme"] = user_email
    else:
        continue

    regex_psw = re.search(r"psw:(.+)(?=[\ ]*)", row)
    if regex_psw:
        user_password = regex_psw.group(1)
        user["psw"] = user_password
    else:
        continue

    regex_age = re.search(r"age:(\d+)", row)
    if regex_age:
        user_age = regex_age.group(1)
        user["age"] = user_age
    else:
        continue

    regex_loc = re.search(r"loc:(\w+)", row)
    if regex_loc:
        user_location = regex_loc.group(1)
        user["loc"] = user_location
    else:
        continue

    regex_fll = re.search(r"fll:(\d+)", row)
    if regex_fll:
        user_followers = regex_fll.group(1)
        user["fll"] = user_followers
    else:
        continue

    users_dict.append(user)
    users_valid += 1

print(str(users_valid) + user_name)
