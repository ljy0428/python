fr = open('/Users/jeongyeon/Backup/Data/Repository/github_ljy0428_python/python/Algorithm/read.txt', 'r', encoding='utf-8')

fw = open('/Users/jeongyeon/Backup/Data/Repository/github_ljy0428_python/python/Algorithm/write.txt', 'w', encoding='utf-8', newline='')

for val in fr:
    fw.write(val)

fr.close()

fw.close()
