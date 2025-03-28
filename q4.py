import pandas as pd
import numpy as np

### 1.1차원 데이터를 선언하여 Series형 데이터를 생성하세요.
# 5개의 age 데이터와 이름을 age로 선언해보세요.
age = pd.Series([10, 20, 30, 40, 50], name= 'age')
print(age,'\n')

### 2. Python Dictionary형 데이터 class_name을 Series형 데이터로 생성하세요.
class_name = {'국어' : 90,'영어' : 70,'수학' : 100,'과학' : 80}
class_series = pd.Series(class_name)
print(class_series,'\n')


### 3. 2차원 데이터를 선언하여 DataFrame형 데이터를 생성하세요.
#a = pd.Series([[3,7,1,5],[9,0,4,2],[6,8,5,3]])
arr = np.random.randint(low = 0,high = 10,size = (3, 5))
df = pd.DataFrame(arr,columns=['r1','r2','r3','r4','r5'],index=[1,2,3])
print(df,'\n')
