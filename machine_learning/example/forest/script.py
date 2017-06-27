import csv


class Entry:
    instances = []
    def __init__(self, arg):
        self.X = int(arg[0])
        self.Y = int(arg[1])
        self.month = dict_month[arg[2]]
        self.day = dict_day[arg[3]]
        self.FFMC = float(arg[4])
        self.DMC = float(arg[5])
        self.DC = float(arg[6])
        self.ISI = float(arg[7])
        self.temp = float(arg[8])
        self.RH = int(arg[9])
        self.wind = float(arg[10])
        self.rain = float(arg[11])
        self.area = float(arg[12])
        self.instances.append(self)

    def __repr__(self):
        return "[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]".format(\
                self.X, self.Y, self.month, self.day, self.FFMC, self.DMC,
                self.DC, self.ISI, self.temp, self.RH, self.wind, self.rain, self.area)


dict_month = {"jan": 1,"feb": 2,"mar": 3,"apr": 4,"may": 5,"jun": 6,"jul": 7,"aug": 8,"sep": 9,"oct": 10,"nov": 11,"dec": 12}
dict_day = {"mon": 1,"tue": 2,"wed": 3,"thu": 4,"fri": 5,"sat": 6,"sun": 7}

with open('forestfires.csv', 'r') as csvfile:
    #csvfile.next() #delete header
    content = csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(content):
        if i > 0:
            print(Entry(row))
        else:
            pass