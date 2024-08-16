Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
misterio = []
type(misterio)
<class 'list'>
len(misterio)
0
>>> misterio.append(16)
>>> misterio.append(32.2)
>>> misterio.append(True)
>>> misterio.append('IFPB')
>>> misterio.append([0]*4)
>>> misterio
[16, 32.2, True, 'IFPB', [0, 0, 0, 0]]
>>> type(misterio)
<class 'list'>
>>> type(misterio[3])
<class 'str'>
>>> type(misterio[4])
<class 'list'>
>>> misterio[4][1] = 4
>>> misterio
[16, 32.2, True, 'IFPB', [0, 4, 0, 0]]
>>> misterio[4]
[0, 4, 0, 0]
