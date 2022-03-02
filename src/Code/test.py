




fileObj = open('src/Maps/AW.txt', "r")
words = fileObj.read().splitlines()
for i, line in enumerate(words):
    words[i] = line.split('\t')
fileObj.close()
print(words)