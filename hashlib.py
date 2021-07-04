import hashlib,sys
def hash_func():
    def md5():
        print("\n")
        plainmd5text = input("enter the text to convert it into md5: ")
        hash_object_md5 = hashlib.md5(str(plainmd5text).encode('utf-8'))
        print("\n")
        print('Hash for the text in md5 is :  ', hash_object_md5.hexdigest())
        print("\n")
    def sha512():
        print("\n")
        plainsha512text = input("enter the text to convert it into sha512: ")
        hash_object_sha512 = hashlib.sha512(str(plainsha512text).encode('utf-8'))
        print("\n")
        print('Hash for the text in sha512 is :  ', hash_object_sha512.hexdigest())
        print("\n")
    def sha256():
        print("\n")
        plainsha256text = input("enter the text to convert it into sha256: ")
        hash_object_sha256 = hashlib.sha256(str(plainsha256text).encode('utf-8'))
        print("\n")
        print('Hash for the text in sha256 is :  ', hash_object_sha256.hexdigest())
        print("\n")
    def sha3_256():
        print("\n")
        plainsha3256text = input("enter the text to convert it into sha3_256: ")
        hash_object_sha3256 = hashlib.sha3_256(str(plainsha3256text).encode('utf-8'))
        print("\n")
        print('Hash for the text in sha3_256 is :  ', hash_object_sha3256.hexdigest())
        print("\n")
    def sha3_512():
        print("\n")
        plainsha3512text = input("enter the text to convert it into sha3_512: ")
        hash_object_sha3512 = hashlib.sha3_512(str(plainsha3512text).encode('utf-8'))
        print("\n")
        print('Hash for the text in sha3_512 is :  ', hash_object_sha3512.hexdigest())
        print("\n")
    def salting():
        print("\n")
        plaintext = input("enter the text: ")
        plainsaltingtext = ("salting"+plaintext+"salting")
        hash_object_salting_md5 = hashlib.md5(str(plainsaltingtext).encode('utf-8'))
        print("\n")
        print('Hash for the text is :  ', hash_object_salting_md5.hexdigest())
        print("\n")
        print("The above hash you got is the md5 hash for which salting is added at the start and at the end. For example if the text you entered is hello then salted text is saltinghellosalting and the hash is md5 for saltinghellosalting")
        print("\n")
    def iteration():
        print("\n")
        plainiterationtext = input("enter the text: ")
        print("\n")
        hash_md5_1 = hashlib.md5(str(plainiterationtext).encode('utf-8'))
        md51 = (hash_md5_1.hexdigest())
        hash_md5_2 = hashlib.md5(str(md51).encode('utf-8'))
        md52 = (hash_md5_2.hexdigest())
        hash_md5_3 = hashlib.md5(str(md52).encode('utf-8'))
        md53 = (hash_md5_3.hexdigest())
        hash_md5_4 = hashlib.md5(str(md53).encode('utf-8'))
        md54 = (hash_md5_4.hexdigest())
        hash_md5_5 = hashlib.md5(str(md54).encode('utf-8'))
        md55 = (hash_md5_5.hexdigest())
        print("iterated hash for the text is: ", md55)
        print("\n")
        print("the above md5 hash you got is the hash after iterating 5 itmes.")
        print("\n")
    menu = str(input("Type the number which you want to use  1.md5  2.sha512  3.sha256  4.sha3_256  5.sha3_512  6.salting  7.Iteration : "))
    if menu == "1":
      md5()
    elif menu == "2":
      sha512()
    elif menu == "3":
      sha256()
    elif menu == "4":
      sha3_256()
    elif menu == "5":
      sha3_512()
    elif menu == "6":
      salting()
    elif menu == "7":
      iteration()
    else: 
      sys.exit(0)
    runagain = str(input("Do you want to use this again (type yes or no): "))
    print("\n")
    while runagain == "yes":
      hash_func()
    else:
      print("\n")
      print("closing the programme")
      sys.exit(0)
hash_func()
