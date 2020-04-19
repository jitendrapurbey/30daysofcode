# solution worked in all test cases
class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        values = self.__elements
        max_value = list()
        sorted_elements = sorted(self.__elements)
        self.maximumDifference = abs(sorted_elements[-1] - sorted_elements[0])

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)


# solution not worked some test cases
class Difference:
    def __init__(self, a):
        self.__elements = a


    # Add your code here
    def computeDifference(self):
        values = self.__elements
        max_value = list()

        for rank, i in enumerate(values):
            if rank == len(values) - 1:
                diff = values[rank] - values[0]
                diff = abs(diff)
            else:
                diff = values[rank] - values[rank + 1]
                diff = abs(diff)
            max_value.append(diff)
        maximum_value = max(max_value)
        self.maximumDifference = maximum_value


    # def maximumDifference(self):
    #     values = self.computeDifference()
    #     maximum_value = max(values)
    #     return maximum_value


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
