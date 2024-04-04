def count_vow_and_con(input_string):
    vow = "aeiou"
    con = "bcdfghjklmnpqrstvwxyz"
    
    vow_count = 0
    con_count = 0
    
    input_string = input_string.lower()
    
    for char in input_string:
        if char in vow:
            vow_count += 1
        elif char in con:
            con_count += 1
    
    counts = {'vowels': vow_count, 'consonants': con_count}
    
    return counts


input_string = input("Enter your string here: ")
result = count_vow_and_con(input_string)
print(result)  