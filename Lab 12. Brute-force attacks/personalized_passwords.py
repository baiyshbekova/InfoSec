name = "Alex"
surname = "Smith"
birth_year = "2001"
number = "7"

candidates = {
    name,
    name.lower(),
    surname,
    surname.lower(),
    name + birth_year,
    name.lower() + birth_year,
    surname + birth_year,
    name + number,
    name.lower() + number,
    name + surname,
    name.lower() + surname.lower(),
    birth_year + number,
}

with open("personalized_passwords.txt", "w") as file:
    for password in sorted(candidates):
        file.write(password + "\n")

print(f"Generated {len(candidates)} password candidates.")
