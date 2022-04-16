def check_length_less_than(name, n):
    return len(name) <= n

def check_alphabets(s):
    for x in s:
        if((ord(s)>=ord('a') and ord(s)<=ord('z')) or (ord(s)>=ord('A') and ord(s)<=ord('Z'))):
            continue
        return False
    return True

def is_numeric(s):
    for x in s:
        if ((ord(x)) >= ord('0') and ord(x)<=ord('9')):
            continue
        return False
    return True
