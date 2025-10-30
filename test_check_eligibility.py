import unittest
from check_credit_eligibility import check_credit_eligibility

class TestCreditEligibility(unittest.TestCase):

    def test_young_age(self):
        """Node path: 0→1→2→3"""
        result = check_credit_eligibility(18, 2000, 0, False, False, 400)
        self.assertEqual(result, "Not Eligible")

    def test_high_credit_and_income(self):
        """Node path: 0→1→2→4→5"""
        result = check_credit_eligibility(30, 6000, 1000, True, False, 800)
        self.assertEqual(result, "Eligible")

    def test_mid_credit_good_income_low_debt(self):
        """Node path: 0→1→2→4→6→7→8→9"""
        result = check_credit_eligibility(30, 4000, 500, True, False, 650)
        self.assertEqual(result, "Eligible")

    def test_mid_credit_medium_debt(self):
        """Node path: 0→1→2→4→6→7→10→11"""
        result = check_credit_eligibility(30, 4000, 1600, True, False, 700)
        self.assertEqual(result, "Review")

    def test_mid_credit_high_debt(self):
        """Node path: 0→1→2→4→6→7→10→12"""
        result = check_credit_eligibility(30, 4000, 3000, True, False, 700)
        self.assertEqual(result, "Not Eligible")

    def test_mid_credit_no_stability(self):
        """Node path: 0→1→2→4→6→7→13"""
        result = check_credit_eligibility(30, 2000, 1000, False, False, 600)
        self.assertEqual(result, "Not Eligible")

    def test_low_credit_with_collateral(self):
        """Node path: 0→1→2→4→6→14→15→16"""
        result = check_credit_eligibility(35, 4500, 1000, False, True, 450)
        self.assertEqual(result, "Review")

    def test_low_credit_with_job_stability(self):
        """Node path: 0→1→2→4→6→14→15→17→18"""
        result = check_credit_eligibility(40, 3600, 1000, True, False, 400)
        self.assertEqual(result, "Review")

    def test_low_credit_no_support(self):
        """Node path: 0→1→2→4→6→14→15→17→19"""
        result = check_credit_eligibility(40, 2000, 3000, False, False, 450)
        self.assertEqual(result, "Not Eligible")

    def test_credit_just_above_500(self):
        """Node path: 0→1→2→4→6→14→20"""
        result = check_credit_eligibility(40, 2000, 1000, False, False, 520)
        self.assertEqual(result, "Not Eligible")

if __name__ == '__main__':
    unittest.main()