class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        n = len(s)
        
        if n < 4 or n > 12:
            return res

        def is_valid(segment):
            if len(segment) > 1 and segment[0] == '0':
                return False
            if int(segment) > 255:
                return False
            return True

        for i in range(1, min(4, n - 2)):
            for j in range(i + 1, min(i + 4, n - 1)):
                for k in range(j + 1, min(j + 4, n)):
                    p1, p2, p3, p4 = s[:i], s[i:j], s[j:k], s[k:]
                    if is_valid(p1) and is_valid(p2) and is_valid(p3) and is_valid(p4):
                        res.append("{}.{}.{}.{}".format(p1, p2, p3, p4))

        return res