/*
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
*/
#include<bits/stdc++.h>
using namespace std;
class Train{
    public:
        int number,arrival[2],departure[2];
        string name,strstation,endstation;
    Train(int number,int arrival[2],int departure[2],string name,string strstation,string endstation){
        this->number=number;
        this->arrival[2]=arrival[2];
        this->departure[2]=departure[2];
        this->name=name;
        this->strstation=strstation;
        this->endstation=endstation;
    }
};
class TimeTable{
    public:
        map<int,Train> chart;
    void addTrain(int number,int arrival[2],int departure[2],string name,string strstation,string endstation)
    {
        Train new_Train(number,arrival,departure,name,strstation,endstation);
        chart.insert({number,new_Train});
    }
};
int main()
{
    TimeTable tt;
    int arri[]={13,0};
    int dep[]={13,10};
    tt.addTrain(23456,arri,dep,"Kinshuk","Kinshuk","Thapa");
}