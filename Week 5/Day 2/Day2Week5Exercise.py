class Family:

    def __init__(self, members):
        self.members = []

    def add_member(self, name, age, sex, is_child):
        member = {"name": name, "age": age, "sex": sex, "is_child": is_child}
        self.members.append(member)

    def is_18(self, name):
        family = self.members
        for item in family:
            if item["name"] != name:
                continue
            elif item["name"] == name:
                if item["age"] < 18:
                    return True
                else:
                    return  False
                break


    def represent(self):
        for i in range (len(self.members)):
                print(f" my name is {self.members[i]['name']}, I am {self.members[i]['age']} and I am a {self.members[i]['sex']}")










new_member = Family("Levy")
new_member.add_member("Michael", 35, "male", False)
new_member.add_member("Julia", 10, "female", True)
new_member.add_member("Sarah", 32, "female", False)
new_member.add_member("Kevin", 16, "male", True)
print(new_member.members)
print(new_member.is_18("Julia"))
print(new_member.represent())
