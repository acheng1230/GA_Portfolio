![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) 

Project 7: Airport Delays
----

### Overview
This week we learned we learned how to use scikit-learn to run linear regression models, how Goals & Business Objectives translate to Model Fit, and also how to optimize models using cross-validation. We worked a lot with housing data and predicting prices. Now we're going to use these skills to dig into a rich set of data!

#### Scenario 1: State tax board

You are a data scientist in residence at the Iowa State tax board. The Iowa State legislature is considering changes in the liquor tax rates and wants a report of current liquor sales by county and projections for the rest of the year.

**Goal for Scenario #1:** Your task is as follows:

* Calculate the yearly liquor sales for each score using the provided data. You can add up the transactions for each year, and store sales in 2015 specifically will be used later as your target variable.
* Use the data from 2015 to make a linear model using as many variables as you find useful to predict the yearly sales of each store. You must use the sales from Jan to March per store as one of your variables.
* Use your model for 2015 to estimate total sales for each store in 2016, extrapolating from the sales so far for Jan-March of 2016.
* Report your findings, including any projected increase or decrease in total sales (over the entire state) for the tax committee of the Iowa legislature.
* Use cross-validation to check how your model predicts to held out data compared to the model metrics on the full dataset.
* Use cross-validation to tune the regularization parameter that maximizes R^2 on your holdout sets for the Ridge regression and the Lasso Regression. Do the regularized models perform better than the non-regularized model? Which regularized model performs better? What is the Ridge regression doing? What is the Lasso doing?


#### Scenario 2: Market research for new store locations

A liquor store owner in Iowa is looking to expand to new locations and has hired you to investigate the market data for potential new locations. The business owner is interested in the details of the best model you can fit to the data so that his team can evaluate potential locations for a new storefront.

**Goal for Scenario #2:** Your task is to:

* Build models of total sales based on location, price per bottle, total bottles sold. You may find it useful to build models for each county, zip code, or city.
* Provide a table of the best performing stores by location type of your choice (city, county, or zip code) and the predictions of your model(s).
* Based on your models and the table of data, recommend some general locations to the business owner, taking into account model performance. Validate your model's performance and ability to predict future sales using cross-validation.
* _Bonus_: Recommend targets for volume sold and price per bottle!




### Suggested Ways to Get Started

**Tips for both scenarios:**
1. Likely you will find it useful to reduce the data set with pandas before fitting models. You may want to make a new table with the following data for each store:
 * The vendor name
 * The location data (zip code, county, city)
 * The total sales for the year
 * The total sales for each month (or at least for Jan-March for the first scenario)
 * The total volume sold
 * The total number of bottles sold
 * The average price per bottle (perhaps useful for distinguishing store types)

2. We're using linear regression for our models. Find the best model you can, but don't fret if you cannot get a really good model. We'll learn techniques later that will help improve your analysis, such as _classifying store types_. For now do the best you can with the tools that you have.

3. Take advantage of pandas as much as possible -- the `groupby`, `summation`, and other features of DataFrames can make computing the necessary summary data much easier. This is a great time to practice what you learned in Week 2!

4. Take care in the presentation of your results. Your audience is likely non-technical, so explain your findings in accessible language.

**General suggestions:**
- Write pseudocode before you write actual code. Thinking through the logic of something helps.  
- Read the docs for whatever technologies you use. Most of the time, there is a tutorial that you can follow, but not always, and learning to read documentation is crucial to your success!
- Document **everything**.  

### Useful Resources
- [Documentation for SKLearn](http://scikit-learn.org/stable/user_guide.html)
- [What is regularization?](https://www.quora.com/What-is-regularization-in-machine-learning)

---



