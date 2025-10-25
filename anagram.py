'''
Check if s1 and s2 are anagram
'''

def hashmap(s1, s2):
    #check if s1 and s2 has the same length
    #if no, then output false
    #if yes, then compare the string -> loop or hashmap

    if(len(s1) != len(s2)):
        return False
    
    map1 = {}
    map2 = {}

    for ch1 in s1:
        if ch1 in map1:
            map1[ch1] += 1
        else:
            map1[ch1] = 1
    
    for ch2 in s2:
        if ch2 in map2:
            map2[ch2] += 1
        else:
            map2[ch2] = 1
    
    for key in map1:
        if key not in map2 or map1[key] != map2[key]:
            return False
    return True

def sorting(s1, s2):
    if(len(s1) != len(s2)):
        return False
    
    return sorted(s1) == sorted(s2)

def main():
    s1 = "nameless"
    s2 = "salesmen"
    hashmap_value = hashmap(s1,s2)

    if hashmap_value == True:
        print("Hashmap method shows Anagram")
    else:
        print("Hashmap method shows Not Anagram")

    sorting_value = sorting(s1, s2)

    if sorting_value == True:
        print("Sorting method shows Anagram")
    else:
        print("Sorting method shows Not Anagram")


if __name__ == "__main__":
    main()