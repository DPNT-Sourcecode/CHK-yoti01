from solutions.HLO import hello_solution


class Test():
    def test(self):
        assert hello_solution.hello("John") == "Hello, John!"
