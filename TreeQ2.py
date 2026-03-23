class TreeQ2:
    def __init__(self, country):
        self.country = country
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, level):
        spaces = " " * self.getLevel() * 3
        prefix = spaces + "|__" if self.parent else ""
        if self.getLevel() > level:
            return
        print(prefix + self.country)
        if self.children:
            for child in self.children:
                child.print_tree(level)



def build_tree():
    root = TreeQ2("Global")

    india = TreeQ2("India")
    usa = TreeQ2("USA")

    gujarat = TreeQ2("Gujarat")
    karnataka = TreeQ2("Karnataka")

    ahamedabad = TreeQ2("Ahamedabad")
    baroda = TreeQ2("Baroda")

    bangalore = TreeQ2("Bangalore")
    mysore = TreeQ2("Mysore")

    newJersey = TreeQ2("NewJersey")
    california = TreeQ2("California")

    princeton = TreeQ2("Princeton")
    trenton = TreeQ2("Trenton")

    sanFrancisco = TreeQ2("San Francisco")
    mountainView = TreeQ2("MountainView")
    paloAlto = TreeQ2("PaloAlto")


    newJersey.add_child(princeton)
    newJersey.add_child(trenton)

    california.add_child(sanFrancisco)
    california.add_child(mountainView)
    california.add_child(paloAlto)

    usa.add_child(newJersey)
    usa.add_child(california)


    india.add_child(gujarat)
    india.add_child(karnataka)

    gujarat.add_child(ahamedabad)
    gujarat.add_child(baroda)

    karnataka.add_child(bangalore)
    karnataka.add_child(mysore)

    root.add_child(india)
    root.add_child(usa)
    return root


if __name__ == '__main__':
    root = build_tree()
    root.print_tree(2)
    pass
