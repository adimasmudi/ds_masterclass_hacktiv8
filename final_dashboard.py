from numpy import ubyte
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_option('deprecation.showfileUploaderEncoding', False)


st.title("Visualisasi Data Covid-19 di Indonesia")

st.sidebar.subheader("Pengaturan Visualisasi")

uploaded_file = st.sidebar.file_uploader(label="Upload file CSV anda", type=['xlsx'])







show_data_daily = st.sidebar.checkbox("Tampilkan Data kasus harian aktif per provinsi")
show_data_total = st.sidebar.checkbox("Tampilkan Total Kasus per Provinsi")
show_daily_stats = st.sidebar.checkbox("Tampilkan statistik harian")

if uploaded_file is not None:
    daily_cases=pd.read_excel(uploaded_file,sheet_name='Kasus Aktif')
    daily_cases.fillna(0,inplace=True)
    daily_cases.set_index('Date',inplace=True)
    
    total_cases=pd.read_excel(uploaded_file,sheet_name='Total Kasus')
    total_cases.fillna(0,inplace=True)
    total_cases.set_index('Date',inplace=True)


    daily_stats = pd.read_excel(uploaded_file,sheet_name='Statistik Harian')
    daily_stats = daily_stats[:len(daily_stats)-29]
    daily_stats.fillna(0,inplace=True)
    daily_stats.set_index('Date',inplace=True)

try:
    if show_data_daily:
        st.write(daily_cases)

        active_case_select = st.sidebar.selectbox(
            label='pilih yang ingin divisualisasikan',
            options=['silahkan pilih :)','kasus aktif harian','provinsi dengan kasus aktif harian terbanyak']
        )

        if active_case_select == 'kasus aktif harian':
            daily_cases.sum(axis=1).plot()
            plt.title('Jumlah kasus aktif covid per hari di indonesia')
            st.pyplot(plt)
        elif active_case_select == 'provinsi dengan kasus aktif harian terbanyak':
            amount = st.sidebar.slider('Pilih jumlah provinsi', 5,34,1)
            daily_cases.sum(axis=0).sort_values(ascending=False).head(amount).plot(kind="bar")
            st.pyplot(plt)
    
    if show_data_total:
        st.write(total_cases)
        total_case_select = st.sidebar.selectbox(
            label='pilih yang ingin divisualisasikan',
            options=['silahkan pilih :)','total kasus','provinsi dengan total kasus harian terbanyak']
        )

        if total_case_select == 'total kasus':
            total_cases.sum(axis=1).plot()
            plt.title('Jumlah Total kasus covid per hari di indonesia')
            st.pyplot(plt)
        elif total_case_select == 'provinsi dengan total kasus harian terbanyak':
            amount = st.sidebar.slider('Pilih jumlah provinsi', 5,34,1)
            total_cases.sum(axis=0).sort_values(ascending=False).head(amount).plot(kind="bar")
            st.pyplot(plt)
    
    if show_daily_stats:
        st.write(daily_stats)

        comparison_daily_stats = daily_stats[['Total kasus','Kasus aktif','Sembuh','Meninggal']]
        pemeriksaan = daily_stats[['Jumlah orang diperiksa','Negatif']]


        daily_stats_select = st.sidebar.selectbox(
            label='pilih yang ingin divisualisasikan',
            options=['silahkan pilih :)','vaksin dosis 1','vaksin dosis 2','perbandingan data harian','pemeriksaan']
        )
        if daily_stats_select == 'vaksin dosis 1':
            daily_stats[['Dosis pertama']].sum(axis=1).plot()
            
        elif daily_stats_select == 'vaksin dosis 2':
            daily_stats[['Dosis kedua']].sum(axis=1).plot()
            
        elif daily_stats_select == 'perbandingan data harian':
            comparison_daily_stats.plot(y=["Total kasus", "Kasus aktif","Sembuh", "Meninggal"])
        elif daily_stats_select == 'pemeriksaan':
            pemeriksaan.plot(y=['Jumlah orang diperiksa','Negatif'])
        st.pyplot(plt)
        
except Exception as e:
    st.write('masukkan data',e)