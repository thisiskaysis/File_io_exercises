import csv

# KAYCEE'S WAY
# This way works but may not the best way to do it?? It makes sense to me but how much sense does it make to others
# This way takes the row that is == colour_name("Android Green") and appends it to a list chosen_colour. Then I access the HEX and English values from that list.
# The row "Android Green" information gets stored as a dictionary within chosen_colour list.
# So chosen_colour = [{'HEX': '#a4c639', 'RGB': '164,198,57', 'English': 'Android Green}]
# When calling chosen_colour[0] - [0] is the key (thats why ["HEX"] works)

chosen_colour = []
    
with open("./data/colours_865.csv", mode="r") as text_colours:
    reader = csv.DictReader(text_colours)
    for row in reader:
        if row["English"] == "Android Green":
            print(row)
            chosen_colour.append(row)
            print(chosen_colour)

if chosen_colour:
    HEX = chosen_colour[0]["HEX"]
    English = chosen_colour[0]["English"]      \

# BETTER WAY - FOR INSTEAD OF IF STATEMENT ABOVE
# for i in chosen_colour:
#     hex = i["HEX"]
#     english = i["English"]

print(f'<p style="color:{HEX};">{English}</p>')


# REECE'S WAY

with open("./data/colours_865.csv", mode="r") as file:
    reader = csv.reader(file)

    next(reader)
    for row in reader:
        name = row[2]
        hex_code = row[1]
        if name == "Android Green":
            print(f'<p style="color:{hex_code};">{name}</p>')

# THIS IS WAY SIMPLER - NO LIST NEEDED. JUST PRINT STRAIGHT AWAY. MAY BE BETTER FOR OTHERS READING.
