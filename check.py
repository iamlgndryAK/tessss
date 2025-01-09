import os
import time

def check_internet():
    response = os.system("ping -n 1 8.8.8.8 > nul 2>&1")
    return response == 0

def main():
    while True:
        if check_internet():
            print("working")
        else:
            print("not working")
        time.sleep(1)

if __name__ == "__main__":
    main()
