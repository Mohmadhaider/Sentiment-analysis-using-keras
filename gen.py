import csv

cnt = 1
with open('Sentiment Analysis Datasetggvjhv.csv', 'r', encoding = 'utf8') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            #print (row)
            with open('Sentiment Analysis Dataset.csv', 'a', encoding = 'utf8', newline='') as writeFile:
                    writer = csv.writer(writeFile)
                    if type(row[3]) != bytes: 
                        row[3] = row[3].encode('UTF-8')
                    lis = []
                    lis = [cnt,row[1],row[2],row[3]]
                    writer.writerow(lis)
                    
            cnt+=1
            if cnt == 10000001:
                break

csvFile.close()
writeFile.close()
print ("done")
