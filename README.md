# Student Performance Analysis System

A Python project built with **NumPy** and **Pandas** that turns a plain list of marks into clear results, without any manual calculation.

Teachers usually keep marks in a register or a spreadsheet and work out totals, averages, grades and pass or fail by hand. That is slow, and one small slip changes a student's result. This program reads the marks from a CSV file and calculates everything automatically. It then prints a ranked result list, a class summary, a subject-wise comparison and a list of high scorers.

## Features

| Feature | What it does |
|---|---|
| File check | Shows a clear message if `students.csv` is missing instead of crashing |
| `add_totals()` | Adds total and average marks using NumPy |
| `get_grade()` | Gives each student a grade from A+ to F |
| `get_result()` | Decides Pass or Fail using marks and attendance |
| `subject_summary()` | Gives the average, highest and lowest mark of every subject |
| Ranking | Lists all students from best to lowest average |
| Class summary | Shows the class average, topper, lowest scorer and pass percentage |
| High scorers | Lists students with an average of 80 or more |
| Saved output | Writes the results to two CSV files |

## Changing the Subjects

Subject names are kept in one list at the top of `functions.py`. To use different subjects, edit this list and make sure the column names in `students.csv` match it exactly:

```python
SUBJECTS = ["Data Structures", "Operating Systems", "Computer Networks", "Machine Learning"]
```

## Technologies Used

- **Python** – the language the whole project is written in
- **Pandas** – loading the CSV, creating new columns, sorting, filtering and saving results
- **NumPy** – summing and averaging each student's marks, and calculating subject averages
- **CSV files** – input data and saved output
- **Git and GitHub** – version control and submission
- **VS Code** – writing and running the code

## Project Structure

```
student-performance-analysis/
├── main.py                 # Runs the program from start to end
├── functions.py            # Helper functions used by main.py
├── students.csv            # Input data (21 students)
├── student_results.csv     # Output: full results (created on run)
├── subject_analysis.csv    # Output: subject table (created on run)
└── README.md
```

## Dataset

`students.csv` holds records of 21 students, one row per student.

| Column | What it holds |
|---|---|
| Student_ID | A unique ID for each student (2401 to 2421) |
| Name | The student's name |
| Department | CSE, IT or ECE |
| Data Structures | Marks out of 100 |
| Operating Systems | Marks out of 100 |
| Computer Networks | Marks out of 100 |
| Machine Learning | Marks out of 100 |
| Attendance | Attendance in percent |

The program adds four more columns while it runs: `Total_Marks`, `Average_Marks`, `Grade` and `Result`.

## How It Works

1. **Loading the file.** `main.py` checks that `students.csv` is in the same folder and prints a message if it is not. Otherwise it reads the file with `pd.read_csv()` and shows the student count, column names and first five rows.
2. **Totals and averages.** `add_totals()` picks the four subject columns, converts them to a NumPy array, and sums and averages each row. The average is rounded to two decimal places.
3. **Grade and result.** `get_grade()` converts the average into a grade, and `get_result()` is applied to every row to decide Pass or Fail.
4. **Ranking.** Students are sorted by average marks, highest first, and shown with total, average, grade, attendance and result.
5. **Class summary.** Finds the class average, the highest and lowest scorers (using `idxmax()` and `idxmin()`), the number of passes and fails, and the pass percentage.
6. **Subject analysis.** `subject_summary()` returns the average, highest and lowest mark of each subject, and the subject with the best class average is printed.
7. **High scorers.** Students with an average of 80 or more are filtered and listed.
8. **Saving.** Full results go to `student_results.csv` and the subject table to `subject_analysis.csv`.

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

A student passes only when **every subject mark is 40 or more** and **attendance is 40% or more**. A student can have a good average and still fail if one subject or attendance falls below the limit.

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
   git clone https://github.com/bushrazahgeer/student-performance-analysis.git
   cd student-performance-analysis
   ```
2. Make sure `students.csv` is in the same folder as `main.py`.
3. Run the program:
   ```bash
   python main.py
   ```

## Sample Results

For the 21 students in the dataset:

- **Class average:** 67.20
- **Pass percentage:** 76.19% (16 passed, 5 failed)
- **Highest average:** 91.00, scored by Zoya Verma (grade A+)
- **Lowest average:** 51.50
- **Students with an average of 80 or more:** 1
- **Best subject:** Computer Networks, with a class average of 70.86

| Subject | Average | Highest | Lowest |
|---|---|---|---|
| Data Structures | 61.43 | 93 | 32 |
| Operating Systems | 67.00 | 94 | 34 |
| Computer Networks | 70.86 | 96 | 45 |
| Machine Learning | 69.52 | 97 | 51 |

## What I Learned

Working with data in Pandas, calculating with NumPy arrays, sorting and filtering a DataFrame, writing reusable functions, organising a project across multiple files and uploading it to GitHub.

## Author

**Owais**
B.Tech, 6th Semester, CSE
Government College of Engineering & Technology, Safapora, Ganderbal

Submitted to Chandini Madam on 20/10/2026.
