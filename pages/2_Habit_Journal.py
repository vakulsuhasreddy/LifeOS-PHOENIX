import streamlit as st

from modules.habit_journal import create_habit_entry
from database.db import create_tables, save_habit, get_habits


st.title("📖 Habit Journal")

st.write("Record and track your daily habits.")

# Make sure the database table exists
create_tables()

# Habit entry form
with st.form("habit_form"):

    habit_name = st.text_input("Enter habit name")

    completed = st.checkbox("Mark as completed")

    notes = st.text_area("Notes (optional)")

    submitted = st.form_submit_button("Save Habit")

    if submitted:

        entry, message = create_habit_entry(
            habit_name,
            completed,
            notes
        )

        if entry is None:
            st.error(message)

        else:
            save_habit(entry)
            st.success("Habit saved successfully!")

# Display saved habits
st.subheader("Your Saved Habits")

habits = get_habits()

if habits:

    st.table([
        {
            "Date": habit[1],
            "Habit": habit[2],
            "Status": (
                "Completed" if habit[3] else "Not completed"
            ),
            "Notes": habit[4]
        }
        for habit in habits
    ])

else:
    st.info("No habits recorded yet.")
