This is some examples of using Plotly/Dash and Parquet.

Demonstration so far:
1. Plot two lines on the same plot

2. Make a histogram

3. Able to deal with >32 bit numbers
   * the scatter plot itself couldn't handle >32 bit numbers AFAICT

   * Plotting log2 of the numbers was fine

   * the Parquet write/read routines handled uint64's just fine

4. Write/read compressed binary parquet files

Here's a screenshot of the interactive browser graphs:
![screenshot](/screenshot.png)
Format: ![Alt Text](url)
