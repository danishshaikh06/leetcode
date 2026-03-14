# valid paranthesis

def valid (str):
  stack = []

  for i in range (len(str)):
    if str[i] == '(' or str[i] == '[' or str[i] == '{':
      stack.append(str[i])

    else:
      if not stack:
        return False

      if stack[-1] == '(' and str[i] == ')' or stack[-1] == '[' and str[i] == ']' or stack[-1] == '{' and str[i] == '}':
        stack.pop()

      else:
        return False 
  return len(stack) == 0 

