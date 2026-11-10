full_blood_types = {
    "A positive": 0,
    "A negative": 0,
    "B positive": 0,
    "B negative": 0,
    "AB positive": 0,
    "AB negative": 0,
    "O positive": 0,
    "O negative": 0
}

letter_types = {
    "A": 0,
    "B": 0,
    "AB": 0,
    "O": 0
}

rh_types = {
    "positive": 0,
    "negative": 0
}

with open("bloodtypes.txt", "r") as file:
    for line in file:
        blood_types = line.split()

        for i in range(0, len(blood_types), 2):
            letter = blood_types[i]
            rh = blood_types[i + 1]

            full_type = letter + " " + rh

            # Count full blood types
            full_blood_types[full_type] += 1

            # Count letter blood types
            letter_types[letter] += 1

            # Count Rh factor
            rh_types[rh] += 1

# Print results
print("Full Blood Types:")
for blood_type, count in full_blood_types.items():
    print(blood_type, ":", count)

print("\nBlood Types Without Rh Factor:")
for blood_type, count in letter_types.items():
    print(blood_type, ":", count)

print("\nRh Factor:")
for rh, count in rh_types.items():
    print("Rh", rh, ":", count)
