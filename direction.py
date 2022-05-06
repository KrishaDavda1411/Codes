d = input()
dl = [c for c in d]
if dl.count("N") == dl.count("S") and dl.count("E") == dl.count("W"):
    print("Returned successfully")
else:print("Not Returned successfully")