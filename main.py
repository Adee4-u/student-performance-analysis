import os
import pandas as pd
from functions import (check_columns, clean_marks, add_totals, get_grade,
                       get_result, subject_summary)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "students.csv")


def heading(text):
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60)


def main():
    # 1. Load and check the file
    if not os.path.isfile(DATA_FILE):
        print("students.csv not found. Keep it in the same folder as main.py")
        return

    df = pd.read_csv(DATA_FILE)
    if df.empty:
        print("students.csv has no student records.")
        return

    missing = check_columns(df)
    if missing:
        print("These columns are missing from students.csv:", ", ".join(missing))
        return

    df, bad_rows = clean_marks(df)
    if not bad_rows.empty:
        print("Invalid marks or attendance found (must be numbers from 0 to 100):")
        print(bad_rows.to_string(index=False))
        return

    heading("STUDENT PERFORMANCE ANALYSIS")
    print("Total students:", len(df))
    print("Columns:", list(df.columns))
    print()
    print(df.head().to_string(index=False))

    # 2. Totals, grades and results
    df = add_totals(df)
    df["Grade"] = df["Average_Marks"].apply(get_grade)
    df["Result"] = df.apply(get_result, axis=1)

    # 3. Ranking
    heading("STUDENT WISE RESULTS")
    columns = ["Student_ID", "Name", "Department", "Total_Marks",
               "Average_Marks", "Grade", "Attendance", "Result"]
    ranked = df.sort_values("Average_Marks", ascending=False)
    print(ranked[columns].to_string(index=False))

    # 4. Class summary
    heading("CLASS SUMMARY")
    topper = df.loc[df["Average_Marks"].idxmax()]
    lowest = df.loc[df["Average_Marks"].idxmin()]
    passed = int((df["Result"] == "Pass").sum())
    failed = len(df) - passed
    print("Class average:", round(df["Average_Marks"].mean(), 2))
    print("Highest:", topper["Name"], "-", topper["Average_Marks"])
    print("Lowest:", lowest["Name"], "-", lowest["Average_Marks"])
    print("Passed:", passed)
    print("Failed:", failed)
    print("Pass percentage:", round(passed * 100 / len(df), 2), "%")

    # 5. Subject analysis
    heading("SUBJECT WISE PERFORMANCE")
    subjects = subject_summary(df)
    print(subjects.to_string(index=False))
    print("Best subject (by class average):",
          subjects.loc[subjects["Average_Marks"].idxmax(), "Subject"])

    # 6. High scorers
    heading("TOP STUDENTS (average >= 80)")
    high = ranked[ranked["Average_Marks"] >= 80]
    if high.empty:
        print("Nobody scored 80 or above.")
    else:
        print(high[["Student_ID", "Name", "Average_Marks", "Grade"]].to_string(index=False))

    # 7. Save
    df.to_csv(os.path.join(BASE_DIR, "student_results.csv"), index=False)
    subjects.to_csv(os.path.join(BASE_DIR, "subject_analysis.csv"), index=False)
    print("\nSaved student_results.csv and subject_analysis.csv")


if __name__ == "__main__":
    main()
