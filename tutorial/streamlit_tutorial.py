import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.write("Hello World!")
st.write({"key": "value", "asdf": "asdf"})

pressed = st.button("Press Me!")
print(pressed)

st.title("Simple Title")
st.header("Simple Header")
st.subheader("Simple Subheader")
st.markdown("This is a **Markdown** _letter_")
st.divider()
st.caption("This is a **Markdown** _letter_")
st.code("""
    print('hello', name)
    """)
st.image(os.path.join(os.getcwd(), 'tutorial\static', 'bg.jpg'))

st.divider()

st.title("Streamlit Elements")

df = pd.DataFrame({
    'name': ["Lucy", "Edward", "Johnson"],
    'age': [4, 5, 6],
    'position': ["Engineer", "Driver", "CEO"]
})

st.subheader("Dataframe")
st.dataframe(df)

st.subheader("Data Editor")
editable_df = st.data_editor(df)
print(editable_df)

st.subheader("Static Table")
st.table(df)

st.subheader("Metric")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Age", value=round(df['age'].mean(), 1))

st.subheader("JSON & Dictionary")
sample_data = {
    'name': 'Alice',
    'age': 24,
    'skills': ['Data Analyst','Data Engineer', 'Business Analyst', 'Web Developer']
}
st.json(sample_data)
st.write("Dictionary", sample_data)

st.divider()

st.title("Streamlit Charts")

chart_data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['a', 'b', 'c']
)

st.subheader("Area Chart")
st.area_chart(chart_data)

st.subheader("Bar Chart")
st.bar_chart(chart_data)

st.subheader("Line Chart")
st.line_chart(chart_data)

st.subheader("Scatter Chart")
scatter_data = pd.DataFrame({
    'x': np.random.randn(50),
    'y': np.random.randn(50)
})
st.scatter_chart(scatter_data)

st.subheader("Map")
map_data = pd.DataFrame(
    np.random.randn(10, 2) / [20, 20] + [-6.2, 106.8],
    columns=['lat', 'lon']
)
st.map(map_data)

st.subheader("Pyplot Chart")
fig, ax = plt.subplots()
ax.plot(chart_data['a'], label='A')
ax.plot(chart_data['b'], label='B')
ax.plot(chart_data['c'], label='C')
ax.set_title('Pyplot Line Chart')
ax.legend()
st.pyplot(fig)