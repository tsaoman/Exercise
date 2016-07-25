def reverse(text):
    length = len(text)
    i = length
    result = "text"
    while (i > 0):
        result[i] = text[length-i]
        i -= 1
    
    return result

print reverse("abcd")