def remove_chars(word, n):
    # write your code 
    end=len(word)

    return (word[n:end])

  #n=8 
  # word[2:8]  
 

print("Removing characters from a string")
print(remove_chars("pynative", 4)) 
# output 'tive' first four characters are removed

print(remove_chars("pynative", 2)) 
# output 'native'