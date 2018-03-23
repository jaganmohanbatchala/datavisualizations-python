# datavisualizations-python

# Data Visualization 
### Usage of Python Visualisation Libraries

# Visualization \ Visualisation

It is any technique for creating images, diagrams, or animations to communicate a message.

Is Data scientist an artist ?

	* Data Sculpting to Shape Business Insights
	
	* They make paintings in form of digital visualization  (of data) 
   with a motive of manifesting  the hidden patterns / insights in it.
	
# Types of data visualizations
## Explanatory
The aim of explanatory visualizations is to tell stories—they’re carefully constructed to surface key findings.

## Exploratory
* Create an interface into a dataset … they facilitate the user exploring the data, letting them unearth their own insights.
* Exploratory visualizations are interactive. While there are many Python plotting libraries, only a handful can create interactive charts that you can embed online and distribute. 

**Python Visualisation Libraries**

   * **Matplotlib** 
   
   * **Pandas**
   
   * **ggpy** 
   
   * **Altair** 
   
   * **Seaborn** 
   
   * **Plotly** 
   
   * **Bokeh** 
   
   * **HoloViews** 
   
   * **VisPy** 
   
   * **Lightning**

# Python Vis Library - Matplotlib 
Matplotlib is a Python 2D plotting library which produces publication quality figures in a interactive environments across platforms.

*We can generate plots, histograms, power spectra, bar charts, errorcharts, scatterplots, etc., with just a few lines of code

'''
tries to make easy things easy and 
 hard things possible
'''
 
# Python Vis Library - seaborn
* Seaborn is a library for making attractive and informative statistical graphics in Python.
* Seaborn aims to make visualization a central part of exploring and understanding data.
* The plotting functions operate on dataframes and internally perform the necessary aggregation and  statistical model-fitting to produce informative plots

'''
tries to make a well-defined set of 
 hard things easy too
'''

# Python Vis Library - Altair
Altair is a declarative statistical visualization library for Python
We can generate plots, histograms, power spectra, bar charts, errorcharts, scatterplots, etc., with just a few lines of code
'''
produces beautiful and effective visualizations with a minimal amount of code
'''

* Pandas is handy for simple plots but you need to be willing to learn matplotlib to customize.

* Seaborn can support some more complex visualization approaches but still requires matplotlib knowledge to tweak. The color schemes are a nice bonus.

* ggplot has a lot of promise but is still going through growing pains.

* bokeh is a robust tool if you want to set up your own visualization server but may be overkill for the simple scenarios.

* pygal stands alone by being able to generate interactive svg graphs and png files. It is not as flexible as the matplotlib based solutions.

* Plotly generates the most interactive graphs. You can save them offline and create very rich web-based visualizations.

# Visualization methods
* Distribution
* Comparison
* Relationship
* Composition

## Distribution
It is commonly used at the initial stage of data exploration i.e. when we get started with understanding the variable. Variables are of two types: Continuous and Categorical. For continuous variable, we look at the centre, spread, outlier. For categorical variable we look at frequency table.
**Histogram**
It is used for showing the distribution of continuous variables

**Box-Plot**
It is used to display full range of variation from min to max and useful to identify outlier values.

## Comparison
It is used to compare values across different categories.
Common charts to represent these information are Bar and Line chart.

**Bar Chart**
It is used to compare values across different categories

**Line Chart**
It is used to compare values over quantitative variable.

## Composition
It is used to show distribution of a variable across categories of another variable

**Pie Chart**
It can be created by passing the values representing each of the slices of the pie.

## Relationship
It is widely used to understand the correlation between two or more continuous variables

**Scatter Plot**
It clearly shows the relationship between two variables

# Summary
* Plotting data in the python ecosystem is a good news/bad news story.

* Trying to figure out which ones works for you will depend on what you’re trying to accomplish
