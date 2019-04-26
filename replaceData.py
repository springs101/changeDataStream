import codecs

def readfile():
    file = codecs.open("E:\\test.sql",'r','utf-8')
    file1 = codecs.open("E:\\test_new.sql", 'a', 'utf-8')
    while 1:
        try:
         lines = file.readlines(100000)
         if not lines:
             break
         for line in lines:
             line.strip()
             if line.startswith("INSERT"):
                 if not line.endswith(")\n"):
                    lineobj=line.replace("\n", "").replace("\r", "").replace("\r\n","")
                    file1.write(lineobj)
                 else:
                     file1.write(line)

        except Exception as err:
         print(err)

if __name__ == '__main__':
    readfile()