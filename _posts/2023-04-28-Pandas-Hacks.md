---
keywords: fastai
description: Hacks!!
title: Petite Pandas Data Analysis using Pandas and NumPy Hacks
toc: true
categories: [Other Projects]
comments: true
nb_path: _notebooks/2023-28-04-Pandas-Hacks.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2023-28-04-Pandas-Hacks.ipynb
-->

<div class="container" id="notebook-container">
        
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Popcorn-Hacks:">Popcorn Hacks:<a class="anchor-link" href="#Popcorn-Hacks:"> </a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Predictive analysis is the use of <strong>statistical</strong>, data mining, and machine learning techniques to analyze current and historical data in order to make predictions about future events or behaviors. It involves identifying <strong>patterns</strong> and trends in data, and then using that information to forecast what is likely to happen in the future.</p>
<p>Predictive analysis is used in a wide range of applications, from forecasting sales and demand, to predicting customer behavior, to detecting fraudulent transactions. It involves collecting and analyzing data from a variety of sources, including historical data, customer data, financial data, and social media data, among others.</p>
<p>The process of predictive analysis typically involves the following steps:</p>
<ol>
<li>Defining the problem and identifying the relevant data sources</li>
<li><strong>Collecting and cleaning the data</strong></li>
<li>Exploring and analyzing the data to identify patterns and trends</li>
<li>Selecting an appropriate model or algorithm to use for predictions</li>
<li>Training and validating the model using historical data</li>
<li><strong>Using the model to make predictions on new data</strong></li>
<li>Monitoring and evaluating the performance of the model over time</li>
</ol>
<p>Predictive analysis can help organizations make more informed decisions, improve efficiency, and gain a competitive advantage by leveraging insights from data.</p>
<p>It is most commonly used in <strong>Retail</strong>, where workers try to predict which products would be most popular and try to advertise those products as much as possible, and also <strong>Healthcare</strong>, where algorithms analyze patterns and reveal prerequisites for diseases and suggest preventive treatment, predict the results of various treatments and choose the best option for each patient individually, and predict disease outbreaks and epidemics.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>An array is the central <strong>data structure</strong> of the NumPy library. They are used as <strong>containers</strong> which are able to store more than one item at the same time. Using the function <code>np.array</code> is used to create an array, in which you can create multidimensional arrays.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="c1"># create 3D array here</span>
<span class="n">x</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([[[</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">],</span> <span class="p">[</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">3</span><span class="p">]],</span> <span class="p">[[</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">],</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">]]])</span>
<span class="nb">print</span><span class="p">(</span><span class="n">x</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>(2, 2, 3)
[[[1 1 2]
  [2 3 3]]

 [[1 1 1]
  [1 1 1]]]
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="3.-Basic-array-operations">3. Basic array operations<a class="anchor-link" href="#3.-Basic-array-operations"> </a></h3><p>One of the most basic operations that can be performed on arrays is <strong>arithmetic operations</strong>. With numpy, it is very easy to perform arithmetic operations on arrays. You can <strong>add</strong>, <strong>subtract</strong>, <strong>multiply</strong> and <strong>divide</strong> arrays, just like you would with regular numbers. When performing these operations, numpy applies the operation element-wise, meaning that it performs the operation on each element in the array separately. This makes it easy to perform operations on large amounts of data quickly and efficiently.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">a</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">])</span>
<span class="n">b</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">])</span>

<span class="c1"># calculate sin</span>
<span class="n">f</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="n">b</span><span class="p">)</span>
<span class="c1"># calculate cos</span>
<span class="n">g</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="n">b</span><span class="p">)</span>
<span class="c1"># calculate tan</span>
<span class="n">h</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">tan</span><span class="p">(</span><span class="n">b</span><span class="p">)</span>
<span class="c1"># calculate natural log</span>
<span class="n">i</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="n">b</span><span class="p">)</span>
<span class="c1"># calculate log10</span>
<span class="n">j</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">log10</span><span class="p">(</span><span class="n">b</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">g</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">h</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">j</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>[-0.7568025  -0.95892427 -0.2794155 ]
[-0.65364362  0.28366219  0.96017029]
[ 1.15782128 -3.38051501 -0.29100619]
[1.38629436 1.60943791 1.79175947]
[0.60205999 0.69897    0.77815125]
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="4.-Data-analysis-using-numpy">4. Data analysis using numpy<a class="anchor-link" href="#4.-Data-analysis-using-numpy"> </a></h3><p>Numpy provides a convenient and powerful way to perform data analysis tasks on <strong>large datasets</strong>. One of the most common tasks in data analysis is finding the <strong>mean</strong>, <strong>median</strong>, and <strong>standard deviation</strong> of a dataset. Numpy provides functions to perform these operations quickly and easily. The mean function calculates the average value of the data, while the median function calculates the middle value in the data. The standard deviation function calculates how spread out the data is from the mean. Additionally, numpy provides functions to find the minimum and maximum values in the data. These functions are very useful for gaining insight into the properties of large datasets and can be used for a wide range of data analysis tasks.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">data</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">2</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">12</span><span class="p">,</span> <span class="mi">13</span><span class="p">,</span> <span class="mi">19</span><span class="p">])</span>

<span class="c1"># create a different way of solving the sum or products of a dataset from what we learned above</span>
<span class="nb">print</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">sum</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">product</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>51
29640
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Main-Hack:">Main Hack:<a class="anchor-link" href="#Main-Hack:"> </a></h1>
</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="n">age</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">loadtxt</span><span class="p">(</span><span class="s1">&#39;files/age.csv&#39;</span><span class="p">,</span> <span class="n">delimiter</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="nb">str</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;utf-8&#39;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">age</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>[&#39;Age&#39; &#39;18&#39; &#39;19&#39; &#39;20&#39; &#39;21&#39; &#39;22&#39; &#39;23&#39; &#39;24&#39; &#39;25&#39; &#39;26&#39; &#39;27&#39; &#39;28&#39; &#39;29&#39; &#39;30&#39;]
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Panda:">Panda:<a class="anchor-link" href="#Panda:"> </a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><strong>Min:</strong></p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">age</span><span class="o">=</span> <span class="p">[</span><span class="mi">18</span><span class="p">,</span> <span class="mi">19</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">21</span><span class="p">,</span> <span class="mi">22</span><span class="p">,</span> <span class="mi">23</span><span class="p">,</span> <span class="mi">24</span><span class="p">,</span> <span class="mi">25</span><span class="p">,</span> <span class="mi">26</span><span class="p">,</span> <span class="mi">27</span><span class="p">,</span> <span class="mi">28</span><span class="p">,</span> <span class="mi">29</span><span class="p">,</span> <span class="mi">30</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">min</span><span class="p">(</span><span class="n">age</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>18
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><strong>Max:</strong></p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">age</span><span class="o">=</span> <span class="p">[</span><span class="mi">18</span><span class="p">,</span> <span class="mi">19</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">21</span><span class="p">,</span> <span class="mi">22</span><span class="p">,</span> <span class="mi">23</span><span class="p">,</span> <span class="mi">24</span><span class="p">,</span> <span class="mi">25</span><span class="p">,</span> <span class="mi">26</span><span class="p">,</span> <span class="mi">27</span><span class="p">,</span> <span class="mi">28</span><span class="p">,</span> <span class="mi">29</span><span class="p">,</span> <span class="mi">30</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">max</span><span class="p">(</span><span class="n">age</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>30
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Numpy:">Numpy:<a class="anchor-link" href="#Numpy:"> </a></h3>
</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="c1"># Generate a single random number</span>
<span class="n">random_number</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">rand</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">random_number</span><span class="p">)</span>

<span class="c1"># Generate an array of random numbers</span>
<span class="n">random_array</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">rand</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>  <span class="c1"># Generates an array of 5 random numbers</span>
<span class="nb">print</span><span class="p">(</span><span class="n">random_array</span><span class="p">)</span>

<span class="c1"># Generate a 2D array of random numbers</span>
<span class="n">random_matrix</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">rand</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>  <span class="c1"># Generates a 3x2 matrix of random numbers</span>
<span class="nb">print</span><span class="p">(</span><span class="n">random_matrix</span><span class="p">)</span>

<span class="c1"># Generate random integers within a specific range</span>
<span class="n">random_int</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>  <span class="c1"># Generates a random integer between 1 and 10 (inclusive)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">random_int</span><span class="p">)</span>

<span class="c1"># Generate an array of random integers within a specific range</span>
<span class="n">random_int_array</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span>  <span class="c1"># Generates an array of 5 random integers between 1 and 10 (inclusive)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">random_int_array</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>0.22694578746731575
[0.90154584 0.14164067 0.1356398  0.17760852 0.8175945 ]
[[0.35257292 0.22036514]
 [0.90568225 0.00206035]
 [0.5691113  0.27038592]]
58
[8 3 9 2 4]
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="n">array</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([[[</span><span class="mi">1</span><span class="p">,</span><span class="mi">11</span><span class="p">,</span><span class="mi">2</span><span class="p">],</span> <span class="p">[</span><span class="mi">2</span><span class="p">,</span><span class="mi">13</span><span class="p">,</span><span class="mi">3</span><span class="p">]],</span> <span class="p">[[</span><span class="mi">1</span><span class="p">,</span><span class="mi">10</span><span class="p">,</span><span class="mi">1</span><span class="p">],</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">]]])</span>
<span class="nb">print</span><span class="p">(</span><span class="n">array</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>(2, 2, 3)
[[[ 1 11  2]
  [ 2 13  3]]

 [[ 1 10  1]
  [ 1  1  1]]]
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="n">linear_array</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">15</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">linear_array</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>[ 0.          1.42857143  2.85714286  4.28571429  5.71428571  7.14285714
  8.57142857 10.         11.42857143 12.85714286 14.28571429 15.71428571
 17.14285714 18.57142857 20.        ]
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

</div>
 
