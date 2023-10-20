def find_duplicate_epcs(input_list):
    # Create a dictionary to store EPC counts and lists
    epc_dict = {}

    for sublist in input_list:
        epc = sublist[1]  # Get the second element of the sublist
        if epc in epc_dict:
            epc_dict[epc].append(sublist)
        else:
            epc_dict[epc] = [sublist]

    # Check if EPC duplicates are found
    duplicate_found = False
    for epc, sublists in epc_dict.items():
        if len(sublists) > 1:
            duplicate_found = True
            break

    if duplicate_found:
        print("EPC Duplicates found")

    # Separate unique and duplicate sublists
    unique_sublists = [sublist for sublist in input_list if len(epc_dict[sublist[1]]) == 1]
    duplicate_sublists = [sublist for sublist in input_list if len(epc_dict[sublist[1]]) > 1]

    # Return counts and lists
    return len(unique_sublists), unique_sublists, len(duplicate_sublists), duplicate_sublists

# Example usage with sampleList
sampleList = [
    ['e2806894200050299705499e', '30361F8B380783174876F5AA', 1, False],

              ['e2806894200040289df3717d', '30361F8B380783174876F5AB', 1, False],

              ['e2806894200050299703fd3e', '30361F8B380783174876F5AC', 1, False],

              ['e2806894200050289df5ece4', '30361F8B380783174876F5AD', 1, False],

              ['e280689420005028a323d4e0', '30361F8B380783174876F5AE', 1, False],

              ['e2806894200050299a079572', '30361F8B380783174876F5AF', 1, False],

              ['e280689420004028441518f6', '30361F8B380783174876F5B0', 1, False],

              ['e2806894200040299a067ca8', '30361F8B380783174876F5B1', 1, False],

              ['e280689420005028a266bd51', '30361F8B380783174876F5B2', 1, False],

              ['e2806894200040299a07f97f', '30361F8B380783174876F5B3', 1, False],

              ['e280689420004028a25485cf', '30361F8B380783174876F5B4', 1, False],

              ['e280689420005028a1a6386c', '30361F8B380783174876F5B5', 1, False],

              ['e2806894200050289df37933', '30361F8B380783174876F5B6', 1, False],

              ['e280689420005028a1a5bd76', '30361F8B380783174876F5BC', 1, False],

              ['e28068942000402104b03d1d', '30361F8B380783174876F5B8', 2, False],

              ['e280689420004029970565ab', '30361F8B380783174876F5B8', 2, False],

              ['e280689420005028a269513f', '30361F8B380783174876F5BA', 2, False],

              ['e2806894200050299703c0b1', '30361F8B380783174876F5BC', 3, False],

              ['e2806894200040289df390e1', '30361F8B380783174876F5BC', 3, False],

              ['e2806894200040289e0415d1', '30361F8B380783174876F5BD', 3, False]
]

unique_count, unique_sublists, duplicate_count, duplicate_sublists = find_duplicate_epcs(sampleList)

# Print the counts and lists
print("EPC Duplicates found" if duplicate_count > 0 else "EPC Duplicates not found")
print("\nunique list")
print(unique_count)
print(unique_sublists)
print("\nduplicate list")
print(duplicate_count)
print(duplicate_sublists)
