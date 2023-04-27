'''def palindrome(string):
    n = len(string)
    i = 0
    whie i <= n/2:
        if string[i] == string[-(i+1)]:
           i += 1
        else:
            print("Not a palindrome!")
            exit()
    print("Palindrome!")

palindrome("goog")

house = {"kitchen": 0, "bathroom": 0,"hall_room": 0, "bedroom": 0,"living_room": 0, "office": 0}
def light_switch(room_name):
    if house[room_name] == 0:
        house[room_name] = 1
    else:
        house[room_name] = 0
def where_is_light_on():
    for room in house:
        if house[room] == 1:
            print(room)

def all_lights_off():
    for room in house:
        if house[room] == 1:
            house[room] = 0

light_switch("bedroom")
light_switch("office")
where_is_light_on()
print(house)
all_lights_off()
print(house)'''

def cost(*seconds, price):
    total = 0
    watt = 5                # 1kWh = 1/1000*3600 Ws
    for i in seconds:
        total = total + i
    return (((watt*total/1000)/3600)*price)

c = cost(60, 120, 240, 7535, price=.8)
print(c)
