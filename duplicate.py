string = "I came for interview"
string = string.lower()
print("Duplicate characters in a given string: ")

for i in range(len(string)):
    if string[i] != ' ' and string[i] != '0':
        count = 1
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                count += 1
                string = string[:j] + '0' + string[j + 1:]
        if count > 1:
            print(string[i] + " - " + str(count))
