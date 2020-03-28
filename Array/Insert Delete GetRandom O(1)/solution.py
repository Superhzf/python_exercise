from random import choice
class RandomizedSet():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.list:
            idx = self.dict[val]
            last_ele = self.list[-1]
            self.list[idx], self.list[-1] = self.list[-1], self.list[idx]
            self.dict[val],self.dict[last_ele] = self.dict[last_ele], self.dict[val]
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)

# The idea is use both hashmap and list at the same time
# list is good at getting a member randomly
# hashmap is good at inserting and inserting
