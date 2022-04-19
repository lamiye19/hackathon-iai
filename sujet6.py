import datetime
def calculDate(n):
    a = datetime.date.today()
    b = datetime.datetime.toordinal(a)+n

    print(datetime.date.fromordinal(b))


if __name__ == '__main__':
    n = int(input())

    calculDate(n)