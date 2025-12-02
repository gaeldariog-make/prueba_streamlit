import streamlit as st
import pandas as pd
import time

while True:
  if i==1:
    break
  'iniciando...'
  
  # Add a placeholder
  latest_iteration = st.empty()
  bar = st.progress(0)
  
  for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'{i+1}%')
    bar.progress(i + 1)
    time.sleep(0.01)
  
  "listo"
  
df=pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]

})
st.write("mis datos:")
st.write(df)
opcion = st.sidebar.selectbox(
    'quieres ingresar un request?',
    ('si', 'no')
)
if opcion=='si':
  add_selectbox = st.sidebar.selectbox(
      'selecciona opcion',
      ('1', '2')
  )
  "escogiste", add_selectbox
  if add_selectbox=='1':
    df['first column']
  if add_selectbox=='2':
    df['second column']
i=1
# Add a slider to the sidebar:
#add_slider = st.sidebar.slider(
#    'valores',
#    0.0, 100.0, (25.0, 75.0))












