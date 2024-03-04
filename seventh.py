""" 
Define a structure data type TRAIN_INFO. The type contain Train No.: integer type
Train name: string Departure Time: aggregate type TIME Arrival Time: aggregate type
TIME Start station: string End station: string The structure type Time contains two integer

members: hour and minute. Maintain a train timetable and implement the following
operations:
(i) List all the trains (sorted according to train number) that depart from a particular station.
(ii) List all the trains that depart from a particular station at a particular time.
(iii) List all he trains that depart from a particular station within the next one hour of a given
time.
(iv) List all the trains between a pair of start station and end station.

Trains(different class)
Timetable(different class)(only for a day)
23456 - arrival [13,00] departure [13,10]
{23456 : [[13,00],[13,10]]}
multiple trains can have same arrival and departure time,
dictionary = 
"""
class Train:
    def __init__(self,number : int,name : str, departure: list, arrival:list, strstation: str ,endstation: str):
        self.number,self.name,self.departure,self.arrival,self.strstation,self.endstation=number,name,departure,arrival,strstation,endstation
class TimeTable:
    def __init__(self):
        self.chart =dict()
        self.stationchart=dict()
    def addTrain(self,number : int,name : str, departure: list, arrival:list, strstation: str ,endstation: str):
        new_Train = Train(number,name,departure,arrival,strstation,endstation)
        self.chart[number]=new_Train
        if strstation not in self.stationchart:
            self.stationchart[strstation]=[number]
        else:
            self.stationchart[strstation].extend(number)
    def sameDeparture(self,station):
        if station not in self.stationchart:
            print("No Trains from this station")
        else:
            self.stationchart[station].sort()
            for i in range(len(self.stationchart[station])):
                print(self.stationchart[station][i],end=" ")
    def sameDepartureSameTime(self,station,time: list):
        if station not in self.stationchart:
            print("No Trains from this station.")
        else:
            self.stationchart[station].sort()
            for i in range(len(self.stationchart[station])):
                if self.chart[self.stationchart[station][i]].departure==time:
                    print(self.chart[self.stationchart[station][i]].name,end="\t")
    def onehourDiff(self,station,time: list):
        if station not in self.stationchart:
            print("No Trains from this station.")
        else:
            self.stationchart[station].sort()
            for i in range(len(self.stationchart[station])):
                temptime=self.chart[self.stationchart[station][i]].departure
                hour=(temptime[0]-time[0])*60
                minu=(temptime[1]-time[1])
                if hour+minu<=60:
                    print(self.chart[self.stationchart[station][i]].name,end="\t")
    def startendpair(self,sta1,sta2):
        flag=0
        for element in self.chart:
            if self.chart[element].strstation==sta1 and self.chart[element].endstation==sta2:
                print(self.chart[element].name,self.chart[element].number)
                flag=1
        if not flag:
            print("No trains between this station pair.")
test=TimeTable()
test.addTrain(12345,"Train1",[8,00],[12,00],"Station A","Station X")
test.addTrain(23456, "Train2", [9,30], [13,30], "Station B", "Station Y")
test.addTrain(34567, "Train3", [10,45], [15,00], "Station C", "Station Z")
test.addTrain(45678, "Train4", [12,15], [16,30], "Station D", "Station X")
test.addTrain(56789, "Train5", [14,00], [18,00], "Station E", "Station Y")
test.addTrain(67890, "Train6", [15,30], [19,45], "Station F", "Station Z")
test.addTrain(78901, "Train7", [16,45], [21,00], "Station G", "Station X")
test.addTrain(89012, "Train8", [18,00], [22,15], "Station H", "Station Y")
test.addTrain(90123, "Train9", [19,30], [23,45], "Station I", "Station Z")
test.addTrain(10111, "Train10", [21,00], [1,00], "Station J", "Station X")
def menu():
    print("1. List all trains departing from a particular station.")
    print("2. List all trains departing from a particular station at a particular time.")
    print("3. List all trains departing from a particular station within the next one hour of a given time.")
    print("4. List all trains between a pair of start and end station.")
    print("5. Exit")
while True:
    menu()
    choice = input("Enter your choice: ")

    match choice:
        case '1':
            station = input("Enter the station name: ")
            print("Trains departing from", station)
            test.sameDeparture(station)
        case '2':
            station = input("Enter the station name: ")
            time = input("Enter the departure time (HH:MM): ").split(':')
            time = [int(x) for x in time]
            print("Trains departing from", station, "at", ":".join(map(str, time)))
            test.sameDepartureSameTime(station, time)
        case '3':
            station = input("Enter the station name: ")
            time = input("Enter the reference time (HH:MM): ").split(':')
            time = [int(x) for x in time]
            print("Trains departing from", station, "within the next one hour of", ":".join(map(str, time)))
            test.onehourDiff(station, time)
        case '4':
            start_station = input("Enter the start station: ")
            end_station = input("Enter the end station: ")
            print("Trains between", start_station, "and", end_station)
            test.startendpair(start_station, end_station)
        case '5':
            print("Exiting...")
            break
        case _:
            print("Invalid choice. Please try again.")