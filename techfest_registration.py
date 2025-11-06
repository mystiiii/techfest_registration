dict ={}

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
print(f"Registered participants")
for i in range(len(dict)):
    print(f"{i+1}. {dict[f'Partcipant{i+1}']['Name']} - {dict[f'Partcipant{i+1}']['Track']}")