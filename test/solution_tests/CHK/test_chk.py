from solutions.CHK import checkout_solution


class Test():
    def test(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("AB") == 80
        assert checkout_solution.checkout("AAA") == 130

