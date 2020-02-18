"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
		# record of all solution pairs (x, y)
        solution_pair = []

		# Two pointers,
		# x goes from lower bound, 1, to upper bound z
		# y goes from upper bound, z, to lower bound 1
        x, y = 1, z

        while x <= z and y >= 1:

            f_of_x_y = customfunction.f(x,y)

            if f_of_x_y > z:
                # this f(x,y) is too big, make y smaller
                y -= 1

            elif f_of_x_y < z:
                # this f(x,y) is too small, make x bigger
                x += 1

            else:
                # pair (x, y) is a solution to f(x,y) = z
                solution_pair.append( (x,y) )

                # make x bigger for next iteration
                x += 1

        return solution_pair

# This is actually using two pointers method
