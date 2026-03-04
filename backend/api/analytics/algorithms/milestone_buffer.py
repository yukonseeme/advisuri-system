from datetime import datetime

def calculate_buffer(forecast_date_str, deadline_date):
    """
    Goal: Calculate the 'Cushion' between predicted finish and the actual deadline.
    Returns: Days remaining (Positive = Safe, Negative = Overdue).
    """
    if not forecast_date_str or forecast_date_str == "N/A":
            return 0

    forecast_dt = datetime.strptime(forecast_date_str, "%Y-%m-%d").date()

    # Calculate difference
    delta = (deadline_date - forecast_dt).days
    return delta