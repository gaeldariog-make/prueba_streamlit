import streamlit as st
import pandas as pd
import time
i=1
while i==1:
  'iniciando...'
  
  # Add a placeholder
  latest_iteration = st.empty()
  bar = st.progress(0)
  
  for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteracion {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
  
  "listo"
  i+=1

st.write("mis datos:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]

}))
opcion = st.sidebar.selectbox(
    'quieres ingresar un request?',
    ('si', 'no')
)
if opcion=='si':
  add_selectbox = st.sidebar.selectbox(
      'selecciona opcion',
      ('1', '2', '3','4')
  )
  "escogiste", add_selectbox
  pd.loc('add_selectbox')
# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'valores',
    0.0, 100.0, (25.0, 75.0)








