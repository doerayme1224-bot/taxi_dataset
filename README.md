# Taxi Ride, Distance Analysis
## Project Purpose
The purpose of this project is to develop a model which can predict the distance you would make with a taxi ride, based on how much you would pay. This could be used as a model on an app, which could offer users a clear way understand how far they could go with the amount of money that they have.
## Data Dictionary
| Column name            |Description|
|-------------------|----------|
|pickup	       | The date and time the trip started.|
|dropoff	       | The date and time the trip ended.|
|passengers	   | The number of passengers for the trip.|
|distance	  |  The distance of the trip in miles.|
|fare	       | The initial fare calculated by the meter.|
|tip	          |  The tip amount paid.|
|tolls	       | The total amount of tolls paid.|
|total	       | The total cost of the trip, including fare, tip, and tolls.|
|color	       | The color of the taxi, either 'yellow' or 'green'.|
|payment	       | The method of payment, such as 'credit card' or 'cash'.|
|pickup_zone	 |   The name of the taxi zone for the pickup location.|
|dropoff_zone	|The name of the taxi zone for the drop-off location.|
|pickup_borough|	The name of the borough for the pickup location.|
|dropoff_borough|	The name of the borough for the drop-off location.|
## Summary
### Handling NaN Values and Outliers
- I handled NaN values by...
1. dropping them, I didn't want synthetic data to manipulate the performance of my model
**EX:**
```python
#1: dropping all the na values and saving them in a variable
sub = df.dropna()
#2: turning that subset into a csv with `to_csv`
sub.to_csv('data/cleaned_universities.csv')
```
**important to convert to a csv for later ease of use.**
### key visuals
#### 1. A heatmap of Correlations of In-State Tuition
![heatmap of correlation](Model_Visuals/correlation_of_tuition_and_features.png)
**a heatmap which shows the correlations between different numerical columns, this was helpful when it came to selecting features in order to create the model**
#### 2. A Scatterplot of Tuition and Board Costs
![Scatter plot](Model_Visuals/in_state_tuition_by_board.png) 
**a scatterplot that shows the cost of in-state tuition by the board cost, and they are grouped by wether the school is public or private. shows us that public schools have lower in-state tuition costs than private schools, but the cost betwen the Board isn't to different between public and private schools (private schools do however appear to have a higher board cost on average compared to public schools)**
#### 3. A Scatterplot of Tuition and Student Faculty Ratio's
![scatter plot 2](Model_Visuals/in_state_tuition_by_student_faculty_ratio.png) 
**A Scatterplot showing the cost of in-state tuition by the student faculty ratio, and they are grouped by wether the school is public or private. Shows us that schools with higher student faculty ratio's tend to have lower in-state tuition costs. also private schools seem to have lower student facult ratio's then public schools (but there are some outliers)**
## Model Performance
### Feature Selection
**I decided to chose these features...**
1. Public (1)/ Private (2)
2. board
3. Graduation rate
4. % new stud. from top 10%
5. % new stud. from top 25%
6. room
7. stud./fac. ratio
I chose them as they correlated strongly with the target variable (In-State Tuition) with about being *HEAVILY* related (Like the out-of-state tuition).
### Model Selection
**I chose several models...**
1. Linear Regression
2. Decission Tree Regressor
3. Random Forest Regressor
4. K Nearest Neighbors Regressor
**chose these because i'm used to using them**
### Evaluation Metrics

| Model             | RMSE     | R²       |MAPE|
|-------------------|----------|----------|------|
| Linear Regressor |1802.64$|89.551%|26.774%|
|Decission Tree Regressor|2612.58$|78.051%|33.512%|
|Random Forest Regressor|1809.52$|89.558%|23.016%|
|K Nearest Neighbor Regressor|1864.03$|87.077%|63.990%|
### pickling
I chose to pickle the random forest model as it had the best R squared score and the best MAPE score. while its rmse was worse then linear regression, it wasn't worse by much, which ads to the reason as to why I chose the randome forest model to pickle
## conclusion
#### my analysis was able to create a model that is effecctive at developing predictions, it could be used to...
1. forecast the price of future higher eduaction projects
2. be used to estimate future prices of pre-existing schools by plugging in projected values