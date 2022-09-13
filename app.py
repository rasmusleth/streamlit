import streamlit as st

st.title('Jeg er en titel')
sentences1 = st.text_input('Insert sentences 1:')
sentences2 = st.text_input('Insert sentences 2:')

if st.button('Submit'):
    st.write('Sentences1 is: ', sentences1)
    st.write('Sentences2 is: ', sentences2)