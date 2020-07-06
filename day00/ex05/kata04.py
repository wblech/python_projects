t = (0, 4, 132.42222, 10000, 12345.67)

day = t[0] if t[0] >= 10 else "0" + str(t[0])
ex = t[1] if t[1] >= 10 else "0" + str(t[1])

message = f"day_{day}, ex_{ex} : {t[2]:.2f}, {t[3]:.2e}, {t[4]:.2e}"

print(message)
