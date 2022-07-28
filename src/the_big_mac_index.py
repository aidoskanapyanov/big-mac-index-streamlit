import pandas as pd
import streamlit as st

from visualization import create_figure

DATE_COLUMN = 'date'
DATA_PATH = './src/data/cleaned/big-mac-source-data-plus-kaz.csv'


st.set_page_config(
    page_title="The Big Mac Index",
    page_icon="🍔",
)
st.title('🍔 The Big Mac Index')
st.subheader('Visualization')
st.write(
    "The following chart shows the calculated index values as of 1st of July, 2022."
)
st.write(
    "Negative index indicates that the given currency is undervalued against the selected base currency by said percentage. "
    "For example, a Kazakhstani tenge is undervalued against the US dollar by 57.5%, according to the Big Mac index."
)


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_PATH, nrows=nrows)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# Load data
data = load_data(10000)

# Choose base currency
base_currency = {
    'US dollar (USD)': 'USD',
    'Euro (EUR)': 'EUR',
    'British pound (GBP)': 'GBP',
    'Japanese yen (JPY)': 'JPY',
    'Chinese yuan (CNY)': 'CNY',
    'Kazakhstani tenge (KZT)': 'KZT',
}
chosen_base_currency = st.selectbox(
    'Choose base currency:', tuple(base_currency.keys())
)
chosen_base_currency = base_currency.get(chosen_base_currency)

# Plot the Big Mac Index
data = data.sort_values(by=[chosen_base_currency], ascending=True).reset_index(
    drop=True
)
figure = create_figure(data, chosen_base_currency)
st.plotly_chart(figure, use_container_width=True)

# Data view
st.subheader('Data')
st.write('To see the data that is being used, check the following box.')

# Toggle to view raw data
if st.checkbox('Show raw data'):
    st.write(data)
