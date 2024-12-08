import os
import pandas as pd
import streamlit as st
from io import BytesIO
import plotly.express as px


datoteka = "data/sati_volontiranja.csv"

st.logo("images/logo_png.png",size="large")

if not os.path.exists(datoteka):
    df = pd.DataFrame(columns=["Ime","Prezime","Datum","Sati volontiranja"])
    df.to_csv(datoteka, index=False)

df= pd.read_csv(datoteka)

df['Sati volontiranja'] = df["Sati volontiranja"].round(1)

st.title("Evidencija sati volontiranja")

tab1, tab2 ,tab3 = st.tabs(["Zapisnik sati", "Sortirani podaci","Statistika"])

with tab1:
    with st.form("Zapisnik sati",clear_on_submit=True):
        ime = st.text_input("Ime")
        prezime = st.text_input("Prezime")
        datum = st.date_input("Datum", format="DD.MM.YYYY")
        vrijeme_vol = st.number_input("Vrijeme volontiranja", min_value=0.0, step=0.5,value=2.0, format="%.1f")

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
        label="Preuzmi u excel datoteku",
        data=excel_data,
        file_name="data.xlsx",
        mime="text/xlsx"
    )

with tab3:
    ukupni_sati_po_osobi = df.groupby(['Ime', 'Prezime'])['Sati volontiranja'].sum().reset_index()

    df['Mjesec'] = pd.to_datetime(df['Datum']).dt.to_period('M')
    ukupni_sati_po_mjesecu_po_osobi = df.groupby(['Ime', 'Prezime', 'Mjesec'])['Sati volontiranja'].sum().reset_index()

    st.subheader("Ukupni sati po osobi")
    st.dataframe(ukupni_sati_po_osobi)
    output1 = BytesIO()
    ukupni_sati_po_osobi.to_excel(output1, index=False, engine='xlsxwriter')
    excel_po_osobi = output1.getvalue()
    st.download_button(
        label="Preuzmi u excel datoteku",
        data=excel_po_osobi,
        file_name="sati_po_osobi.xlsx",
        mime="text/xlsx"
    )

    st.subheader("Ukupni sati mjesečno po osobi")
    st.dataframe(ukupni_sati_po_mjesecu_po_osobi)
    output2 = BytesIO()
    ukupni_sati_po_mjesecu_po_osobi.to_excel(output2, index=False, engine='xlsxwriter')
    excel_po_mjesecu_po_osobi = output2.getvalue()
    st.download_button(
        label="Preuzmi u excel datoteku",
        data=excel_po_mjesecu_po_osobi,
        file_name="sati_po_mjesecu_po_osobi.xlsx",
        mime="text/xlsx"
    )

    st.subheader("Dijagrami")
    
    # Graf: Ukupni sati po osobi
    fig1 = px.bar(
        ukupni_sati_po_osobi,
        x="Ime",
        y="Sati volontiranja",
        color="Prezime",
        title="Ukupni sati volontiranja po osobi",
        labels={"Sati volontiranja": "Sati"}
    )
    st.plotly_chart(fig1)

    # Graf: Trend sati po mjesecu po osobi
    ukupni_sati_po_mjesecu_po_osobi['Mjesec'] = ukupni_sati_po_mjesecu_po_osobi['Mjesec'].astype(str)
    fig2 = px.line(
        ukupni_sati_po_mjesecu_po_osobi,
        x="Mjesec",
        y="Sati volontiranja",
        color="Ime",
        line_group="Prezime",
        title="Trend sati volontiranja po mjesecu",
        labels={"Sati volontiranja": "Sati"}
    )
    st.plotly_chart(fig2)