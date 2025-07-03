# Slicing 
name = "Rin"
print(name[0]) #R
print(name[1]) #i
print(name[2]) #n

# Slicing with start index and end index
# take character from index 0 to 3
name = "Rin"
print(name[0:3]) #Rin
# take character from index 0 to 2
name = "Rin"
print(name[0:2]) #R

# Slicing from start to or end
# Slice from start to index 10
team = "San Antonio Spurs"
print(team[:10]) #San Antonio
# Slice from index 5 t end
team = "San Antonio Spurs"
print(team[5:]) #Spurs
# Slice all string (copy string)
team = "San Antonio Spurs"
print(team[:]) #San Antonio Spurs

# Negative Indexing
character= "Andor"

# Last Character
print(character[-1]) #r

# Last two characters
print(character[-2:]) #or

# All characters except last two
print(character[:-2]) #And

# Reverse string
print(character[::-1]) #rodnA