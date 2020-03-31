class SnapshotArray:

    def __init__(self, length: int):
        self.snap_list = {}
        self.snap_id = 0
        self.snap_list[self.snap_id] = {}

    def set(self, index: int, val: int) -> None:
        self.snap_list[self.snap_id][index] = val


    def snap(self) -> int:
        self.snap_id += 1
        self.snap_list[self.snap_id] = {k:v for k,v in self.snap_list[self.snap_id-1].items()}
        return self.snap_id - 1


    def get(self, index: int, snap_id: int) -> int:
        return self.snap_list[snap_id].get(index,0)


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

# Use hash map instead of array
