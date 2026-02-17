import numpy as np
import pandas as pd

students = [

{"name": "Alice", "score": 85},

{"name": "Bob", "score": 92},

{"name": "Charlie", "score": 78},

{"name": "David", "score": 90},

{"name": "Eva", "score": 88}

]
df = pd.DataFrame(students)
print(df)
mean=np.mean(df["score"])
print("Mean is:",mean)

median=np.median(df["score"])
print("Median is :",median)
print("Standard Deviation is:",np.std(df["score"]))