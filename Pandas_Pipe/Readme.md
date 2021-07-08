# Read me

I downloaded a csv file about 80 cereal products with their dietary characteristics on <a href="https://perso.telecom-paristech.fr/eagan/class/igr204/datasets"> Project datasets.</a>

Here is the goal of this data analysis.

1. How many kinds of cereal each manufacturer has.
2. We want to find the best cereal for Sam. Sam's cereal should be protein >= 2, fat <=2, sugars <=7. Sam wants low calories and good rating as well. 

In this data analysis, I work with `pipe` in Pandas so that it is easy to find out what I have done in each code. This is also good when I want to redo something during analysing the data.

First, we analysed the data in the notebook <a href="https://github.com/Sieye-R/Python-the_very_first_step/blob/main/Pandas_Pipe/Pandas%20pipe%20pre%20work.ipynb">Pandas pipe pre work</a>.
After that, we separate it into two files so that it is easy to see the result at first glance.
The main file is <a href="https://github.com/Sieye-R/Python-the_very_first_step/blob/main/Pandas_Pipe/Result/result.ipynb">result.ipynb</a>.
Since we have many steps for pipes, we use logging here to check out the execution of each step. Logging and the pipes which are used in `result.ipynb` are saved in <a href="https://github.com/Sieye-R/Python-the_very_first_step/blob/main/Pandas_Pipe/Result/pipe.py">pipe.py</a>.


## References

To study Pandas Pipe, I watched <a href="https://calmcode.io/pandas-pipe/introduction.html">pandas-pipe tutorial in calmcode</a> and <a href="https://tomaugspurger.github.io/modern-1-intro.html">modern pandas</a>.

To study logging, I watched <a href="https://calmcode.io/logging/introduction.html"> logging tutorial in calmcode</a> and <a href="https://www.python-engineer.com/courses/advancedpython/10-logging/"> logging tutorial in Python Engineer</a>.

To study decorator, I watched <a href="https://calmcode.io/decorators/introduction.html">decorator tutorial in calmcode</a> and <a href="https://www.python-engineer.com/courses/advancedpython/13-decorators/">decorator tutorial in Python Engineer</a>.
