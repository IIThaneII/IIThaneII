with open("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/6_day(26-30)/data_overlap/file1.txt") as f1:
    a = [int(num) for num in f1.readlines()]
with open("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/6_day(26-30)/data_overlap/file2.txt") as f2:
    b = [int(num) for num in f2.readlines()]

c = [num for num in a if num in b]
print(c)