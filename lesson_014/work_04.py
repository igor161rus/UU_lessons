deep_ocean = 'Ocean, oocan, ocean, off, aaaa, Nemo, nemo, mimo, NEMO, nEmo'
nemo = r'[Nn]em\w{,2}'
import re

matched = re.search(nemo, deep_ocean)
print(matched)
matched = re.match(nemo, deep_ocean)
print(matched)

# print(matched.group())
# print(matched.start())
# print(matched.end())
# print(matched.span())
print('*' * 20, end='\n\n')

srch_iter = re.finditer(nemo, deep_ocean)
for matched in srch_iter:
    print(matched)

full_srch = re.findall(nemo, deep_ocean)
print(full_srch)

final_matched = re.search('Nemo', deep_ocean)
print(final_matched)
print(final_matched.start())
print(final_matched.end())
print('*' * 20, end='\n\n')

transparent = re.sub(r'[Oo]\w{4}', '', deep_ocean)
print(transparent)
cleared = re.sub(r'[Oo]\w{4}\s+', '', deep_ocean)
print(cleared)


