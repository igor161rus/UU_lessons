import os, time

path = 'C:/Windows/help'
path_normalized = os.path.normpath(path)
print(path_normalized)

count = 0
for dirpath, dirnames, filenames in os.walk(path_normalized):
    print('*' * 27)
    print(dirpath, dirnames, filenames)
    print(os.path.dirname(dirpath))
    count += len(filenames)
    for file in filenames:
        full_name_path = os.path.join(dirpath, file)
        secs = os.path.getatime(full_name_path)
        file_time = time.gmtime(secs)
        if file_time[0] == 2013:
            print(full_name_path, secs)
print(count)
print(__file__, os.path.dirname(__file__))
