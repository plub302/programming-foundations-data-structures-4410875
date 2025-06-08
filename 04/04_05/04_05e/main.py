def has_unique_characters(data):
    unique_set = set(data)
    print(unique_set)
    if len(data) == len(unique_set):
        return True
    else:
        return False

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
