from collections import deque

def check_matching_parentheses(string):
  count_open = 0
  count_closed = 0

  for char in string:
    if char == '(':
      count_open = count_open + 1
    elif char == ')':
      count_closed = count_closed +1
    
  if count_closed == count_open:
    return True
  else:
    return False

print(check_matching_parentheses("()"))
print(check_matching_parentheses("(hi there)"))
print(check_matching_parentheses("(hell)o"))
print(check_matching_parentheses("((linkedin)) learning"))

print(check_matching_parentheses("(hi(there"))
print(check_matching_parentheses("()ok)"))
print(check_matching_parentheses("((increment)"))
print(check_matching_parentheses(")linkedin()("))