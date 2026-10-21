import numpy as np
import pandas as pd

# Subject columns expected in students.csv. Edit this list to change subjects.
SUBJECTS = ["Python", "Web Development", "Cyber Security", "Cloud Computing"]
REQUIRED_COLUMNS = ["Student_ID", "Name", "Department"] + SUBJECTS + ["Attendance"]


def check_columns(df):
    """Return the list of required columns that are missing from the data."""
    return [col for col in REQUIRED_COLUMNS if col not in df.columns]


def clean_marks(df):
    """Convert marks and attendance to numbers and report any invalid entries."""
    numeric_cols = SUBJECTS + ["Attendance"]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")
    bad_rows = df[df[numeric_cols].isna().any(axis=1) | (df[numeric_cols] < 0).any(axis=1)
                  | (df[numeric_cols] > 100).any(axis=1)]
    return df, bad_rows


def add_totals(df):
    """Add Total_Marks and Average_Marks using a NumPy array of the subject columns."""
    marks = df[SUBJECTS].to_numpy()
    df["Total_Marks"] = marks.sum(axis=1)
    df["Average_Marks"] = np.round(marks.mean(axis=1), 2)
    return df


def get_grade(avg):
    """Convert an average into a grade. Boundaries are inclusive (80 exactly is an A)."""
    if avg >= 90:
        return "A+"
    if avg >= 80:
        return "A"
    if avg >= 70:
        return "B"
    if avg >= 60:
        return "C"
    if avg >= 50:
        return "D"
    return "F"


def get_result(row):
    """Pass only if every subject mark is 40+ and attendance is 40%+."""
    marks_ok = all(row[subject] >= 40 for subject in SUBJECTS)
    attendance_ok = row["Attendance"] >= 40
    return "Pass" if marks_ok and attendance_ok else "Fail"


def subject_summary(df):
    """Average, highest and lowest mark of each subject."""
    return pd.DataFrame({
        "Subject": SUBJECTS,
        "Average_Marks": [round(df[s].mean(), 2) for s in SUBJECTS],
        "Highest_Mark": [df[s].max() for s in SUBJECTS],
        "Lowest_Mark": [df[s].min() for s in SUBJECTS],
    })
