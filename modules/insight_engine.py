def generate_insights(results):
    """
    Generate simple, explainable insights
    from personal activity statistics.
    """

    insights = []

    # Check whether analysis results are available
    if not results:
        return ["No data available to generate insights."]

    for column, stats in results.items():

        average = stats["average"]
        minimum = stats["minimum"]
        maximum = stats["maximum"]

        # Check for columns with no variation
        if minimum == maximum:
            insights.append(
                f"Your {column} value remained constant "
                f"at {average:.2f} in this dataset."
            )

        # General numerical insight
        else:
            insights.append(
                f"Your average {column} is {average:.2f}. "
                f"The values range from {minimum:.2f} "
                f"to {maximum:.2f}."
            )

    return insights
