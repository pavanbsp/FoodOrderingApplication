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

def get_hours_minutes_from_time(s):
    hours = 0
    hours += ord(s[0]) - ord('0')
    hours *= 10
    hours += ord(s[1]) - ord('0')
    minutes = 0
    minutes += ord(s[3]) - ord('0')
    minutes *= 10
    minutes += ord(s[4]) - ord('0')
    return (hours,minutes)
