user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    keys = list(user_pref.keys())
    return {keys[0],keys[1],keys[3]}


print(user_preferences)
print(update_preferences(user_preferences))
