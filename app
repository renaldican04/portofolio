import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard Penjualan Barang")

uploaded_file = st.file_uploader("Upload dataset penjualan (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Data Penjualan")
    st.dataframe(df)

    # Grafik 1: Total Penjualan per Produk
    st.subheader("🏷️ Total Penjualan per Produk")
    fig_total_produk = px.bar(df, x="Nama Produk", y="Total Penjualan", text="Total Penjualan")
    st.plotly_chart(fig_total_produk, use_container_width=True)

    # Grafik 2: Jumlah Qty per Produk
    st.subheader("📦 Jumlah Qty per Produk")
    fig_qty = px.bar(df, x="Nama Produk", y="Qty", text="Qty")
    st.plotly_chart(fig_qty, use_container_width=True)

    # Grafik 3: Penjualan Bersih per Pelanggan
    st.subheader("👥 Penjualan Bersih per Pelanggan")
    fig_pelanggan = px.bar(df, x="Nama Pelanggan", y="Penjualan Bersih", text="Penjualan Bersih")
    st.plotly_chart(fig_pelanggan, use_container_width=True)

    # Grafik 4: Total Penjualan berdasarkan Tanggal
    st.subheader("📅 Total Penjualan per Tanggal")
    fig_tgl = px.line(df, x="Tanggal", y="Total Penjualan")
    st.plotly_chart(fig_tgl, use_container_width=True)

else:
    st.info("Silakan upload dataset CSV untuk memulai dashboard.")
