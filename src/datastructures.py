
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        if not "id" in member:
            member["id"] = self._generateId()
            self._members.append(member)

    def delete_member(self, id):
        # fill this method and update the return
        for i in range(len(self._members)):
            if self._members[i]["id"] == id:
                member = self._members[i]
                del self._members[i]
                return member

    def get_member(self, id):
        # fill this method and update the return
        for i in range(len(self._members)):
            if self._members[i]["id"] == id:
                return self._members[i]

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members


jackson_family = FamilyStructure("Jackson")

member1 = {
    "first_name": "John",
    "last_name": "Jackson",
    "age": 33,
    "lucky_numbers": [7, 13, 22]
}

member2 = {
    "first_name": "Jane",
    "last_name": "Jackson",
    "age": 35,
    "lucky_numbers": [10, 14, 3]
}

member3 = {
    "first_name": "Jimmy",
    "last_name": "Jackson",
    "age": 5,
    "lucky_numbers": [1]
}

jackson_family.add_member(member1)
jackson_family.add_member(member2)
jackson_family.add_member(member3)

print(jackson_family._members)