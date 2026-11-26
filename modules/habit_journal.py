from datetime import date


def create_habit_entry(habit_name, completed, notes=""):
    """
    Create a daily habit journal entry.
    """

    # Check whether habit name is provided
    if not habit_name or not habit_name.strip():
        return None, "Please enter a habit name."

    # Prepare the habit entry
    entry = {
        "date": date.today().isoformat(),
        "habit_name": habit_name.strip(),
        "completed": bool(completed),
        "notes": notes.strip()
    }

    return entry, "Habit entry created successfully!"


def get_habit_status(entry):
    """
    Return a readable habit completion status.
    """

    if entry["completed"]:
        return "Completed"

    return "Not completed"
