import pytest
from check_credit_eligibility import check_credit_eligibility


class TestCheckCreditEligibility:
    """
    A comprehensive test suite for the check_credit_eligibility function.
    """

    def test_age_less_than_21(self):
        """Test case: Age less than 21, should return 'Not Eligible'."""
        assert (
            check_credit_eligibility(20, 6000, 1000, True, True, 600) == "Not Eligible"
        )

    def test_high_credit_score_and_high_income(self):
        """Test case: High credit score and high income, should return 'Eligible'."""
        assert check_credit_eligibility(25, 5000, 1000, True, True, 750) == "Eligible"

    def test_medium_credit_score_and_sufficient_income_with_job_stability(self):
        """Test case: Medium credit score, sufficient income, and job stability, should return 'Eligible'."""
        assert check_credit_eligibility(25, 3000, 500, True, False, 600) == "Eligible"

    def test_medium_credit_score_and_sufficient_income_with_collateral(self):
        """Test case: Medium credit score, sufficient income, and collateral, should return 'Eligible'."""
        assert check_credit_eligibility(25, 3000, 500, False, True, 600) == "Eligible"

    def test_medium_credit_score_and_insufficient_income(self):
        """Test case: Medium credit score and insufficient income, should return 'Not Eligible'."""
        assert (
            check_credit_eligibility(25, 2000, 500, True, True, 600) == "Not Eligible"
        )

    def test_medium_credit_score_and_high_debt_ratio(self):
        """Test case: Medium credit score and high debt ratio, should return 'Not Eligible'."""
        assert (
            check_credit_eligibility(25, 3000, 2000, True, False, 600) == "Not Eligible"
        )

    def test_medium_credit_score_and_moderate_debt_ratio(self):
        """Test case: Medium credit score and moderate debt ratio, should return 'Review'."""
        assert check_credit_eligibility(25, 3000, 1200, True, False, 600) == "Review"

    def test_low_credit_score_with_collateral_and_sufficient_income(self):
        """Test case: Low credit score with collateral and sufficient income, should return 'Review'."""
        assert check_credit_eligibility(25, 4000, 1000, False, True, 400) == "Review"

    def test_low_credit_score_with_job_stability_and_sufficient_income_and_low_debt(
        self,
    ):
        """Test case: Low credit score with job stability, sufficient income, and low debt, should return 'Review'."""
        assert check_credit_eligibility(25, 3500, 1500, True, False, 400) == "Review"

    def test_low_credit_score_without_collateral_or_job_stability(self):
        """Test case: Low credit score without collateral or job stability, should return 'Not Eligible'."""
        assert (
            check_credit_eligibility(25, 3000, 1000, False, False, 400)
            == "Not Eligible"
        )

    def test_edge_case_age_21(self):
        """Test case: Age exactly 21, high credit score, high income."""
        assert check_credit_eligibility(21, 5000, 1000, True, True, 750) == "Eligible"

    def test_edge_case_credit_score_749(self):
        """Test case: credit score 749, income above 3000, job stability."""
        assert check_credit_eligibility(25, 3000, 500, True, False, 749) == "Eligible"

    def test_edge_case_credit_score_500(self):
        """Test case: credit score 500, income above 3000, job stability."""
        assert check_credit_eligibility(25, 3000, 500, True, False, 500) == "Eligible"

    def test_edge_case_credit_score_499(self):
        """Test case: credit score 499, collateral and income."""
        assert check_credit_eligibility(25, 4000, 500, False, True, 499) == "Review"

    def test_edge_case_debt_equals_income_times_0_3(self):
        """Test case: debt equals income * 0.3, medium credit score, job stability."""
        assert check_credit_eligibility(25, 3000, 900, True, False, 600) == "Eligible"

    def test_edge_case_debt_ratio_exactly_0_5(self):
        """Test case: debt ratio exactly 0.5, medium credit score, job stability."""
        assert check_credit_eligibility(25, 3000, 1500, True, False, 600) == "Review"

    def test_edge_case_debt_ratio_slightly_above_0_5(self):
        """Test case: debt ratio slightly above 0.5, medium credit score, job stability."""
        assert (
            check_credit_eligibility(25, 3000, 1501, True, False, 600) == "Not Eligible"
        )

    def test_edge_case_income_equals_5000_and_credit_score_equals_750(self):
        """Test case: income equals 5000 and credit score equals 750, should return 'Eligible'."""
        assert check_credit_eligibility(25, 5000, 1000, True, True, 750) == "Eligible"

    def test_income_equals_3000_and_job_stability_true_and_debt_less_than_income_times_0_3(
        self,
    ):
        """Test case: income equals 3000, job stability true, debt less than income * 0.3."""
        assert check_credit_eligibility(25, 3000, 899, True, False, 600) == "Eligible"

    def test_income_equals_4000_and_has_collateral_true_and_credit_score_less_than_500(
        self,
    ):
        """Test case: income equals 4000, has collateral true, credit score less than 500."""
        assert check_credit_eligibility(25, 4000, 1000, False, True, 400) == "Review"

    def test_income_equals_3500_and_job_stability_true_and_debt_less_than_2000_and_credit_score_less_than_500(
        self,
    ):
        """Test case: income equals 3500, job stability true, debt less than 2000, credit score less than 500."""
        assert check_credit_eligibility(25, 3500, 1999, True, False, 400) == "Review"
