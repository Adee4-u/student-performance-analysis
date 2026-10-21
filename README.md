# Student Performance Analysis System

A Python project built with **NumPy** and **Pandas** that turns a simple list of marks into clear, ready-to-read results with no manual calculation.

Marks are often kept in a register or a spreadsheet, and totals, averages, grades and pass or fail status are then worked out by hand. This takes time, and a single small mistake can change a student's result. This program reads marks from a CSV file and calculates everything automatically for every student, then produces a ranked result list, a class summary, a subject-wise comparison and a list of high scorers.

## Features

| Feature | What it does |
|---|---|
| File check | Displays a clear message instead of crashing when `students.csv` is missing |
| Data checks | Reports missing columns and invalid marks before any calculation starts |
| `add_totals()` | Calculates total and average marks using NumPy |
| `get_grade()` | Assigns each student a grade from A+ to F |
| `get_result()` | Decides Pass or Fail based on marks and attendance |
| `subject_summary()` | Returns the average, highest and lowest mark of every subject |
| Ranking | Lists all students from the highest to the lowest average |
| Class summary | Shows the class average, topper, lowest scorer and pass percentage |
| High scorers | Lists students with an average of 80 or above |
| Saved output | Saves the results to two CSV files |

## Technologies Used

- **Python** – the language the entire project is written in
- **Pandas** – loading the CSV, adding new columns, sorting, filtering and saving results
- **NumPy** – adding up and averaging each student's marks
- **CSV files** – input data and saved output
- **Git and GitHub** – version control and submission
- **VS Code** – writing and running the code

## Project Structure

```
student-performance-analysis/
├── main.py                 # Runs the program from start to finish
├── functions.py            # Helper functions used by main.py
├── students.csv            # Input data (15 students)
├── student_results.csv     # Output: full results (created on run)
├── subject_analysis.csv    # Output: subject table (created on run)
└── README.md
```

## Dataset

`students.csv` contains records for 15 students, with one row per student.

| Column | What it holds |
|---|---|
| Student_ID | A unique ID for each student (2501 to 2515) |
| Name | The student's full name |
| Department | CSE, IT or ECE |
| Python | Marks out of 100 |
| Web Development | Marks out of 100 |
| Cyber Security | Marks out of 100 |
| Cloud Computing | Marks out of 100 |
| Attendance | Attendance in percent |

Four more columns are added by the program as it runs: `Total_Marks`, `Average_Marks`, `Grade` and `Result`.

## How It Works

1. **Loading and checking the file.** `main.py` confirms that `students.csv` is in the same folder and shows a message if it is missing or empty. It then checks that every required column is present and that all marks and attendance values are valid numbers from 0 to 100.
2. **Totals and averages.** `add_totals()` selects the four subject columns, converts them into a NumPy array, and calculates the sum and average of each row. The average is rounded to two decimal places.
3. **Grade and result.** `get_grade()` turns the average into a grade, and `get_result()` is applied to each row to decide Pass or Fail.
4. **Ranking.** Students are sorted by average marks, from highest to lowest.
5. **Class summary.** The program works out the class average, finds the top and lowest scorers with `idxmax()` and `idxmin()`, and counts the passes and fails to get the pass percentage.
6. **Subject analysis.** `subject_summary()` returns the average, highest and lowest mark for each subject, and the best subject by class average is displayed.
7. **High scorers.** Students whose average is 80 or above are listed. If nobody reaches 80, a message is shown instead.
8. **Saving.** The complete results are written to `student_results.csv` and the subject table to `subject_analysis.csv`.

### Grading Scale

| Average | Grade |
|---|---|
| 90 and above | A+ |
| 80 and above | A |
| 70 and above | B |
| 60 and above | C |
| 50 and above | D |
| Below 50 | F |

### Pass / Fail Rule

A student is marked Pass only if **every subject mark is at least 40** and **attendance is at least 40%**. A student can have a good average and still fail if one subject or attendance falls below the limit.

## Changing the Subjects

Subject names are kept in one list at the top of `functions.py`. To use different subjects, edit this list and make sure the column names in `students.csv` match it exactly:

```python
SUBJECTS = ["Python", "Web Development", "Cyber Security", "Cloud Computing"]
```

## Getting Started

### Prerequisites

- Python 3
- Pandas and NumPy

```bash
pip install pandas numpy
```

### Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Adee4-u/student-performance-analysis.git
   cd student-performance-analysis
   ```
2. Make sure `students.csv` is in the same folder as `main.py`.
3. Run the program:
   ```bash
   python main.py
   ```

## Sample Results

For the 15 students in the dataset:

- **Class average:** 69.03
- **Pass percentage:** 73.33% (11 passed, 4 failed)
- **Highest average:** 83.75, scored by Dev Malhotra (grade A)
- **Lowest average:** 53.25
- **Students with an average of 80 or above:** 2
- **Best subject:** Cyber Security, with a class average of 75.60

| Subject | Average | Highest | Lowest |
|---|---|---|---|
| Python | 61.60 | 99 | 33 |
| Web Development | 71.93 | 99 | 42 |
| Cyber Security | 75.60 | 99 | 48 |
| Cloud Computing | 67.00 | 99 | 35 |

## What I Learned

Working with data in Pandas, calculating with NumPy arrays, sorting and filtering a DataFrame, writing reusable functions, organising a project across multiple files and uploading it to GitHub.

## Author

**Mir Adnan Sadiq**
B.Tech, 6th Semester, CSE
Government College of Engineering & Technology, Safapora, Ganderbal

Submitted to Chandini Madam on 20/10/2026.
