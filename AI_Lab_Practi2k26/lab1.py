#A simple reflex Agent - Vaccum cleaner world
# Taking input from Users
room_A = input('Enter status of room A (Dirty/Clean): ').lower()
room_B = input('Enter status of room B (Dirty/Clean): ').lower()

#Initial Position of a Vaccum Cleaner
position = "A"

print("\nVaccum cleaner started")

#Agent checks and ceans both the rooms
while True:
    if position == "A":
        if room_A == "Dirty":
            print("Room A is Dirty --> Cleaning Room A, please wait")
            room_A = "Clean"
        else:
            print("Room A is Clean --> Move to Room B")
            position == "B"

    elif position == "B":
        if room_B == "Dirty":
            print("Room B is Dirty --> Cleaning Room B, please wait")
            room_B = "Clean"
        else:
            print("Room B is Clean --> Task is Completed")
            break
    break

print("\nFinal Status")
print("Room A:", room_A)
print("Room B:", room_B)
print("\nBoth the Rooms are cleaned now.")
print("\n=====================Thank--You=================")