import numpy as np
import pandas as pd

# Change the subject names here if your CSV uses different ones.
SUBJECTS = ["Data Structures", "Operating Systems", "Computer Networks", "Machine Learning"]


def add_totals(df):
    """Add Total_Marks and Average_Marks using a NumPy array of the subject columns."""
    marks = df[SUBJECTS].to_numpy()
    df["Total_Marks"] = marks.sum(axis=1)
    df["Average_Marks"] = np.round(marks.mean(axis=1), 2)
    return df


def get_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    return "F"


def get_result(row):
    """Pass only if every subject mark is 40+ and attendance is 40%+."""
    if all(row[s] >= 40 for s in SUBJECTS) and row["Attendance"] >= 40:
        return "Pass"
    return "Fail"


def subject_summary(df):
    """Average, highest and lowest mark of each subject."""
    return pd.DataFrame({
        "Subject": SUBJECTS,
        "Average_Marks": [round(df[s].mean(), 2) for s in SUBJECTS],
        "Highest_Mark": [df[s].max() for s in SUBJECTS],
        "Lowest_Mark": [df[s].min() for s in SUBJECTS],
    })