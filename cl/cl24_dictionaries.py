"""Examples of set and dictionary syntax"""

pids: set[int] = {710000000, 712345678}
pids.add(730569281)

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

ice_cream["vanilla"] += 110


if mint in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint")

for flavor in ice_cream:
    print(flavor)
    print(ice_cream[flavor])
