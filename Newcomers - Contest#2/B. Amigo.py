k = int(input())
l = int(input())
#we have to find out if the key "k" could open the door "l" or not.
if k == 1 and l == 2:
    print("GOOD LUCK AGENT P")
elif k == 2 and (l == 1 or l == 3):
    print("GOOD LUCK AGENT P")
elif k == 3 and (l == 2 or l == 4):
    print("GOOD LUCK AGENT P")
elif k == 4 and (l == 3 or l == 5):
    print("GOOD LUCK AGENT P")
elif k == 5 and l == 4:
    print("GOOD LUCK AGENT P")
else:
    print("CURSE YOU")