str = input("Enter something: ")
freq = {}
 
for i in str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
    print("Count of all characters in GeeksforGeeks is :\n "+ 
      str(freq)) 