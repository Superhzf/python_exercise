
# Employee info

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dict = {}
        for this_employee in employees:
            employee_dict[this_employee.id] = this_employee

        total_value = 0
        q = [employee_dict[id]]
        while q:
            this_sub = q.pop(0)
            total_value += this_sub.importance
            for sub in this_sub.subordinates:
                q.append(employee_dict[sub])
        return total_value

# The idea is that fist store employees in a hash table (dict) for query
# convenience. Then, find out all the importance by DFS
