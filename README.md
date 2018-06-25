## Glassdoor Crawler to extract job information.
The program extracts and writes to CSV file the following information: title job, local, company name, salary and description. In this project was used data-science jobs, but can be used for other jobs.

## Requirements
- Python

Packages :
- scrapy
- scrapy-splash
- bs4

## Steps
1. After downloading the files, access glassdoor.py and paste the url into start_urls (optional).
2. Run on the python console (In the project folder):
scrapy crawl glassdoor
3. Access booksdata.csv to explore the results.

Example
``````
title,local,company_name,salary,description

Data Scientist Partner Services, Los Angeles CA, Factual,$159.000,At Factual we love all things data Our mission is to organize and
interpret the worlds location information As a Data Scientist on our Partner Services team you will have the opportunity to work directly 
with our customers to query filter aggregate analyze explain and visualize what is happening in the physical world About you You are a 
data scientist who knows the tools and algorithms to analyze data and understands how to find its shape and underlying structure Working 
on the Partner Services team youll apply analytics to bridge the gap between Factuals established products and the huge variety of 
questions were trying to answer You are a skilled communicator that will provide compelling and appropriate explanation and guidance to 
critical existing and potential customers You have strong engineering experience and enjoy working in a rapidly changing environment And 
most of all you ship What youll do Analyze interpret and solve a range of location data problems Design experiments and work with fellow 
engineers to ensure thoroughness and correctness on a variety of analyses Use and provide feedback to our data processing software and 
frameworks Develop visualizations based on bespoke data analysis challenges Author specifications and lead technical projects Propose 
creative strategies based on datadriven insights What were looking for Deep understanding of machine learning concepts and algorithms  
particularly classification clustering and supervised learning Expertise with PythonScalaJava Familiarity with distributed programming 
with Spark or MapReduce Applied knowledge of Statistics we really value people who can handle uncertainty and variance Willingness and 
ability to wrangle messy data An advanced degree in a quantitative field Math Statistics Computer Science Excellent oral and written 
communication skills Industry experience maintaining production data pipelines and using data science to solve business problems is a plus 
Cover letters will be greatly appreciated Thanks
``````

This is a simple project to capture web information, it can be used for statistical data and text mining. In the next part (Part 2) will make an exploration of texts analyzing the frequency of keywords that appear in job descriptions using pandas, wordcloud and ntlk.
