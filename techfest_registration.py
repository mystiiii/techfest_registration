dict = {}
tracks = set({})

print("Welcome to SMIT TechFest!")
print("Event organized by Lei Villacorta of APPDAET BTCS2\n")

noPartic = int(input("How many participants will register? "))
if noPartic <= 0: exit()

for i in range(noPartic):
    pName = input("\nEnter participant name: ")
    pTrack = input("Enter chosen track: ")

    dict[f"Partcipant{i+1}"] = {
        "Name": pName,
        "Track": pTrack,
    }

print(f"\nRegistered participants")
for i in range(len(dict)):
    tracks.add(dict[f'Partcipant{i+1}']['Track'])
    print(f"{i+1}. {dict[f'Partcipant{i+1}']['Name']} - {dict[f'Partcipant{i+1}']['Track']}")

print("\nTracks offered in this event: ")
if len(tracks) < 2:
    print("Not enough variety in tracks.")
else:
    print(", ".join(str(i) for i in tracks))