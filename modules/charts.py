import plotly.express as px


def create_chart(df, column):
    """
    Create an interactive chart for a selected
    numeric activity column.
    """

    # Check whether the selected column exists
    if column not in df.columns:
        return None

    # Check whether the selected column is numeric
    if not df[column].dtype.kind in "iuf":
        return None

    # Create a line chart
    fig = px.line(
        df,
        y=column,
        title=f"{column} Trend",
        markers=True
    )

    # Add chart labels
    fig.update_layout(
        xaxis_title="Records",
        yaxis_title=column,
        template="plotly_white"
    )

    return fig
