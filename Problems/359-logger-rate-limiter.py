# https://leetcode.com/problems/logger-rate-limiter

class Logger:

    def __init__(self):
        self.msg2time = dict()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.msg2time:
            self.msg2time[message] = timestamp
            return True
        if timestamp - self.msg2time[message] >= 10:
            self.msg2time[message] = timestamp
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)