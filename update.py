from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d %I:%M %p")

newline = input()
with open('log.txt','r+') as f:
    lines = f.readlines()
    f.seek(0)
    f.write(today)
    f.write(" - ")
    f.write(newline)
    f.write("\n")
    for x in lines[:-1]:
        f.write(x)
    f.truncate()
