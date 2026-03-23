

class TreeQ1:
    def __init__(self, data, desgination):
        self.data = data
        self.desgination = desgination
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


    def print_tree(self, show="both"):
        spaces = " " * self.getLevel() * 3
        prefix = spaces + "|__" if self.parent else ""

        if show == "name":
            value = self.data
        elif show == "desgination":
            value = self.desgination
        else:
            value = f"{self.data} ({self.desgination})"

        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(show)


def build_tree():
    root = TreeQ1("Nilupul", "CEO")

    cto = TreeQ1("Chinemay", "CTO")

    infraHead = TreeQ1("Vishwa", "Infrastructure Head")
    appHead = TreeQ1("Aamir", "Application Head")

    cloudManager = TreeQ1("Dhaval", "Cloud Manager")
    infraHead.add_child(cloudManager)
    appManager = TreeQ1("Abhijit", "App Manager")
    infraHead.add_child(appManager)
    cto.add_child(infraHead)
    cto.add_child(appHead)

    hrHead = TreeQ1("Gels", "HR Head")
    hrHead.add_child(TreeQ1("Peter", "Recuitement Manager"))
    hrHead.add_child(TreeQ1("Waqas", "Policy Manager"))

    root.add_child(hrHead)
    root.add_child(cto)


    return root





if __name__ == '__main__':
    root = build_tree()
    root.print_tree()

    pass



