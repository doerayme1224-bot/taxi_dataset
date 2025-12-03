<div style="display: flex; align-items: center; justify-content: center; text-align: center;">
  <img src="https://coursereport-s3-production.global.ssl.fastly.net/uploads/school/logo/219/original/CT_LOGO_NEW.jpg" width="100" style="margin-right: 10px;">
  <div>
    <h1><b>[M6] 🧪 Lab - EDA Practice w/ Taxi Dataset</b></h1>
  </div>
</div>

<br>

In this assignment, you'll explore the taxi dataset using Seaborn. You'll dive into best practices for exploratory data analysis (EDA) while also providing a chance to apply and enhance data visualization skills.

### Loading the Taxi Dataset

1. Import the necessary libraries:
   ```python
   import seaborn as sns
   import pandas as pd
   ```

2. Load the taxi dataset using Seaborn's built-in dataset function:
   ```python
   taxi_data = sns.load_dataset("taxis")
   ```

3. Verify the dataset loaded correctly by examining the first few rows:
   ```python
   taxi_data.head()
   ```