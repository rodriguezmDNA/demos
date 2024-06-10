import streamlit as st

from birthdate_sim import *

import pandas as pd

import altair as alt

import seaborn as sns 
import matplotlib.pyplot as plt


#### Styling functions
stHTML = lambda string: st.markdown(string, unsafe_allow_html=True)
stHTMLsidebar = lambda string: st.sidebar.markdown(string, unsafe_allow_html=True)
textCenter = lambda text: f"<p style='text-align:center;'> {text} </p>"
center_string = lambda x: f"<p style='text-align:center;'> {x} </p>"


##########################################

########################################## SIDEBAR ##########################################
st.sidebar.title('Parameters')
st.sidebar.markdown('---')

people = st.sidebar.slider('Size of group',1,100,23)
samples = st.sidebar.slider('Number of random samples',10,1000,100,10)



###########################################  MAIN  ###########################################
html_string = "<h2 style='text-align:center;'> Birthday paradox </h2>"
stHTML(html_string)
st.markdown('---')


html_string = f"""<h4 style='text-align:center;'> What is the probability that in a group of <code>{people}</code> 
                people, at least two share the same birthdate?
                </h4>
                """
stHTML(html_string)
st.markdown('---')


sample_birth_dates = (simulate_birthdate_draws(samples,people))
counts_dates = tally_shared_birthdates(samples,sample_birth_dates)

frequencies_at_least_n_shared = {n_shared: np.mean(np.any(counts_dates >= n_shared,1)) for n_shared in range(2,11)}

frequencies_at_least_n_shared_df = pd.DataFrame.from_dict(frequencies_at_least_n_shared,orient='index').reset_index()
frequencies_at_least_n_shared_df.columns = ['n','prob']

########################################################################

st.write(f'''
         To calculate the probabilities, I take {people} random samples from a pool of 365 numbers (each representing a date of birth). This simulates any random group of people. I repeat this {samples} times and tally how many times I see at least two dates repeated.

         With the results of the simulation, I further calculate the probabilities of larger subsets sharing a birthdate.

         Some simplifications are made: each date has an equal probability of being selected, and no leap days or the existence of twins in the group are considered.
         ''')


st.markdown('---')


st.subheader('Altair interactive visualization')


chart = alt.Chart(frequencies_at_least_n_shared_df).mark_line(point=alt.OverlayMarkDef(color="black")).encode(
    x=alt.X('n:Q', title='At least n people', axis=alt.Axis(tickMinStep=1)),
    y=alt.Y('prob', title='Probability')
).properties(
    title=f'Probabilities that at least n people shared a birthdate in a group of size {people}',
    width=800,
    height=300
).configure_point(
    color='black'
).configure_line(
    strokeDash=[4, 4]
)

st.altair_chart(chart, use_container_width=True)


# Plotting with Seaborn
st.subheader('Seaborn static visualization')
fig, ax = plt.subplots(figsize=(12, 3))
ax.set_title(f'Probabilities that at least n people shared a birthdate in a group of size {people}',)
sns.scatterplot(data=frequencies_at_least_n_shared_df,x='n',y='prob', color='black', ax=ax)
sns.lineplot(data=frequencies_at_least_n_shared_df,x='n',y='prob', color='black', ls=':', ax=ax)
ax.set_ylabel('Probability')
ax.set_xlabel('At least n people')
st.pyplot(fig)




#############################################
stHTML('<br>')
stHTML('<br>')
st.markdown('---')


html_string = f"<h5 style='text-align:center;'> Joel Rodriguez Medina </h5>"
stHTML(html_string)