str_1 = input("Enter a string with punctuation: ")
punctuation_chars = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
cleaned_string = ""

for i in str_1:
    
    if i not in punctuation_chars:
        
        cleaned_string = cleaned_string+i

print("String without punctuation:",cleaned_string)