import csv
import dsv

data = [
    ['Name', 'Comment'],
    ['Alice', 'She said, "Hello" and waved']
]

with open('/tmp/data.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL, escapechar='\\')
    writer.writerows(data)

with open('/tmp/data.csv', 'r') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)


data1 = [
    ['Name', 'Score'],
    ['Alice', 100]
]

print("------------------------------------------------------------")

with open('/tmp/data.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(data1)

with open('/tmp/data.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)

print("------------------------------------------------------------")


with open('/tmp/data.csv', 'w', newline='\r\n') as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open('/tmp/data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("------------------------------------------------------------")

data = [
    ['Name', 'Comment'],
    ['Bob', 'This is a multi-line comment\r\nspanning two lines.']
]

with open('/tmp/data.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar='\\')
    writer.writerows(data)

with open('/tmp/data.csv', 'r', newline='') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_NONE, escapechar='\\')
    for row in reader:
        print(row)

print("------------------------------------------------------------")


data_new = [
    ['Name', 'Comment'],
    ['Alice', 'She said, "Hello" and waved.'],
    ['Bob', 'This is a multi-line comment\r\nspanning two lines.'],
    ['Charlie', 'More fun with\ntwo lines.'],
    ['Diana', 'How about some UTF-8: café, naïve, résumé. 📝'],
    ['Edward', 'アップル'],
]

writer = dsv.DSVWriter('/tmp/data.csv')
writer.write(data_new)

reader = dsv.DSVReader('/tmp/data.csv')
reader.read()


