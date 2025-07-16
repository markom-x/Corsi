months = {
    "January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
}
while True:
    listen = input("Date: ").split('/')
    try:
        y = int(listen[2])
        m = int(listen[0])
        d = int(listen[1])
        if d <= 31 and m <= 12:
            if m < 10:
                m = f"0{m}"
            if d < 10:
                d = f"0{d}"
            print(y, m, d, sep='-')
            break
        else:
            continue
    except IndexError:
        l = str(listen[0]).split(' ')
        if "," in l[1]:
            try:
                y = int(l[2])
                m = l[0]
                d = int(l[1].removesuffix(','))
                if d <= 31:
                    if d < 10:
                        d = f"0{d}"
                    if m in months:
                        print(y, months[m], d, sep='-')
                        break
                else:
                    continue
            except:
                continue
        else:
            continue
    except:
        continue




