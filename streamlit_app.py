import os
import pandas as pd
import streamlit as st
from io import BytesIO

datoteka = "data/sati_volontiranja.csv"

if not os.path.exists(datoteka):
    df = pd.DataFrame(columns=["Ime","Prezime","Datum","Sati volontiranja"])
    df.to_csv(datoteka, index=False)

df= pd.read_csv(datoteka)

df['Sati volontiranja'] = df["Sati volontiranja"].round(1)

st.title("Evidencija sati volontiranja")

tab1, tab2 = st.tabs(["Zapisnik sati", "Sortirani podaci"])

with tab1:
    with st.form("Zapisnik sati",clear_on_submit=True):
        ime = st.text_input("Ime")
        prezime = st.text_input("Prezime")
        datum = st.date_input("Datum", format="DD.MM.YYYY")
        vrijeme_vol = st.number_input("Vrijeme volontiranja", min_value=0.0, step=0.5, format="%.1f")

        podneseno = st.form_submit_button("Podnesi")
        if podneseno:
            zaokruzeno_vrijeme = round(vrijeme_vol,1)

            novi_unos = pd.DataFrame([{
                "Ime": ime,
                "Prezime" : prezime,
                "Datum" : datum,
                "Sati volontiranja" : zaokruzeno_vrijeme
            }])
            df=pd.concat([df, novi_unos],ignore_index=True)

            df.to_csv(datoteka,index=False)
            st.success("Uspješno podnešeno")


with tab2:
    st.write("Soritrani podaci sati po datumu i imenu i prezimenu")
    df1 = pd.read_csv(datoteka, parse_dates=['Datum'])

    df1['Datum'] = df1['Datum'].dt.strftime('%d.%m.%Y')
    sortirano = df1.sort_values(by=["Datum","Ime"])
    st.dataframe(sortirano)


    output = BytesIO()
    sortirano.to_excel(output, index=False, engine='xlsxwriter')
    excel_data = output.getvalue()  # Retrieve the binary data from the buffer

    st.download_button(
        label="Download data as XLSX",
        data=excel_data,
        file_name="data.xlsx",
        mime="text/xlsx",
)

