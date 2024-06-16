# Class Hardware
## Mini Presentation

Through basic exploratory data analysis, we see some interesting results from the Class Hardware Survey. See classHardwareSurvey.py for visual representations.

## Quantitative Varibales
We see that:
- Students' CPU Cycle Rate is typically between 1 and 5, with large concentrations of values around 1.5, 2.25, and 3.25
- Students' CPU core counts tend to be between 1 and 10, with some having more. Large concentrations at around 4 and 9.
- Students' RAM values (in GB) tend to be slightly below 10, slightly below 10, or slightly above 30. With some outliers around 60
- Hard drive sizes (in GB) tend to be between 0 and 1000, with most of them being around 500 or lower. Some outliers have around 2000, 3000, or 4000 GB.
- Values for GPU CUDA Number of Cores range from 0 to 10000, with concentrations around 1000.

## Qualitative Variables
- UVA net ID and Github usernames serve as unique identifiers for our data points rather than providing useful data to work with.
- The vast majority are of students are usin MacOS (156) or Windows (128) operating systems, with 3 using Linux.
- There are a wide variety of different GPU names, likely due to the way in which the data was collected, allowing students to type the name of their GPU in the response form. We do, however, see that Intel(R) Iris(R) Xe Graphics, Apple M1, Intel(R) UHD Graphics 620, and Intel Iris Plus Graphics 1536 MB appear as some of the most common values.
