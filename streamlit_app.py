import streamlit as st
import pandas as pd
import openpyxl 

st.title('TechQuest')
em = st.text_input('E-mail')
roll = st.text_input('Roll.no')
inp = st.radio('how are you?',['Yes','No'])
sub = st.button('Submit')

def mail(em):
    y = 'drngpit.ac.in'
    x = em[8:]
    if x != y:
        st.error('Enter with your college ID', icon="⚠️")
    
def rol(roll):
    if len(roll) > 7:
        st.warning('Roll number should be 7 characters')

mail(em)
rol(roll)

if sub:
    ex = 'data.xlsx'
    df = pd.read_excel(ex)
    new_data = {"E-mail": em, "Roll.no": roll, "How are you?":inp }
    df = df.append(new_data, ignore_index=True)
    df.to_excel(ex, index=False)
    st.success('Your answer has been submited successfully!')
