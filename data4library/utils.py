DISALLOW_CAMEL_CASES = {

}

def to_camel_case(s):
    if s in DISALLOW_CAMEL_CASES:
        return s

    result = []
    idx = 0
    while idx < len(s):
        if s[idx] == '_':
            idx += 1
            result.append(s[idx].upper())
        else:
            result.append(s[idx])
        idx += 1

    return ''.join(result)
