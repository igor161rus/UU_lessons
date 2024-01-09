# -*- coding: utf-8 -*-

print(ord('h'))
print(chr(104))

codes = []
for i in 'привет':
#    print(ord(i))
    codes.append(ord(i))
print(codes)
#codes = [104, 101, 108, 108, 111, ]
out = ''
for i in codes:
    out += chr(i)
print(out)

for code in range(1000, 1200):
    print(code, hex(code), chr(code))

bb = b'\xd1\x84'
print(bb)
print(type(bb))
print(bb[0])
print(hex(bb[0]))
print(bb.count(0xd1))
print(b'he' + b'llo')

print(bin(0xd1))
print(bin(0x84))

code = 0b10001000100
print(code, hex(code))
print(chr(code))

file_name = 'out.txt'
file = open(file_name, mode='w', encoding='utf8')
file_content = 'hello'
file.write(file_content)
file.close()

file_name = 'out.txt'
file = open(file_name, mode='r')
file_content = file.read()
file.close()
print(file_content)