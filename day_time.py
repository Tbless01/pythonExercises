day = int(input("Enter today's day(1-7): "))
elapse_day = int(input("Enter the number of days elapse since today(1-31): "))
match day:
            case 0:
                print("Today is Sunday ")
            case 1:
                print("Today is Monday ")
            case 2:
                print("Today is Tuesday ")
            case 3:
                print("Today is Wednesday ")
            case 4:
                print("Today is Thursday ")
            case 5:
                print("Today is Friday ")
            case 6:
                print("Today is Saturday ")
            case unknown_command:
                print("Unknown ")
match elapse_day:
            case 0 | 7 | 14 | 21 | 28:
                print("and the future day is Sunday")
            case 1 | 8 | 15 | 22 | 29:
                print("and the future day is Monday")
            case 2 | 9 | 16 | 23 | 31:
                print("and the future day is Tuesday")
            case 3 | 10 | 17 | 24:
                print("and the future day is Wednesday")
            case 4 | 11 | 18 | 25:
                print("and the future day is Thursday")
            case 5 | 12 | 19 | 26:
                print("and the future day is Friday")
            case 6 | 13 | 20 | 27:
                print("and the future day is Saturday")
            case unknown_command:
                print("Unknown")
