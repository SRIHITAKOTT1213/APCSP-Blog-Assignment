---
keywords: fastai
description: Python Lists
title: Python Lists
permalink: /Python/Lists
categories: [1.A, 3.A, 4.B]
toc: true
comments: true
nb_path: _notebooks/2022-09-04-Python-Lists.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2022-09-04-Python-Lists.ipynb
-->

<div class="container" id="notebook-container">
        
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>{% include nav_frontend.html %}</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># variable of type string</span>
<span class="n">name</span> <span class="o">=</span> <span class="s2">&quot;Sri Kotturi&quot;</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;name&quot;</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="n">name</span><span class="p">))</span>

<span class="c1"># variable of type integer</span>
<span class="n">age</span> <span class="o">=</span> <span class="mi">16</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;age&quot;</span><span class="p">,</span> <span class="n">age</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="n">age</span><span class="p">))</span>

<span class="c1"># variable of type float</span>
<span class="n">score</span> <span class="o">=</span> <span class="mf">90.0</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;score&quot;</span><span class="p">,</span> <span class="n">score</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="n">score</span><span class="p">))</span>

<span class="nb">print</span><span class="p">()</span>

<span class="c1"># variable of type list (many values in one variable)</span>
<span class="n">langs</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;Python&quot;</span><span class="p">,</span> <span class="s2">&quot;JavaScript&quot;</span><span class="p">,</span> <span class="s2">&quot;Java&quot;</span><span class="p">,</span> <span class="s2">&quot;Bash&quot;</span><span class="p">,</span> <span class="s2">&quot;html&quot;</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;langs&quot;</span><span class="p">,</span> <span class="n">langs</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="n">langs</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;- langs[2]&quot;</span><span class="p">,</span> <span class="n">langs</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span> <span class="nb">type</span><span class="p">(</span><span class="n">langs</span><span class="p">[</span><span class="mi">2</span><span class="p">]))</span>

<span class="nb">print</span><span class="p">()</span>

<span class="c1"># variable of type dictionary (a group of keys and values)</span>
<span class="n">person</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="n">name</span><span class="p">,</span>
    <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="n">age</span><span class="p">,</span>
    <span class="s2">&quot;score&quot;</span><span class="p">:</span> <span class="n">score</span><span class="p">,</span>
    <span class="s2">&quot;langs&quot;</span><span class="p">:</span> <span class="n">langs</span>
<span class="p">}</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;person&quot;</span><span class="p">,</span> <span class="n">person</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="n">person</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;- person[&quot;name&quot;]&#39;</span><span class="p">,</span> <span class="n">person</span><span class="p">[</span><span class="s2">&quot;name&quot;</span><span class="p">],</span> <span class="nb">type</span><span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s2">&quot;name&quot;</span><span class="p">]))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>name Sri Kotturi &lt;class &#39;str&#39;&gt;
age 16 &lt;class &#39;int&#39;&gt;
score 90.0 &lt;class &#39;float&#39;&gt;

langs [&#39;Python&#39;, &#39;JavaScript&#39;, &#39;Java&#39;, &#39;Bash&#39;, &#39;html&#39;] &lt;class &#39;list&#39;&gt;
- langs[2] Java &lt;class &#39;str&#39;&gt;

person {&#39;name&#39;: &#39;Sri Kotturi&#39;, &#39;age&#39;: 16, &#39;score&#39;: 90.0, &#39;langs&#39;: [&#39;Python&#39;, &#39;JavaScript&#39;, &#39;Java&#39;, &#39;Bash&#39;, &#39;html&#39;]} &lt;class &#39;dict&#39;&gt;
- person[&#34;name&#34;] Sri Kotturi &lt;class &#39;str&#39;&gt;
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">InfoDb</span> <span class="o">=</span> <span class="p">[]</span>

<span class="c1"># Append to List a Dictionary of key/values related to a person and cars</span>
<span class="n">InfoDb</span><span class="o">.</span><span class="n">append</span><span class="p">({</span>
    <span class="s2">&quot;FirstName&quot;</span><span class="p">:</span> <span class="s2">&quot;Srihita&quot;</span><span class="p">,</span>
    <span class="s2">&quot;LastName&quot;</span><span class="p">:</span> <span class="s2">&quot;Kotturi&quot;</span><span class="p">,</span>
    <span class="s2">&quot;DOB&quot;</span><span class="p">:</span> <span class="s2">&quot;December 13&quot;</span><span class="p">,</span>
    <span class="s2">&quot;Residence&quot;</span><span class="p">:</span> <span class="s2">&quot;San Diego&quot;</span><span class="p">,</span>
    <span class="s2">&quot;Email&quot;</span><span class="p">:</span> <span class="s2">&quot;srihita.kotturi@gmail.com&quot;</span><span class="p">,</span>
    <span class="s2">&quot;Owns_Cars&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;Hundai Accent&quot;</span><span class="p">],</span>
    <span class="s2">&quot;Favorite_Activity&quot;</span><span class="p">:</span> <span class="s2">&quot;Watching TV!&quot;</span>
    
    
    
<span class="p">})</span>


<span class="nb">print</span><span class="p">(</span><span class="n">InfoDb</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>[{&#39;FirstName&#39;: &#39;Srihita&#39;, &#39;LastName&#39;: &#39;Kotturi&#39;, &#39;DOB&#39;: &#39;December 13&#39;, &#39;Residence&#39;: &#39;San Diego&#39;, &#39;Email&#39;: &#39;srihita.kotturi@gmail.com&#39;, &#39;Owns_Cars&#39;: [&#39;Hundai Accent&#39;], &#39;Favorite_Activity&#39;: &#39;Watching TV!&#39;}]
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">print_data</span><span class="p">(</span><span class="n">d_rec</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">d_rec</span><span class="p">[</span><span class="s2">&quot;FirstName&quot;</span><span class="p">],</span> <span class="n">d_rec</span><span class="p">[</span><span class="s2">&quot;LastName&quot;</span><span class="p">])</span>  <span class="c1"># using comma puts space between values</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">&quot;</span><span class="p">,</span> <span class="s2">&quot;Residence:&quot;</span><span class="p">,</span> <span class="n">d_rec</span><span class="p">[</span><span class="s2">&quot;Residence&quot;</span><span class="p">])</span> <span class="c1"># \t is a tab indent</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">&quot;</span><span class="p">,</span> <span class="s2">&quot;Birth Day:&quot;</span><span class="p">,</span> <span class="n">d_rec</span><span class="p">[</span><span class="s2">&quot;DOB&quot;</span><span class="p">])</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">&quot;</span><span class="p">,</span> <span class="s2">&quot;Cars: &quot;</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">)</span>  <span class="c1"># end=&quot;&quot; make sure no return occurs</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;, &quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">d_rec</span><span class="p">[</span><span class="s2">&quot;Owns_Cars&quot;</span><span class="p">]))</span>  <span class="c1"># join allows printing a string list with separator</span>
    <span class="nb">print</span><span class="p">()</span>


<span class="c1"># for loop iterates on length of InfoDb</span>
<span class="k">def</span> <span class="nf">for_loop</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;For loop output</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">InfoDb</span><span class="p">:</span>
        <span class="n">print_data</span><span class="p">(</span><span class="n">record</span><span class="p">)</span>

<span class="n">for_loop</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>For loop output

Srihita Kotturi
	 Residence: San Diego
	 Birth Day: December 13
	 Cars: Hundai Accent

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
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">while_loop</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;While loop output</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
    <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">InfoDb</span><span class="p">):</span>
        <span class="n">record</span> <span class="o">=</span> <span class="n">InfoDb</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
        <span class="n">print_data</span><span class="p">(</span><span class="n">record</span><span class="p">)</span>
        <span class="n">i</span> <span class="o">+=</span> <span class="mi">1</span>
    <span class="k">return</span>

<span class="n">while_loop</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>While loop output

Srihita Kotturi
	 Residence: San Diego
	 Birth Day: December 13
	 Cars: Hundai Accent

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
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">recursive_loop</span><span class="p">(</span><span class="n">i</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">InfoDb</span><span class="p">):</span>
        <span class="n">record</span> <span class="o">=</span> <span class="n">InfoDb</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
        <span class="n">print_data</span><span class="p">(</span><span class="n">record</span><span class="p">)</span>
        <span class="n">recursive_loop</span><span class="p">(</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
    <span class="k">return</span>
    
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Recursive loop output</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="n">recursive_loop</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>Recursive loop output

Srihita Kotturi
	 Residence: San Diego
	 Birth Day: December 13
	 Cars: Hundai Accent

</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

</div>
 

