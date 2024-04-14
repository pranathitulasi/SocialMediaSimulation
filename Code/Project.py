class SocNet:
    def __init__(self):
        self.names = []
        self.names_list = []
        self.social_nw = {}
        self.unique_list = []
        self.ul = []
        self.all_list = []
        self.each_list = []
        self.list_set = []
        self.list1 = []
        self.name = str
        self.filename = str

    # feature 1.i
    def file_check(self, fn):  # this is to display the error message if file name is incorrect
        try:
            open(fn, "r")  # this tries to open the file name entered
            return 1
        except IOError:
            print("Invalid file name")
            return 0
            # if there is no such file in directory it throws an error return 0

    # feature 1.ii
    def start(self):
        loop = 'y'
        while loop == 'y':  # loops until the correct file name is entered
            self.filename = str(input("Enter the file name: "))
            self.social_nw = {}  # making an empty dictionary that will store keys and values

            if self.file_check(self.filename) == 1:
                with open(self.filename, 'r') as self.f:
                    # print (f.read())
                    self.f.close()
                    with open(self.filename, 'r') as self.f:
                        self.names = [line.strip() for line in self.f]
                        self.names.pop(0)  # removes the first string because it's not a member name
                        self.names_list = []  # list of lists to store every individual line in file
                        for i in self.names:
                            self.name = i.split()  # splits every string in each line and assigns it to names_list
                            self.names_list.append(self.name)  # adds each individual string to the names list

                        # print (self.ListNames)
                        self.all_list = []  # single list that stores all strings linearly
                        for i in self.names_list:
                            for j in i:
                                self.all_list.append(j)
                                # traverses each  list in names_list and separates out the strings into one list

                        self.ul = []
                        self.unique(self.all_list)  # performs the function 'unique' on the list of names
                        self.carry_one()

                loop = "n"

    def unique(self, list1):  # makes a list of all unique names and gets rid of duplicates
        self.list_set = set(list1)
        self.unique_list = (list(self.list_set))
        for x in self.unique_list:  # appends unique names to list ul
            self.ul.append(x)

    def carry_one(self):
        for a in self.ul:  # traverses through ul
            self.each_list = []
            if a in self.all_list:  # checks if that item is in all_list
                j = a  # assigns variable j to that item
                if a == j:
                    item = j
                    indices = [i for i in range(len(self.all_list)) if self.all_list[i] == item]
                    # gives the position of all instances of that item(string)
                    for i in indices:  # traverses through the list of positions that item appears in
                        pos = i
                        if (pos % 2) == 0:  # if position is even
                            self.each_list.append(self.all_list[pos + 1])  # add the next item
                        else:
                            self.each_list.append(self.all_list[pos - 1])
                            # add the previous item if odd this is because all_list prints every relationship linearly,
                            # so they are already in pairs so each pair consists of an even and odd number
                else:
                    continue

            self.social_nw[a] = self.each_list  # for each name/key it's assigning the list of friends
        self.ask_print()
        self.f.close()

    def ask_print(self):
        reply = input("Do you wish to view the social network (y/n)? ")
        if reply == "y":
            for key, values in self.social_nw.items():
                print(key, "->", values)  # pretty printing the dictionary data
        elif reply == "n":
            exit
        else:
            print("Invalid input")
            c.ask_print()


# feature 2.i
class CommonFriend(SocNet):
    def __init__(self):
        super().__init__()
        self.members = []
        self.common_list = []
        self.common_friends = {}

    def common(self):
        self.members = []
        for keys in self.social_nw:
            self.members.append(keys)  # adds each member's name to the list 'members'
        self.common_friends = {}
        for i in range(len(self.social_nw)):  # traversing the list of keys
            self.common_list = []
            n1 = self.members[i]
            for j in range(len(self.social_nw)):
                count = 0
                n2 = self.members[j]  # traverses down the list of keys again to search between values of both keys
                for a in self.social_nw[n1]:  # traversing the values of the key n1
                    for b in self.social_nw[n2]:  # traversing the values of the key n2
                        if a == b:
                            count = count + 1
                        else:
                            continue
                self.common_list.append(count)
            self.common_friends[n1] = self.common_list
            # for each key, the list of common friends is assigned as the value

        reply1 = str(input("Do you want to display common friends (y/n)? "))
        if reply1 == "y":
            for key, values in self.common_friends.items():
                print(key, "->", values)
        elif reply1 == "n":
            exit
        else:
            print("Invalid input")
            c.common()

    # feature 2.ii
    def recommend_friend(self):
        c.common()
        reply2 = input("Do you want to recommend a friend (y/n)? ")
        if reply2 == "y":
            m_name = input("Enter the name of the member you want to recommend a friend to: ")
            for key in self.common_friends:  # searches for the user input in dictionary
                if key == m_name:
                    circ = self.common_friends[key]  # gets the list of common friends for that member/key
                    val = max(circ)
                    # assigns variable 'val' to the highest number in the list of values. this is the highest no. of
                    # common friends with another person
                    name_val = circ.index(val)
                    # gets the index value of that number i.e. the person with whom they share the highest no. of
                    # common friends with (recommended friend)
                    rec_friend = self.ul[name_val]
                    # searches the 'ul' list to find the recommended friend through the index
                    print("Recommended friend is: ", rec_friend)
        elif reply2 == "n":
            exit
        else:
            print("Invalid input")
            c.recommend_friend()


# feature 3.i
class Connection(CommonFriend):
    def __init__(self):
        super().__init__()
        self.member_name = str
        self.ind_friends = {}
        self.ind_list = []

    def display_friends(self):
        reply3 = input("Do you want to display how many friends a member has (y/n)? ")
        if reply3 == "y":
            self.member_name = str(input("Enter the member name: "))
            # takes the user input and assigns it to 'member_name'
            if self.member_name in self.social_nw:
                print(self.member_name, "has", len(self.social_nw[self.member_name]), "friends")
                print(self.social_nw[self.member_name])
                # prints the length of list i.e. the number of friends and then the list itself
            else:
                print("Invalid name")
                c.display_friends()
        elif reply3 == "n":
            exit
        else:
            print("Invalid input")

    # feature 3.ii
    def least_friends(self):
        var_length = 50
        name = ""
        for i in self.social_nw:  # traverses the keys in the dictionary
            val = self.social_nw[i]  # retrieves the values for that key
            length = len(val)  # gets the length of list of values
            if length <= var_length:  # compares with fixed length
                var_length = length  # if it is lower, it is the new fixed length
                name = i  # assigns that key to variable 'name' to be printed later on
            else:
                continue

        reply4 = input("Do you want to display the member with the least friends (y/n)? ")
        if reply4 == "y":
            print(name)
        elif reply4 == "n":
            exit
        else:
            print("Invalid input")
            c.least_friends()

    # feature 3.iii
    def relationship(self):
        reply5 = input("Do you want to display a member's connections (y/n)? ")
        if reply5 == "y":
            name = input("Enter the member name: ")
            if name in self.ind_friends:  # checks the 'ind_friends' dictionary for the name
                print("Direct friends are:", self.social_nw[name], "\nIndirect friends are:", self.ind_friends[name])
                # prints direct friends from 'social_nw[]' and indirect friends from 'ind_friends[]'
            else:
                print("Invalid name")
                c.relationship()
        elif reply5 == "n":
            exit
        else:
            print("Invalid input")
            c.relationship()

    # feature 3.iv
    def indirect_connections(self):
        self.ind_friends = {}  # empty dictionary to store indirect friends of each member
        for i in self.social_nw:  # traverses through member names in social_nw
            self.ind_list = []  # empty list of values to assign to each key
            val = self.social_nw[i]  # retrieves the values of each key
            for a in val:  # traverses through the list of values for each key
                temp = self.social_nw[a]  # temporarily stores the list of friends of each friend of 'i'
                for b in temp:  # traversing through the list of friends ^^
                    if b in self.ind_list:
                        continue  # not adding if the name already exists in the list
                    elif b == i:
                        continue  # not adding the friend's name in their own indirect friends list
                    else:
                        self.ind_list.append(b)
            self.ind_friends[i] = self.ind_list

        reply6 = input("Do you want to display indirect connections (y/n)? ")
        if reply6 == "y":
            for key, values in self.ind_friends.items():
                print(key, '->', values)
        elif reply6 == "n":
            exit
        else:
            print("Invalid input")
            c.indirect_connections()

    def restart(self):
        reply7 = input("Do you want to view another social network (y/n)? ")
        if reply7 == "y":
            main()
        else:
            print("")


c = Connection()


def main():
    c.start()

    c.recommend_friend()

    c.display_friends()

    c.least_friends()

    c.indirect_connections()

    c.relationship()

    c.restart()


main()
