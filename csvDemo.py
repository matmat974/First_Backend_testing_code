import csv


with open('utilities/loanApp.csv') as csvFile:
    csvReader = csv.reader(csvFile)


    # print(csvReader)
    # print(list(csvReader))

    name = []
    status = []

    for row in csvReader:
        name.append(row[0])
        status.append(row[1])


print(name)
print(status)

nameIndex = name.index('Ram')
loanStatus = status[nameIndex]
print('Ram loanStatus is '+loanStatus)



with open('utilities/loanApp.csv', 'a') as wFile:
    csvWrite = csv.writer(wFile)
    csvWrite.writerow(["Bob","Rejected"])
    # Other method to write
    # csvWrite = csv.writer(wFile).writerow(["Bob","Rejected"])