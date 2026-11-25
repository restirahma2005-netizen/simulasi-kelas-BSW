#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyleft © 2026 Anung <anung@trisakti.ac.id>
# 2026-11-19 13:33
# Distributed under terms of the MIT license.

"""

"""
import streamlit as st
import pandas as pd
import plotly.express as px

# Mengambil data
df = pd.read_csv("data_tpt_ipm_2020_2024.csv")

st.set_page_config(
    page_title="Page 1",
    layout="wide",
)

st.title("Annyeonghaseyo, kelompok 2 imnida, kita akan memperlihatkan data Perkembangan TPT dan IPM Indonesia")
st.caption("Chaubella")

# Mengaambil data nasional
nasional = df[df["Provinsi"].str.upper() == "INDONESIA"].copy()
nasional = nasional.sort_values("Tahun")

if not nasional.empty:
    terbaru = nasional[nasional["Tahun"] == 2024].iloc[0]

    st.subheader("Indikator Nasional Tahun 2024")

    col1, col2 = st.columns(2)

    col1.metric(
        "Tingkat Pengangguran Terbuka",
        f'{terbaru["TPT"]:2F}%'
)
            
    col2.metric("indeks pembangunan manusia",
              f'{terbaru["IPM"]:.2F}'
)

st.divider()

st.subheader("Perkembangan Indikator Nasional")

pilihan = st.selectbox(
    "Pilih Indikator",
    ["TPT", "IPM"]
)

fig = px.line(
    nasional,
    x="Tahun",
    y=pilihan,
    markers=True,
    title=f"Perkembangan {pilihan} Indionesia 2020-2024"
)

st.plotly_chart(fig, use_container_width=True)


st.divider()

st.subheader("Tentang Dashboard")

st.write("""Dashboard ini dibuat untuk melihat perkembangan kondisi ketenagakerjaan dan pembangunan manusia di Indonesia. Pengguna dapat melihat data nasional, membandingkan antarprovinsi, serta mengamati perubahan kedua indikator dari tahun 2020 sampai 2024.""")

st.info(
    "Sumber data: Badan Pusat Statistik (BPS)."
    "Data TPT menggunakan periode Agustus."
)
st.markdown("---")

