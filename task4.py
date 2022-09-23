
def zip(a):
    enco = ''
    i = 0
    while i < len(a):
        count = 1
        while i + 1 < len(a) and a[i] == a[i + 1]:
            count += 1
            i += 1
        enco += str(count) + a[i]
        i += 1
    return enco


textt = 'AAAAAABBBAAAAB'
print(zip(textt))


def zap(a):
    deco = ""
    i = 0
    j = 0
    while (i <= len(a) - 1):
        run_count = int(a[i])
        run_word = a[i + 1]
        for j in range(run_count):           
            deco = deco+run_word
            j = j + 1
        i = i + 2
    return deco


a = "6A3B4A1B"
print(zap(a))
