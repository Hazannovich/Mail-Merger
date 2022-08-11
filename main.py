
with open("./Input/Letters/starting_letter.txt") as temp:
    with open("./Input/Names/invited_names.txt") as names_data:
        for name in names_data.readlines():
            with open(f"./Input/Letters/letter_for_{name.strip()}", 'w') as letter:
                for line in temp.readlines():
                    new_line = line.replace("[name]", name.strip())
                    letter.write(new_line)
            temp.seek(0)
