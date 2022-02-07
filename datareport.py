import csv
import json
import os

class DataReport:
    def __init__(self, csvdata):
        with open(csvdata, 'r') as csvfile:
            data = [d for d in csv.reader(csvfile)]
            self.column = data[0]
            self.data = data[1:]
            self.type = {}

    def gettype(self):
        # SQLite資料型態
        self.type = {}
        with open('type.json', 'r') as t:
            p = json.load(t)
            for i in range(len(self.column)):
                if self.column[i] in p:
                    print(self.column[i], p[self.column[i]])
                    self.type[self.column[i]] = p[self.column[i]]

    def show(self, max=10):
        print(self.column)
        print((self.data)[0:max])




print(os.listdir('Data'))
data = DataReport(f'Data/{os.listdir("Data")[2]}/DataRecord-0001.csv')
data.gettype()
print(data.type)
data.show(3)