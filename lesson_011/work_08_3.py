import sys
from pprint import pprint

# pprint(dir(sys))

print(sys.executable)
print(sys.version)
print(sys.version_info)
print(sys.version_info, type(sys.version_info))

print(sys.argv)
print(sys.path)
print(sys.modules)
print(type(sys.modules), sys.modules)
# for k, v in sys.modules.items():
#     print(k, type(v), v)
for k, v in sys.modules.items():
    print(k, type(v), v, dir(v))

print(__builtins__)
pprint(dir(__builtins__))