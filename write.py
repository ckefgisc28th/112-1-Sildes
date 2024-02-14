import os

now = "Blender"

f = open(f"./{now}/{now}.txt",mode="r")
urls = f.readlines()
f.close()
print(urls[0])

for i in range(1,15):
    f = open(f"./{now}/Main-{i}.html",mode="w")
    f.write("<!DOCTYPE html>\n")
    f.write('<html lang="en">\n')
    f.write("<head>\n")
    f.write('    <meta http-equiv="refresh" content="0;url='+urls[i-1].split("\n")[0]+'"/>\n')
    f.write("</head>\n")
    f.write("</html>")
    f.close()
    