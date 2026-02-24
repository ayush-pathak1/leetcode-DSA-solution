class Solution(object):
    def removeDigit(self, number, digit):
        last_index = -1
        
        for i in range(len(number)):
            if number[i] == digit:
                last_index = i
                if i + 1 < len(number) and number[i + 1] > digit:
                    return number[:i] + number[i+1:]
        
        return number[:last_index] + number[last_index+1:]
        