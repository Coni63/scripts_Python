import string
import random
from time import time
import xlsxwriter

workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', "Test")
worksheet.write('B1', "Size of text")
worksheet.write('C1', "time to generate file")
worksheet.write('D1', "duration with len")
worksheet.write('E1', "duration with loop")

for i in range(1, 51):
    with open('test.txt', 'w+') as file:
        start = time()
        for _ in range(10000*i):
            file.write(random.choice(string.ascii_letters))
        duration = (time()-start)*1000
        #print("time to generate the file %s ms" % (duration))

    with open('test.txt', 'r') as file2:
        txt = file2.read()
        start = time()
        l = len(txt)
        duration2 = (time() - start) * 1000
        print("%s characters found in %s ms" % (l, duration2))

        start = time()
        l = 0
        for char in txt:
            l+=1
        duration3 = (time() - start) * 1000
        print("%s characters found in %s ms" % (l, duration3))

    worksheet.write('A' + str(i+1), i)
    worksheet.write('B' + str(i+1), 10000*i)
    worksheet.write('C' + str(i+1), duration)
    worksheet.write('D' + str(i+1), duration2)
    worksheet.write('E' + str(i+1), duration3)

workbook.close()