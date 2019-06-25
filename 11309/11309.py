import sys

def wolfgang():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        time = sys.stdin.readline().strip()
        time = time.split(':')
        hour = time[0]
        minute = time[1]

        for m in range(24*60):
            if int(minute) == 59:
                minute = "00"
                if int(hour) == 23:
                    hour = "00"
                else:
                    hour = str(int(hour) + 1)
                    if len(hour) == 1:
                        hour = "0" + hour
            else:
                minute = str(int(minute)+ 1)
                if len(minute) == 1:
                    minute = "0" + minute
            if hour == "00":
                tm = str(int(minute))
            else:
                tm = str(int(hour)) + minute

            if palindrom(tm):
                print(hour+":"+minute)
                break

def palindrom(string):
    revstr = ""
    for i in range(len(string)-1, -1, -1):
        revstr += string[i]
    if revstr == string:
        return True
    return False

def main():
    wolfgang()

if __name__ == "__main__":
    main()