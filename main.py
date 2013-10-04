def collect(word):
    small_alphabet = range(97,123) #Ascii characters for small letters
    cap_alphabet = range(65, 91)	#Ascii characters for cap letters
    encrypt_word = ""
    for i in word:
        if ord(i) not in range(97,123) + range(65,91):
            new_i = str(i)
        else:
            if ord(i) in range(97,123):
                alphabet = range(97,123)
            if ord(i) in range(65,91):
                alphabet = range(65,91)
            '''the next line will find the modulo 26 of the difference of 
            the last letter and the ascii character  of i, make it negative
            so that it starts counting from behind and then adds 13.
            Modulo allows the code to be cyclical around the alphabet 
            so that it never is never out of range'''
            add_13 = -(((alphabet[-1] + 1) - ord(i)) % 26) + 13
            new_i  = chr(alphabet[add_13])
        encrypt_word += new_i
    return encrypt_word
