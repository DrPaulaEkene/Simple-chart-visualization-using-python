# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 09:49:47 2023, by Ekene Pauline Anugha-Ugochukwu
7PAM2000 Applied Data Science 1
Assignment 1: Visualisation
"""

#import numpy
import numpy as np

#import panadas
import pandas as pd

# import the standard graphics library
import matplotlib.pyplot as plt


# Define a function to sort a DataFrame in descending order
def sort_dataframe_descending(df, columns):
    columns = [columns]

    # Sort the DataFrame in descending order based on the specified columns
    df_sorted = df.sort_values(by=columns, ascending=False)

    return df_sorted

# Define  a function to delete rows


def delete_rows(dataframe, condition):
    """
    Deletes rows from a dataframe based on a specified condition.

    Parameters:
    - dataframe: The pandas DataFrame from which rows are to be deleted.
    - condition: A boolean Series or expression that specifies the rows to delete.

    Returns:
    - A new DataFrame with the specified rows removed.
    """
    new_dataframe = dataframe[~condition]
    return new_dataframe_dataframe


# Read source csv file, Campylo.csv
df_campylo_file = pd.read_csv("Campylo.csv")
df_campylo_raw = df_campylo_file

# Choose the date of interest, the thirteenth of August, 2015
condition = df_campylo_raw["DateExamined"] == "2015-07-13"
df_campylo_raw = df_campylo_raw[condition]

# Print the new DataFrame for the selected date
print(df_campylo_raw)

# Extract and clean target columns for plotting
df_campylo_raw = df_campylo_raw[["DateExamined", "Country",
                                 "RemainingShelflifeDays",
                                 "TemperatureAtCollection", "TypeOfChicken",
                                 "Result"]]

# drop rows with missing values
df_campylo_d = df_campylo_raw.dropna()
print(df_campylo_d)

# Remove '<' to convert the result columnn to integers,fix non-numeric or missing values
df_campylo_d.loc[:, "Result"] = pd.to_numeric(
    df_campylo_d["Result"].str.replace("<", ""), errors='coerce').astype('Int64')

# Changethe results of Campylo Cultures isloated to copies in hundreds
df_campylo_d["Resultsinhundreds"] = df_campylo_d["Result"]/100


# Using defined functions, create data frames based on location
# Seperate England from other countries
condition = df_campylo_d["Country"] == "England"

# Filter and print rows based on the condition-England
df_campylo_Eng = df_campylo_d[condition]
print(df_campylo_Eng)

# Create a new column that assigns IDs to Samples, "Sample- C1, C2, C3......."
df_campylo_Eng["SampleID"] = "C" + (df_campylo_Eng.index + 1).astype(str)
print(df_campylo_Eng)

# Select and print the first 20 Samples for plotting
df_campylo_Eng_First20 = df_campylo_Eng.iloc[0:20]
print(df_campylo_Eng_First20)


# Plot the temperature,shelf life days and results against Samples tested
# Specify the size of the figure
plt.figure(figsize=(12, 6))
x = df_campylo_Eng_First20["SampleID"]
y = df_campylo_Eng_First20["RemainingShelflifeDays"]
z = df_campylo_Eng_First20["TemperatureAtCollection"]
u = df_campylo_Eng_First20["Resultsinhundreds"]


# Produce the legend using the labels, specify the label sizes
plt.plot(x, y, label="Shelf life days left", color="magenta")
plt.plot(x, z, label="Sample Collection Temperature", color="blue")
plt.plot(x, u, label="Campylobacter count in hundreds", color="green")


# Add axis labels
plt.xlabel("Chicken sample ID")
plt.ylabel("sample conditions vs microbial titre")


# Specify legend position, font size, save figure
plt.legend(loc="upper right", fontsize=10)
plt.savefig("Campylocabterinchicken.png")
plt.show()

# Create a column, ChickenType_T(CType_T) and sort in descending order
CType_T = df_campylo_file["TypeOfChicken"].value_counts().reset_index()
sort_dataframe_descending(CType_T, "TypeOfChicken")

# Rename the columns for clarity
CType_T.columns = ['Value', 'Count']
print(CType_T)

# Plot a pie chart, representing the percentage of each type
explode = (0.1, 0, 0.5, 0.1)
CType_T.plot(kind='pie', y='Count',
             labels=CType_T['Value'], autopct='%1.1f%%', legend=False, explode=explode)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Create a column,Chickensource that contains the tally for each source
Chicksource = df_campylo_file["Retailer"].value_counts().reset_index()

# Rename the columns for clarity
Chicksource.columns = ['Value', 'Count']
print(Chicksource)

# Plotting a  green bar chart for the Chicken Sources, label the axes
Chicksource.plot(x="Value", y='Count', kind='bar', color="green")
plt.xlabel("Stores")
plt.ylabel("No of Chicken samples provided")
plt.show()

df_campylo_file['Retailer'] = df_campylo_file['Retailer'].str.lower()

# Perform the value counts and reset the index

Chicksource = df_campylo_file["Retailer"].value_counts().reset_index()


# Rename the columns for clarity
Chicksource.columns = ['Value', 'Count']
print(Chicksource)


# Plotting a green bar chart for the Chicken Sources, label the axes
plt.figure(figsize=(12, 6))
Chicksource.plot(x="Value", y='Count', kind='bar', color="green")
plt.xlabel("Stores")
plt.ylabel("No of Chicken samples provided")
plt.savefig("Chickensources.png", dpi=300)
plt.show()
