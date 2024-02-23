import os
path = './cache/text.txt'
# open in readable and writable
with open(path,"r+") as f:
    s = f.read()
    i = int(s)
    print(i)
    # delete content in text.txt
    f.seek(0)
    f.truncate()
    f.write(str(++i))
    f.flush()
    f.close()