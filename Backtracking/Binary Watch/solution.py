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

# Backtracking method:
class Solution:
    # Generate all possible sum given candidate_list and the number of count
    def generate(self,candidate_list,count):
        result_set = list()
        self.back_track(candidate_list,result_set,0,0,count)
        return result_set

    def back_track(self,candidate_list,result_set,total_sum,position,count):
        if count == 0:
            result_set.append(total_sum)
            return
        else:
            for i in range(position,len(candidate_list)):
                self.back_track(candidate_list,result_set,total_sum+candidate_list[i],i+1,count-1)


    def readBinaryWatch(self, num: int) -> List[str]:
        result = []
        if num < 0 or num > 8:
            return []
        if num == 0:
            return ['0:00']

        hour_list = [8,4,2,1]
        minute_list = [32,16,8,4,2,1]
        for i in range(num+1):
            hour_set = self.generate(hour_list,i)
            minute_set = self.generate(minute_list,num-i)
            for hour in hour_set:
                if hour > 11:
                    continue
                for minute in minute_set:
                    if minute>59:
                        continue
                    result.append('{:d}:{:02d}'.format(hour, minute))
        return result
