'''Given a whether the substring is palnidrome or not
   only check for alphanumeric values that are a-z, A-Z, 0-9
   If any other string found rather than alphanumeric dont count it move ahead'''

def valid_palindrome(substring: str, part: str):
    position = []
    start = 0 
    while (len(substring) > 0):
        search = substring.find(part, start)
        position.append(search)

    return position

substring = 'abcdefabcefg'
part = 'abc'

valid_palindrome(substring, part)



        
