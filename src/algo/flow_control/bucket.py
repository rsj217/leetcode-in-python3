import time


class FlowControl:

    def __init__(self, cap: int = 100, rate: int = 10):
        self.cap = cap
        self.rate = rate
        self.token = 0
        self.last = None

    def consumer_bucket(self) -> bool:
        now = time.time()
        # 流出的token
        out_token = (now - self.last) * self.rate
        # 当前的token
        self.token = max(0, self.token - out_token)
        # 当前的token与新请求少于 bucket 容量
        if self.token + 1 <= self.cap:
            self.token += 1
            self.last = now
            return True
        else:
            return False

    def consumer_token(self) -> bool:

        now = time.time()
        # 流入的token
        in_token = (now - self.last) * self.rate
        # 当前的token
        self.token = min(self.cap, self.token + in_token)
        # 当前的token可以使用
        if self.token - 1 >= 0:
            self.token -= 1
            self.last = now
            return True
        else:
            return False
