def index_of_year(year):
    if year>1599 and year<1700:
        return 6
    if year>1699 and year<1800:
        return 4
    if year>1799 and year<1900:
        return 2
    if year>1899 and year<2000:
        return 0
    if year>1999 and year<2100:
        return 6
print("Enter a date:-")
Date = list(input().split("/"))
month = [0,0,3,5,6,1,4,6,2,5,0,3,5]
print(Date)
sumofFive = 0

#1st take last two digits of this year
yr=str(Date[2])
yy1 = int(yr[2:])
print("First item:-",yy1)
sumofFive+=yy1
#2nd item take the int(yy1/4)
yy2 = int(int(yy1)/4)
print("Second item:-" ,yy2)
sumofFive+=yy2

#3rd item date
date = int(Date[0])
sumofFive+=date
print("Date :- ",date)

#4th item value of a particular month
monthValue = month[int(Date[1])]
print("Index value of this month:- ", monthValue)
sumofFive+=monthValue

#5th item value of a particular year
yar = int(Date[2])
yearValue= index_of_year(yar)
print("Index value of this year:- ", yearValue)
sumofFive+=yearValue
print('sumofFive :- ',sumofFive)
rem = (sumofFive%7)
Days = ['Sunday','Monday',"Tuesday",'Wednesday','Thursday','Friday','Saturday']
print("Date :- ",Date[0],"/",Date[1],'/',Date[2],"\t Day :- {}".format(Days[rem]))
