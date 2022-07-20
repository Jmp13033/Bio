import streamlit as st
import altair as alt
import pandas as pd 
from PIL import Image

image = Image.open('dna.png')
st.image(image, use_column_width=True)

st.write("""

# Dna Nucleotide Count Web APP

This App counts the nucleotides Composition of query DNA 


*** 
""")



st.header("Enter your DNA Sequence ")
sequence_input = ">DNA Query \nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence Input ", sequence_input, height=150)
sequence = sequence.splitlines()
sequence = sequence[1:]

sequence = "".join(sequence)
st.header("Input(DNA Query)")
sequence


st.header("Output (DNA Nucleotide Count) ")


st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
x_values = list(X.values())

X




st.subheader('2. Print text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')



st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)





