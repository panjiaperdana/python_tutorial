import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


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

st.divider()

st.title('Streamlit Form')

with st.form(key='my_form'):
    st.subheader('Text Input')
    name = st.text_input('Enter your name')
    feedback = st.text_area('Provide your feedback')
    number = st.number_input('Enter your age', value=20)

    st.subheader('Selectors')
    choise = st.radio('Choose an option', ['Option 1', 'Option 2', 'Option 3'])
    gender = st.selectbox('Select your gender', ['Male', 'Female'])
    slider_value = st.select_slider('Select range', options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    st.subheader('Toggle & Chceckboxes')
    notification = st.checkbox('Receive notification?')
    toggle_value = st.checkbox("Enable dark mode?", value=False)

    submit_button = st.form_submit_button(label='Submit')

st.title('Strealit Input Form')

input_values = {
    'name': None,
    'height': None,
    'gender': None,
    'dob': None
}
min_date = datetime(1900, 1, 1)
max_date = datetime.now()

with st.form(key='user_info'):
    input_values['name'] = st.text_input('Enter your name:')
    input_values['height'] = st.number_input('Enter your height:')
    input_values['gender'] = st.selectbox('Select your gender:', ['Male', 'Female', 'Other'])
    input_values['dob'] = st.date_input('Enter your date of birth:', max_value=max_date, min_value=min_date)

    submit_button = st.form_submit_button()
    if submit_button:
        if not all(input_values.values()):
            st.warning('Please enter all fields')
        else:
            st.balloons()
            st.write('### Information')
            for i, (key, value) in enumerate(input_values.items()):
                formatted_key = key.upper() if i == 3 else key.capitalize()
                st.write(f'{formatted_key}: {value}')

st.divider()

st.title('Streamlit Session')

if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button('Increament Counter'):
    st.session_state.counter += 1
    st.write(f'Counter increment to {st.session_state.counter}')

if st.button("Reset"):
    st.session_state.counter = 0

st.write(f'Counter value: {st.session_state.counter}')

st.divider()

if "step" not in st.session_state:
    st.session_state.step = 1

if 'info' not in st.session_state:
    st.session_state.info = {}

def go_to_step2():
    st.session_state.info['name'] = st.session_state.name_input
    st.session_state.step = 2

def got_to_step1():
    st.session_state.step = 1

if st.session_state.step == 1:
    st.header('Part 1: Info')

    st.text_input('Name', key='name_input', value=st.session_state.info.get('name', ''))
    st.button("Next", on_click=go_to_step2)

if st.session_state.step == 2:
    st.header('Part 2: Review')
    st.subheader('Please review this:')

    st.write(f'**Name**: {st.session_state.info.get("name", "")}')
    if st.button("Submit"):
        st.success("Great!")
        st.balloons()
        st.session_state.info = {}

    st.button("Back", on_click=got_to_step1)

st.divider()

st.sidebar.title('This is the title')
st.sidebar.write('Write anything on this sidebar')
sidebar_input = st.sidebar.text_input('We also can use inputs')

tab1, tab2, tab3 = st.tabs(['Tab 1', 'Tab 2', 'Tab 3'])

with tab1:
    st.write('Tab 1: You are in here!')
with tab2:
    st.write('Tab 2: You are in here!')
with tab3:
    st.write('Tab 3: You are in here!')

col1, col2 = st.columns(2)
with col1:
    st.header('Column 1')
    st.write('Content for column 1')
with col2:
    st.header('Column 2')
    st.write('Content for column 2')

with st.container(border=True):
    st.write('This is inside a container.')
    st.write('You can think of containers as a grouping for elements.')
    st.write('Containers help manage sections of the page.')

placeholder = st.empty()
placeholder.write('This is an empty placeholder, useful for dynamic content.')

if st.button('Update Placeholder'):
    placeholder.write('The content of this placeholder has been update.')

with st.expander('Expand for more details'):
    st.write('This is additional information that is hidden by default.')
    st.write('You can use expaders to keep your interface cleaner.')

st.write('Hover over this button fot a tooltip.')
st.button ('Button with tooltip', help='This is a tooltip or popover on hover.')

if sidebar_input:
    st.write(f'You entered in the sidebar: {sidebar_input}')

st.divider()

