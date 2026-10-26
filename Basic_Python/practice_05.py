fares = [200, 500, 850, 1000, 1200]

for items in fares:
    if items < 500:
        print("Low fare")
    elif items < 1000:
        print("Medium fare")
    else:
        print("High fare")
        