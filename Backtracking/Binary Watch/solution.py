class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        result = []
        if num < 0 or num > 8:
            return []
        if num == 0:
            return ['0:00']

        for hour in range(12):
            for minute in range(60):
                if bin(hour).count('1')+bin(minute).count('1') == num:
                    result.append('{:d}:{:02d}'.format(hour, minute))
        return result

# The trick here is bin(x).count() which can help find out how many
# lights should be on to get x. This trick is specific for Python.
