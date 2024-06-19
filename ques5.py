text = input("Enter some text: ")
sampleFile = open("C:/Users/Shambhavi/OneDrive/Documents/test/demo.txt", "w")
print(text, file=sampleFile)
print("Successfully saved to the text file")