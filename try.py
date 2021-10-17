import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

st.set_option('deprecation.showfileUploaderEncoding', False)

data = 'data/COVID-19 Indonesia.xlsx'
daily_cases=pd.read_excel(data,sheet_name='Kasus Aktif')
daily_cases.fillna(0,inplace=True)

daily_cases.set_index('Date',inplace=True)

st.write(daily_cases)
daily_cases.sum(axis=1).plot()
st.pyplot(plt)


progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(daily_cases.sum(axis=1))
# st.write(len(daily_cases.index))
for i in daily_cases['Date']:
    # progress_bar.progress(i+1)

    # new_rows = np.random.randn(10, 2)

    # chart.add_rows(new_rows)

    st.write(daily_cases.values.tolist())

    time.sleep(0.1)

# chart = st.line_chart(np.random.randn(10, 2))

# for i in range(100):
#     # Update progress bar.
#     progress_bar.progress(i + 1)

#     new_rows = np.random.randn(10, 2)

#     # Update status text.
#     status_text.text(
#         'The latest random number is: %s' % new_rows[-1, 1])

#     # Append data to the chart.
#     chart.add_rows(new_rows)

#     # Pretend we're doing some computation that takes time.
#     time.sleep(0.1)

# status_text.text('Done!')
# st.balloons()