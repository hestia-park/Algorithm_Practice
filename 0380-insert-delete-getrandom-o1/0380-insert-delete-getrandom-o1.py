# class RandomizedSet:

#     def __init__(self):
#         self.array=[]
        

#     def insert(self, val: int) -> bool:
#         # print("insert ",self.array)
#         if val not in self.array:
#             self.array.append(val)
            
#             return True
#         else:
#             return False


#     def remove(self, val: int) -> bool:
#         # print("remove ",self.array)
#         if val in self.array:
#             self.array.remove(val)
#             return True
#         else:
#             return False
        

#     def getRandom(self) -> int:
#         # print("getRandom ",self.array)
#         if len(self.array) ==0:
#             return False
#         else:
#             return random.choice(self.array)

        

class RandomizedSet:
    def __init__(self):
        self.array = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        # Move the last element to the place of the element to delete
        last_element = self.array[-1]
        idx_to_remove = self.dict[val]
        self.array[idx_to_remove] = last_element
        self.dict[last_element] = idx_to_remove
        # Remove the last element
        self.array.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)

# Example usage:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()