import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('W3 WCS: Stream lit build and shaare data apps exercise')
st.write("In this exercise I should: correlation and distribution analysis through different graphs and comments + buttons must be present to filter the results by region (US / Europe / Japan")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car = pd.read_csv(link)
st.write(df_car)

option=st.selectbox('Choose region:', df_car['continent'].unique())
st.write('You selected:', option)

st.write("Correlation beetween cylinders and cubinches:")
condition=df_car['continent'] == option
df_option=df_car.loc[condition, :]

grafico1 = sns.scatterplot(data=df_option,x="cylinders",y="cubicinches",color='blue').set_title('Scatterplot of cubicinches vs nr cylinders')
st.pyplot(grafico1.figure)

st.write("We can conclude, that cars with more cylinders normally have also more cubinches.")

st.write("Correlation beetween date of the cars and mpg:")
grafico2 = sns.boxplot(data=df_option, x="year",y="mpg", color='blue')
grafico2.set_title('Boxplot of miles per galon vs year of the car')
grafico2.set(ylim=(10, 50))
st.pyplot(grafico2.figure)

st.write("Observing the graph, that the cars have increase their miles per galon (mpg) over time, beetween 1971 and 1983. Which makes sense, since is a result of the technology development.")