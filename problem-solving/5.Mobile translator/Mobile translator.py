n = int(input())
eng = dict()
fr = dict()
ger = dict()
for i in range(0,n):
    info = input().split()
    this_word = info[0]
    eng[info[1]] = this_word
    fr[info[2]] = this_word
    ger[info[3]] = this_word

#print(eng)
#print(fr)
#print(ger)

sen = input().split()

for i in range(0,len(sen)):
    if sen[i] in eng:
        sen[i] = eng[sen[i]]
    elif sen[i] in fr:
        sen[i] = fr[sen[i]]
    if sen[i] in ger:
        sen[i] = ger[sen[i]]
out = str()
for i in sen:
    out += i
    out += ' '
out = out.strip()
print(out)