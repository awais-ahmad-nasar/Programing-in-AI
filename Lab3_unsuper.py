
import pandas as pd

import numpy as np

df1=pd.read_csv("C:\\Users\\AWAIS AHMAD\\OneDrive\Desktop\\DrHassan.csv")
df2=pd.read_csv("C:\\Users\\AWAIS AHMAD\OneDrive\\Desktop\\DrMunir.csv")

#...........................Task1(Read the data)..............................
# print(df1,"\n")
# print(df2,"\n")


#Task2( How many stud have more than 3.5 CGPA? display name+cgpa )
filterd_df=df1[df1['cgpa']>3.5]
#print(filterd_df[['name','cgpa']],"\n")

#Task3( How many stud enrolled in PAI? display on reg_no )
course=df1[df1['course']=='ML']
display=course['std_reg']
#print(display,"\n")




#Task4(display Records of stud who are studing same subject from both teacher)

column_name = 'course'
# Initialize an empty list to store matching rows
matching_rows = []
# Iterate through the rows in the first DataFrame
for index, row1 in df1.iterrows():
    # Get the value from the specified column in the first DataFrame
    value_to_compare = row1[column_name]
    # Check if the value is present in the second DataFrame's column
    if value_to_compare in df2[column_name].values:
        # If a match is found, append the row to the matching_rows list
        matching_rows.append(row1)

# Print or manipulate the matching rows as needed
# for row in matching_rows:
#    print(row)
#OR bolow direct print
#print(matching_rows)



#Task5(sort stud data in decending order on basis of CGPA)
dec=df1.sort_values(by='cgpa',ascending=False)
dec.to_csv("sort data",index=False)
print("DESCENDING:")
#print(dec)





