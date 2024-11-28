import json


def merge_user_data(users, updates):
    user_dict = {user["name"]: user for user in users}
    for update in updates:
        name = update["name"]
        if name not in user_dict:
            user_dict[name] = update
        else:
            for key, value in update.items():
                if key != "name":
                    if key in user_dict[name]:
                        user_dict[name][key] = max(user_dict[name][key], value)
                    else:
                        user_dict[name][key] = value
    for name in user_dict:
        user_dict[name].pop("name", None)
    return user_dict


def main():
    users_file = input()
    updates_file = input()
    with open(users_file, 'r', encoding='utf-8') as ufile:
        users = json.load(ufile)
    with open(updates_file, 'r', encoding='utf-8') as ufile:
        updates = json.load(ufile)
    updated_data = merge_user_data(users, updates)
    with open(users_file, 'w', encoding='utf-8') as ufile:
        json.dump(updated_data, ufile, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
