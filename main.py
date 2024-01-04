import streamlit as st
import datetime

st.header('Calculator')
#st.text('This is calculator ')


a = st.number_input('a')
#t.write('The current number is ', a)

b = st.number_input('b')
#st.write('The current number is ', b)


option = st.selectbox(
    'What  would you like to  calculate?',
    ('Division', 'Multiplication', 'Addition', 'Subtraction'))

def calculator(a, b, option):
    if option == 'Division':
        return a / b
    elif option == 'Multiplication':
        return a * b
    elif option == 'Addition':
        return a + b
    elif option == 'Subtraction':
        return a - b
    else:
        return 'Invalid option'

# Example usage:
result = calculator(a, b, option)
st.write(option,result)


#st.write('option :  ', a/b)







#d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
#st.write('Your birthday is:', d)