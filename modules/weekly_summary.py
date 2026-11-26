def generate_weekly_summary(results):
    """
    Generate a readable summary from activity statistics.
    """

    if not results:
        return "No activity data available for a summary."

    summary = []

    summary.append("Weekly Activity Summary")
    summary.append("-----------------------")

    for column, stats in results.items():

        average = stats["average"]
        minimum = stats["minimum"]
        maximum = stats["maximum"]

        summary.append(
            f"{column}: Average = {average:.2f}, "
            f"Minimum = {minimum:.2f}, "
            f"Maximum = {maximum:.2f}"
        )

    return "\n".join(summary)
