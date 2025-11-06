allNames = []
dict = {}
names = set({})
tracks = set({})

print("Welcome to SMIT TechFest!")
print("Event organized by Lei Villacorta of APPDAET BTCS2\n")

noPartic = int(input("How many participants will register? "))
if noPartic <= 0: exit()

for i in range(noPartic):
    pName = input("\nEnter participant name: ")
    pTrack = input("Enter chosen track: ")
    allNames.append(pName)

    dict[f"Partcipant{i + 1}"] = {
        "Name": pName,
        "Track": pTrack,
    }

print(f"\nRegistered participants:")
for i in range(len(dict)):
    names.add(dict[f'Partcipant{i + 1}']["Name"])
    tracks.add(dict[f'Partcipant{i + 1}']['Track'])
    print(
        f"{i + 1}. {dict[f'Partcipant{i + 1}']['Name']} - {dict[f'Partcipant{i + 1}']['Track']}")

print("\nTracks offered in this event:")
if len(tracks) < 2:
    print("Not enough variety in tracks.")
else:
    print(", ".join(str(i) for i in tracks))

if len(names) < len(allNames):
    print("\nDuplicate names found:")
    check = set()
    duplicates = set()
    for i in allNames:
        if i in check:
            duplicates.add(i)
        check.add(i)

    for i in duplicates:
        print(i)
else:
    print("No duplicate names.")

print("\nParticipants per Track:")
