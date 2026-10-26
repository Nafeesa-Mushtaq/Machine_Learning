passenger = {
    "name": "Nafeesa Mushtaq",
    "fare": 1000.0,
    "age": 20,
}

passenger.update({
    "age": 21,
    "fare": 1200.0
})

if passenger["fare"] < 500:
    print("Low fare")
elif passenger["fare"] < 1000:
    print("Medium fare")
else:
    print("High fare")