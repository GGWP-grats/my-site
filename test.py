n = int(input())
hrs = 0;
mins = 0;

while n != 0:
    n -= 1
    mins++
    if mins == 60:
        mins = 0;
        hrs++;
    if hrs == 24:
        hrs = 0
    if n == 0:
        print(hrs, mins)
