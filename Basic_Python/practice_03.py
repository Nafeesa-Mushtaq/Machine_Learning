passenger = {
    "name": "Nafeesa Mushtaq",
    "fare": 1000.0,
    "age": 20,
}

print(passenger.items())
print(passenger.pop("fare"))
print(passenger.get("fare", 0))
passenger.update({
    "age": 21,
    "fare": 1200.0
})

print(passenger.items())