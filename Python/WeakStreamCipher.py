key = "password" #key (string)
bits = "0 1" #plaintext (string)

#bit decoding map
dmap = {
'0':'A',
'1':'B'
}

#bit encoding map
emap = {v: i for i, v in dmap.items()}

#encodes/decodes text
def charmap(text,dic):
    s = text.split()
    ans = []

    for item in s:
        ans.append(dic.get(item,item))

    return " ".join(ans)

def encode(text):
    return charmap(text,emap)

def decode(text):
    return charmap(text,dmap)



#XOR key with bits
