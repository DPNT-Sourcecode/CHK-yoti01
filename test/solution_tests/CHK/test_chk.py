from solutions.CHK import checkout_solution


class Test():
    def test(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("AB") == 80
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("a") == -1
        assert checkout_solution.checkout("BEE") == 80
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("F") == 10
        assert checkout_solution.checkout("FFF") == 20
#        assert checkout_solution.checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 965
        assert checkout_solution.checkout("EE") == 80
        assert checkout_solution.checkout("RRR") == 150
        assert checkout_solution.checkout("STXYZ") == 45 + 17 + 20

