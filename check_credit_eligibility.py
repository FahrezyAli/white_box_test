def check_credit_eligibility(age, income, debt, job_stability, has_collateral, credit_score):
    """
    Menentukan kelayakan kredit berdasarkan beberapa kriteria.
    Return: "Eligible", "Review", atau "Not Eligible"
    """

    # Cabang utama 1: Umur minimal
    if age < 21:
        return "Not Eligible"
    else:
        # Cabang utama 2: Skor kredit tinggi
        if credit_score >= 750 and income >= 5000:
            return "Eligible"
        
        # Cabang utama 3: Pendapatan menengah dengan kondisi tambahan
        elif 500 <= credit_score < 750:
            if income >= 3000 and (job_stability or has_collateral):
                if debt < income * 0.3:
                    return "Eligible"
                elif 0.3 <= (debt / income) <= 0.5:
                    return "Review"
                else:
                    return "Not Eligible"
            else:
                return "Not Eligible"

        # Cabang utama 4: Skor kredit rendah
        else:
            if credit_score < 500:
                if has_collateral and income >= 4000:
                    return "Review"
                elif job_stability and income >= 3500 and debt < 2000:
                    return "Review"
                else:
                    return "Not Eligible"
    
    # fallback (harusnya tidak pernah tercapai)
    return "Not Eligible"
