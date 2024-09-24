import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import io


# Title aplikasi di Streamlit
st.title("📊 Exploratory Data Analysis (EDA) untuk Dataset Penjualan Regional AS")

# Load dataset (sesuaikan dengan lokasi file kamu)
file_path = 'datasheet.xlsx'
sales_df = pd.read_excel(file_path, sheet_name='Sales Orders Sheet')

# 1. Data Preparation: Mengganti nama kolom agar lebih mudah diakses
sales_df.columns = sales_df.columns.str.replace(' ', '_')

# Penjelasan pengenalan data
st.write("""
Dataset ini berisi informasi tentang *sales orders* di berbagai region di Amerika Serikat. 
Kita akan mengeksplorasi data ini untuk mendapatkan insight-insight yang berguna terkait penjualan, diskon, dan performa produk.
""")

# 2. Menampilkan 5 baris pertama dataset dengan penjelasan
st.subheader("📋 Data Sample - Sales Order Sheet")
st.dataframe(sales_df.head())
st.write("Dataset ini memiliki **{} baris** dan **{} kolom**.".format(sales_df.shape[0], sales_df.shape[1]))

# 3. Memeriksa Tipe Data dan Missing Values
st.subheader("📊 Informasi Data")

# Use StringIO to capture DataFrame info output
buffer = io.StringIO()
sales_df.info(buf=buffer)
info_str = buffer.getvalue()
st.text(info_str)

st.subheader("🔍 Missing Values")
missing_values = sales_df.isnull().sum()
st.write(missing_values[missing_values > 0])

# Load dataset (sesuaikan dengan lokasi file kamu)
file_path = 'datasheet.xlsx'
sales_df1 = pd.read_excel(file_path, sheet_name='Customers Sheet')

# 1. Data Preparation: Mengganti nama kolom agar lebih mudah diakses
sales_df1.columns = sales_df1.columns.str.replace(' ', '_')


# 2. Menampilkan 5 baris pertama dataset dengan penjelasan
st.subheader("📋 Data Sample - Customers Sheet")
st.dataframe(sales_df1.head())
st.write("Dataset ini memiliki **{} baris** dan **{} kolom**.".format(sales_df1.shape[0], sales_df1.shape[1]))

# 3. Memeriksa Tipe Data dan Missing Values
st.subheader("📊 Informasi Data")

# Use StringIO to capture DataFrame info output
buffer = io.StringIO()
sales_df1.info(buf=buffer)
info_str = buffer.getvalue()
st.text(info_str)

st.subheader("🔍 Missing Values")
missing_values = sales_df1.isnull().sum()
st.write(missing_values[missing_values > 0])

# Load dataset (sesuaikan dengan lokasi file kamu)
file_path = 'datasheet.xlsx'
sales_df2 = pd.read_excel(file_path, sheet_name='Store Locations Sheet')

# 1. Data Preparation: Mengganti nama kolom agar lebih mudah diakses
sales_df2.columns = sales_df2.columns.str.replace(' ', '_')


# 2. Menampilkan 5 baris pertama dataset dengan penjelasan
st.subheader("📋 Data Sample - Store Location Sheet")
st.dataframe(sales_df2.head())
st.write("Dataset ini memiliki **{} baris** dan **{} kolom**.".format(sales_df2.shape[0], sales_df2.shape[1]))

# 3. Memeriksa Tipe Data dan Missing Values
st.subheader("📊 Informasi Data")

# Use StringIO to capture DataFrame info output
buffer = io.StringIO()
sales_df2.info(buf=buffer)
info_str = buffer.getvalue()
st.text(info_str)

st.subheader("🔍 Missing Values")
missing_values = sales_df2.isnull().sum()
st.write(missing_values[missing_values > 0])

# Load dataset (sesuaikan dengan lokasi file kamu)
file_path = 'datasheet.xlsx'
sales_df3 = pd.read_excel(file_path, sheet_name='Products Sheet')

# 1. Data Preparation: Mengganti nama kolom agar lebih mudah diakses
sales_df3.columns = sales_df3.columns.str.replace(' ', '_')


# 2. Menampilkan 5 baris pertama dataset dengan penjelasan
st.subheader("📋 Data Sample - Products Sheet")
st.dataframe(sales_df3.head())
st.write("Dataset ini memiliki **{} baris** dan **{} kolom**.".format(sales_df3.shape[0], sales_df3.shape[1]))

# 3. Memeriksa Tipe Data dan Missing Values
st.subheader("📊 Informasi Data")

# Use StringIO to capture DataFrame info output
buffer = io.StringIO()
sales_df3.info(buf=buffer)
info_str = buffer.getvalue()
st.text(info_str)

st.subheader("🔍 Missing Values")
missing_values = sales_df3.isnull().sum()
st.write(missing_values[missing_values > 0])


# Load dataset (sesuaikan dengan lokasi file kamu)
file_path = 'datasheet.xlsx'
sales_df4 = pd.read_excel(file_path, sheet_name='Regions Sheet')

# 1. Data Preparation: Mengganti nama kolom agar lebih mudah diakses
sales_df4.columns = sales_df4.columns.str.replace(' ', '_')


# 2. Menampilkan 5 baris pertama dataset dengan penjelasan
st.subheader("📋 Data Sample - Regions Sheet")
st.dataframe(sales_df4.head())
st.write("Dataset ini memiliki **{} baris** dan **{} kolom**.".format(sales_df4.shape[0], sales_df4.shape[1]))

# 3. Memeriksa Tipe Data dan Missing Values
st.subheader("📊 Informasi Data")

# Use StringIO to capture DataFrame info output
buffer = io.StringIO()
sales_df4.info(buf=buffer)
info_str = buffer.getvalue()
st.text(info_str)

st.subheader("🔍 Missing Values")
missing_values = sales_df4.isnull().sum()
st.write(missing_values[missing_values > 0])

# Load dataset (sesuaikan dengan lokasi file kamu)
file_path = 'datasheet.xlsx'
sales_df5 = pd.read_excel(file_path, sheet_name='Sales Team Sheet')

# 1. Data Preparation: Mengganti nama kolom agar lebih mudah diakses
sales_df5.columns = sales_df5.columns.str.replace(' ', '_')


# 2. Menampilkan 5 baris pertama dataset dengan penjelasan
st.subheader("📋 Data Sample - Regions Sheet")
st.dataframe(sales_df5.head())
st.write("Dataset ini memiliki **{} baris** dan **{} kolom**.".format(sales_df5.shape[0], sales_df5.shape[1]))

# 3. Memeriksa Tipe Data dan Missing Values
st.subheader("📊 Informasi Data")

# Use StringIO to capture DataFrame info output
buffer = io.StringIO()
sales_df5.info(buf=buffer)
info_str = buffer.getvalue()
st.text(info_str)

st.subheader("🔍 Missing Values")
missing_values = sales_df5.isnull().sum()
st.write(missing_values[missing_values > 0])





# # 3. Memeriksa Tipe Data dan Missing Values
# st.subheader("📊 Informasi Data")
# buffer = []
# sales_df.info(buf=buffer)
# info_str = "\n".join(buffer)
# st.text(info_str)

# st.subheader("🔍 Missing Values")
# missing_values = sales_df.isnull().sum()
# st.write(missing_values[missing_values > 0])

# # 3. Memeriksa Tipe Data dan Missing Values
# st.subheader("📊 Informasi Data")

# # Use StringIO to capture DataFrame info output
# buffer = io.StringIO()
# sales_df.info(buf=buffer)
# info_str = buffer.getvalue()
# st.text(info_str)

# st.subheader("🔍 Missing Values")
# missing_values = sales_df.isnull().sum()
# st.write(missing_values[missing_values > 0])

# # 4. Mengubah Format Tanggal ke datetime
# sales_df['OrderDate'] = pd.to_datetime(sales_df['OrderDate'])
# sales_df['ShipDate'] = pd.to_datetime(sales_df['ShipDate'])
# sales_df['Order_Duration'] = (sales_df['ShipDate'] - sales_df['OrderDate']).dt.days

# # # 5. Visualisasi Distribusi Pesanan Berdasarkan Region
# # st.subheader("📍 Distribusi Pesanan Berdasarkan Region")
# # fig, ax = plt.subplots(figsize=(10, 6))
# # sns.countplot(data=sales_df, x='_StoreID', palette='Set2', ax=ax)
# # plt.title('Distribusi Pesanan Berdasarkan Region', fontsize=14, fontweight='bold')
# # ax.set_xlabel("Region")
# # ax.set_ylabel("Jumlah Pesanan")
# # st.pyplot(fig)
# # st.write("""
# # 📌 **Penjelasan:** Grafik ini menunjukkan distribusi jumlah pesanan di setiap region. 
# # Region dengan pesanan terbanyak adalah yang paling berpotensi memberikan keuntungan besar.
# # """)

# # 4. Visualisasi Distribusi Pesanan Berdasarkan Region (dengan rotasi label)
# st.write("📍 *Distribusi Pesanan Berdasarkan Region:*")
# fig, ax = plt.subplots(figsize=(10, 6))
# region_counts = sales_df['_StoreID'].value_counts().sort_values(ascending=False)
# sns.barplot(y=region_counts.index, x=region_counts.values, palette='Set2', ax=ax)
# plt.title('Distribusi Pesanan Berdasarkan Region')
# plt.xlabel('region')
# plt.ylabel('jumlah pesanan')
# plt.tight_layout()
# # Menampilkan grafik di Streamlit
# st.pyplot(fig)
# # 5. Penjelasan
# st.write("📌 *Penjelasan:* Grafik ini menunjukkan distribusi jumlah pesanan di setiap region dengan cara yang lebih mudah dibaca. "
#          "Grafik horizontal membantu lebih jelas dalam membandingkan region satu sama lain, serta mengurangi penumpukan label.")

# # 6. Visualisasi Total Penjualan per Region dengan log scale untuk melihat distribusi yang lebih jelas
# st.subheader("💰 Total Penjualan Berdasarkan Region")
# sales_per_region = sales_df.groupby('_StoreID')['_SalesTeamID'].sum().sort_values(ascending=False)
# fig, ax = plt.subplots(figsize=(10, 6))
# sns.barplot(x=sales_per_region.index, y=sales_per_region.values, palette='Set1', ax=ax)
# ax.set_yscale('log')  # Using log scale to better visualize variations in total sales
# plt.title('Total Penjualan Berdasarkan Region (Log Scale)', fontsize=14, fontweight='bold')
# ax.set_xlabel("Region")
# ax.set_ylabel("Total Penjualan (log)")
# st.pyplot(fig)
# st.write("""
# 📌 **Penjelasan:** Penggunaan skala log pada sumbu y memungkinkan kita untuk melihat lebih jelas variasi penjualan di tiap region, 
# terutama ketika terdapat perbedaan penjualan yang sangat besar antara region.
# """)

# # 7. Analisis Saluran Penjualan dengan interaktivitas tambahan
# st.subheader("🛒 Distribusi Pesanan Berdasarkan Sales Channel")
# fig, ax = plt.subplots(figsize=(10, 6))
# sns.countplot(data=sales_df, x='Sales_Channel', palette='Set3', ax=ax)
# plt.title('Distribusi Pesanan Berdasarkan Sales Channel', fontsize=14, fontweight='bold')
# ax.set_xlabel("Sales Channel")
# ax.set_ylabel("Jumlah Pesanan")
# st.pyplot(fig)
# st.write("""
# 📌 **Penjelasan:** Analisis ini menunjukkan performa dari berbagai saluran penjualan seperti in-store, online, distributor, dan wholesale.
# Saluran penjualan yang paling aktif dapat membantu perusahaan fokus pada strategi pemasaran yang tepat.
# """)

# # 8. Analisis Diskon terhadap Penjualan dengan korelasi tambahan
# st.subheader("🔖 Dampak Diskon terhadap Penjualan")
# fig, ax = plt.subplots(figsize=(10, 6))
# sns.scatterplot(data=sales_df, x='Discount_Applied', y='_SalesTeamID', hue='_StoreID', palette='coolwarm', ax=ax)
# plt.title('Hubungan Diskon dengan Penjualan', fontsize=14, fontweight='bold')
# ax.set_xlabel("Diskon Diterapkan (%)")
# ax.set_ylabel("Total Penjualan")
# st.pyplot(fig)
# st.write("""
# 📌 **Penjelasan:** Hubungan antara diskon dan penjualan dapat dilihat melalui scatter plot ini. 
# Perlu dianalisis lebih dalam apakah penjualan meningkat seiring dengan bertambahnya diskon, atau justru menurunkan profitabilitas.
# """)

# # 9. Durasi Pemesanan dan Penjualan dengan distribusi tersegmentasi
# st.subheader("⏱ Distribusi Durasi Pemesanan")
# fig, ax = plt.subplots(figsize=(10, 6))
# sns.histplot(sales_df['Order_Duration'], bins=20, kde=True, color='lightgreen', ax=ax)
# plt.title('Distribusi Durasi Pemesanan', fontsize=14, fontweight='bold')
# ax.set_xlabel("Durasi Pemesanan (Hari)")
# ax.set_ylabel("Frekuensi")
# st.pyplot(fig)
# st.write("""
# 📌 **Penjelasan:** Durasi pemesanan rata-rata dapat memberikan insight tentang kecepatan pengiriman produk.
# Menganalisis lebih dalam apakah durasi pengiriman yang lebih lama mempengaruhi kepuasan pelanggan.
# """)

# # 10. Analisis Performa Produk: Produk Terlaris dengan tambahan filter
# st.subheader("🏆 Top 10 Produk Terlaris")
# top_products = sales_df.groupby('_ProductID')['Order_Quantity'].sum().nlargest(10)
# fig, ax = plt.subplots(figsize=(10, 6))
# sns.barplot(x=top_products.index, y=top_products.values, palette='cool', ax=ax)
# plt.title('Top 10 Produk dengan Penjualan Tertinggi', fontsize=14, fontweight='bold')
# ax.set_xlabel("Product ID")
# ax.set_ylabel("Total Kuantitas Terjual")
# st.pyplot(fig)
# st.write("""
# 📌 **Penjelasan:** Mengetahui produk-produk terlaris akan membantu perusahaan fokus pada produk yang paling diminati untuk meningkatkan penjualan.
# """)

# # 11. Analisis Tren Penjualan Bulanan dengan data smoothing
# sales_df['OrderDate'] = pd.to_datetime(sales_df['OrderDate'], errors='coerce')
# monthly_sales = sales_df.groupby(sales_df['OrderDate'].dt.to_period("M")).sum(numeric_only=True)

# # Smoothing with rolling mean
# monthly_sales['smoothed_sales'] = monthly_sales['_SalesTeamID'].rolling(window=3, center=True).mean()

# st.subheader("📈 Tren Penjualan Bulanan dengan Smoothing")
# fig, ax = plt.subplots(figsize=(12, 6))
# monthly_sales['smoothed_sales'].plot(ax=ax, color='blue', label='Smoothed Sales', linewidth=2)
# monthly_sales['_SalesTeamID'].plot(ax=ax, color='gray', linestyle='--', label='Original Sales', alpha=0.6)

# plt.title('Tren Penjualan Bulanan', fontsize=14, fontweight='bold')
# ax.set_xlabel('Bulan')
# ax.set_ylabel('Total Penjualan')
# ax.legend()
# st.pyplot(fig)
# st.write("""
# 📌 **Penjelasan:** Grafik menunjukkan tren penjualan bulanan dengan data smoothing. 
# Data asli dan hasil smoothing ditampilkan untuk membantu melihat pola tren yang lebih jelas, yang dapat membantu dalam merencanakan promosi musiman.
# """)

# # 8. Analisis Korelasi Antar Variabel Numerik
# st.subheader("🔗 Analisis Korelasi antar Variabel Numerik")
# fig, ax = plt.subplots(figsize=(10, 6))
# correlation_matrix = sales_df.corr(numeric_only=True)
# sns.heatmap(correlation_matrix, annot=True, cmap='Blues', linewidths=0.5, ax=ax)
# plt.title('Heatmap Korelasi')
# st.pyplot(fig)

# # 9. Analisis Outliers di Sales Amount
# st.subheader("🚨 Analisis Outliers di Sales Amount")
# fig, ax = plt.subplots(figsize=(10, 6))
# sns.boxplot(data=sales_df, y='_SalesTeamID', color='lightcoral', ax=ax)
# plt.title('Analisis Outliers di Sales Amount')
# st.pyplot(fig)