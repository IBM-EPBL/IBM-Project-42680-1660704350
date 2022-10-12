x = input("Enter value: ");
stop_light = int(x)
while True:
    if stop_light >= 1 and stop_light < 15:
        print('Green light')
        stop_light += 1
    elif stop_light < 25:
        print('Yellow light')
        stop_light += 1
    elif stop_light < 40:
        print("Red light")
        stop_light += 1
    else:
        stop_light = 0
    break;
