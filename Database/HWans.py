
def findDays(a, b):
    year = int(a.split(' ')[0])
    month = int(a.split(' ')[1])
    date = int(a.split(' ')[2])
    evenMonthDay = 15
    oddMonthday = 13
    daysInYear = (oddMonthday * 7) + (evenMonthDay * 6)
    festivalMonth = int(b.split(' ')[0])
    untilFestivalDay = int(b.split(' ')[1])

    while year % 4 != 1:
        year += 1
    print(year)

    yearDif = year - int(a.split(' ')[0])

    untilFestivalDay += yearDif*daysInYear

    for i in range(1, festivalMonth):
        if(i % 2 == 0):
            untilFestivalDay += evenMonthDay
        else:
            untilFestivalDay += oddMonthday

    for j in range(1, month):
        if(j % 2 != 0):
            untilFestivalDay -= oddMonthday
        else:
            untilFestivalDay -= evenMonthDay

    untilFestivalDay -= date

    return untilFestivalDay

currentDay1 = '2000 12 10'
festivalDay1 = '1 10'

currentDay2 = '1994 4 8'
festivalDay2 = '7 13'
print(findDays(currentDay1, festivalDay1))
