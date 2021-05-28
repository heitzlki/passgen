import random;a,l=int(input("Amount:") or "1"), int(input("Length:") or "12");[print ("".join(random.choices("abcdefghijklmnopqrstuvwxyz1234567890",k=l))) for _ in range(a)]
