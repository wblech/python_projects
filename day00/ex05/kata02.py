t = (3, 30, 2019, 9, 25)


day = t[3] if t[3] >= 10 else "0" + str(t[3])
month = t[4] if t[4] >= 10 else "0" + str(t[4])
year = t[2]
hour = t[0] if t[0] >= 10 else "0" + str(t[0])
minutes = t[1] if t[1] >= 10 else "0" + str(t[1])

message = f"{day}/{month}/{year} {hour}:{minutes}"
print(message)
