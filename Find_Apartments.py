def apt_search1(city, max_rent, min_beds, pets_allowed):
    if pets_allowed:
        pet_string = " that allow pets. "
    else:
        pet_string = " "
    print(f"Welcome to the GC Property! Looking up listings in {city} for {min_beds} bedroom apartments{pet_string}All within a budget of ${max_rent}")

apt_search1("Atlanta", 2000, 1, True)
apt_search1("Walla", 1500, 1, False)

def apt_search2(city, max_rent, min_beds=1, pet_allowed=False):
    if pet_allowed:
        pet_string = "that allows pets. "
    else:
        pet_string = " "
    print(f"Welcome to the GC Property! Looking up listings in {city} for {min_beds} bedroom apartments{pet_string}All within a budget of ${max_rent}")



apt_search2("Detroit", 1440)
apt_search2("Allen Park", 1450, 2)
apt_search2("Detroit", 1250, pet_allowed=True)

plus_one_hundred = lambda character_value: character_value + 100
square_num = lambda character_value: character_value * character_value
concatenate = lambda character_value: "- " + character_value
divide_by_three = lambda character_value: character_value / 3

print(plus_one_hundred(30))
print(square_num(4))
print(concatenate("hello"))
print(divide_by_three(9))


