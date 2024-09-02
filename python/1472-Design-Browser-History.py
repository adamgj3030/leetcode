class BrowserHistory:

    def __init__(self, homepage: str):
        self.i = 0
        self.len = 1
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.i += 1
        if len(self.history) <= self.i:
            self.history.append(url)
        else:
            self.history[self.i] = url
        self.len = self.i + 1

    def back(self, steps: int) -> str:
        self.i = max (self.i - steps, 0)
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, self.len - 1)
        return self.history[self.i]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
