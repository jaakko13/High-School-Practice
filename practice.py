'''import random
import datetime

def strong():

    upper = "ABCDEFGHIJKLMONPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    num = "1234567890"
    special = "!@#$%^&*()"
    password = ''
    password += random.choice(upper)
    password += random.choice(lower)
    password += random.choice(upper)
    password += random.choice(lower)
    password += random.choice(num)
    password += random.choice(special)
    password += random.choice(num)
    password += random.choice(special)

    print(password)


strong()


def random_episode_chooser():

    office_list = ["season 1 episode 1", "season 1 episode 2", "season 1 episode 3", "season 1 episode 4",
                   "season 1 episode 5", "season 1 episode 6", ]
    friends_list = ["season 1 episode 1", "season 1 episode 2", "season 1 episode 3", "season 1 episode 4",
                    "season 1 episode 5", "season 1 episode 6", ]
    print("The office or Friends")
    x = input().lower()
    if x == "the office":
        print(random.choice(office_list))
    if x == "friends":
        print(random.choice(friends_list))
    print(datetime.datetime.now())


random_episode_chooser()



def asdf():
    n = 5
    while n < 10:
        print("ok")
        if n < 10:
            n += 1
        if n > 9:
            print("noice")


asdf()
'''


def rang():

    for x in range(10):
        print("x")
    else:
        print("done")


rang()
