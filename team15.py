import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import io

# Judul aplikasi di Streamlit
st.title("📊 Dataset Team 15")
st.title("Dipahami dulu ya... kalau ada ide baru boleh disampaikan 🙌")
# Load dataset (sesuaikan dengan lokasi file kamu)
file_path = 'datasheet.xlsx'

# Fungsi untuk menampilkan data sample dan informasinya
def display_sheet_info(sheet_name, n_rows=5):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    df.columns = df.columns.str.replace(' ', '_')

    st.subheader(f"📋 Data Sample - {sheet_name}")

    # Input untuk mengatur jumlah baris yang ditampilkan
    n_rows_to_display = st.number_input(f"Jumlah baris yang ditampilkan ({sheet_name})", min_value=1, value=n_rows)
    st.dataframe(df.head(n_rows_to_display))

    st.write(f"Dataset ini memiliki **{df.shape[0]} baris** dan **{df.shape[1]} kolom**.")

    st.subheader("📊 Informasi Data")
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()
    st.text(info_str)

    st.subheader("🔍 Missing Values")
    missing_values = df.isnull().sum()
    st.write(missing_values[missing_values > 0])

# Tampilkan informasi untuk setiap sheet
sheet_names = ['Sales Orders Sheet', 'Customers Sheet', 'Store Locations Sheet', 
               'Products Sheet', 'Regions Sheet', 'Sales Team Sheet']

for sheet_name in sheet_names:
    display_sheet_info(sheet_name)



# Judul aplikasi di Streamlit
st.title("📊 Exploratory Data Analysis (EDA) untuk Dataset US_Regional_Sales_Data sebagai insight dan acuan pemilihan topik")


# Load dataset
@st.cache_data
def load_data(file_path):
    return pd.read_excel(file_path, sheet_name='Sales Orders Sheet')

file_path = 'datasheet.xlsx'  # Sesuaikan dengan lokasi file kamu
sales_df = load_data(file_path)

# Data Preparation: Mengganti nama kolom dan mengubah tipe data
def prepare_data(df):
    df.columns = df.columns.str.replace(' ', '_')
    df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')
    df['ShipDate'] = pd.to_datetime(df['ShipDate'], errors='coerce')
    df['Order_Duration'] = (df['ShipDate'] - df['OrderDate']).dt.days
    return df

sales_df = prepare_data(sales_df)

# # 5. Visualisasi Distribusi Pesanan Berdasarkan Region
# st.subheader("📍 Distribusi Pesanan Berdasarkan Region")
# fig, ax = plt.subplots(figsize=(10, 6))
# sns.countplot(data=sales_df, x='_StoreID', palette='Set2', ax=ax)
# plt.title('Distribusi Pesanan Berdasarkan Region', fontsize=14, fontweight='bold')
# ax.set_xlabel("Region")
# ax.set_ylabel("Jumlah Pesanan")
# st.pyplot(fig)
# st.write("""
# 📌 **Penjelasan:** Grafik ini menunjukkan distribusi jumlah pesanan di setiap region. 
# Region dengan pesanan terbanyak adalah yang paling berpotensi memberikan keuntungan besar.
# """)

# 4. Visualisasi Distribusi Pesanan Berdasarkan Region (dengan rotasi label)
st.write("📍 *Distribusi Pesanan Berdasarkan Region:*")
fig, ax = plt.subplots(figsize=(10, 6))
region_counts = sales_df['_StoreID'].value_counts().sort_values(ascending=False)
sns.barplot(y=region_counts.index, x=region_counts.values, palette='Set2', ax=ax)
plt.title('Distribusi Pesanan Berdasarkan Region')
plt.xlabel('region')
plt.ylabel('jumlah pesanan')
plt.tight_layout()
# Menampilkan grafik di Streamlit
st.pyplot(fig)
# 5. Penjelasan
st.write("📌 * Grafik ini memberikan gambaran jelas tentang sebaran jumlah pesanan di berbagai region. Dengan menggunakan grafik batang horizontal, kita dapat dengan mudah membandingkan jumlah pesanan antar region. Region yang memiliki batang lebih panjang menunjukkan jumlah pesanan yang lebih tinggi, mengindikasikan potensi pasar yang lebih besar di region tersebut")

# 6. Visualisasi Total Penjualan per Region dengan log scale untuk melihat distribusi yang lebih jelas
st.subheader("💰 Total Penjualan Berdasarkan Region")
sales_per_region = sales_df.groupby('_StoreID')['_SalesTeamID'].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=sales_per_region.index, y=sales_per_region.values, palette='Set1', ax=ax)
ax.set_yscale('log')  # Using log scale to better visualize variations in total sales
plt.title('Total Penjualan Berdasarkan Region (Log Scale)', fontsize=14, fontweight='bold')
ax.set_xlabel("Region")
ax.set_ylabel("Total Penjualan (log)")
st.pyplot(fig)
st.write("""
📌 **Penjelasan:** Grafik ini menampilkan total penjualan di setiap region menggunakan skala logaritmik pada sumbu vertikal. Skala log membantu memvisualisasikan perbedaan besar dalam total penjualan antar region. 
    Hal ini berguna ketika ada beberapa region dengan penjualan sangat tinggi yang dapat mendominasi grafik jika menggunakan skala linear biasa. Dengan skala log, kita dapat melihat variasi penjualan di semua region dengan lebih jelas.
""")

# 7. Analisis Saluran Penjualan dengan interaktivitas tambahan
st.subheader("🛒 Distribusi Pesanan Berdasarkan Sales Channel")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=sales_df, x='Sales_Channel', palette='Set3', ax=ax)
plt.title('Distribusi Pesanan Berdasarkan Sales Channel', fontsize=14, fontweight='bold')
ax.set_xlabel("Sales Channel")
ax.set_ylabel("Jumlah Pesanan")
st.pyplot(fig)
st.write("""
📌 **Penjelasan:** Grafik ini menunjukkan jumlah pesanan yang diterima melalui berbagai saluran penjualan (in-store, online, distributor, wholesale). Dengan membandingkan ketinggian batang, kita dapat mengidentifikasi saluran penjualan mana yang paling efektif dalam menghasilkan pesanan. 
    Informasi ini sangat berharga untuk menentukan strategi pemasaran dan alokasi sumber daya yang tepat.
""")

# 8. Analisis Diskon terhadap Penjualan dengan korelasi tambahan
st.subheader("🔖 Dampak Diskon terhadap Penjualan")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=sales_df, x='Discount_Applied', y='_SalesTeamID', hue='_StoreID', palette='coolwarm', ax=ax)
plt.title('Hubungan Diskon dengan Penjualan', fontsize=14, fontweight='bold')
ax.set_xlabel("Diskon Diterapkan (%)")
ax.set_ylabel("Total Penjualan")
st.pyplot(fig)
st.write("""
📌 **Penjelasan:** Scatter plot ini menggambarkan hubungan antara diskon yang diberikan dan total penjualan yang dihasilkan. Setiap titik mewakili satu transaksi, dengan warna menunjukkan region terkait. 
    Dengan mengamati pola titik-titik, kita dapat melihat apakah ada korelasi antara diskon dan penjualan. Misalnya, jika titik-titik cenderung naik ke kanan, berarti diskon yang lebih tinggi cenderung menghasilkan penjualan yang lebih tinggi. Namun, perlu analisis lebih lanjut untuk memahami dampak diskon terhadap profitabilitas secara keseluruhan.
""")

# 9. Durasi Pemesanan dan Penjualan dengan distribusi tersegmentasi
st.subheader("⏱ Distribusi Durasi Pemesanan")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(sales_df['Order_Duration'], bins=20, kde=True, color='lightgreen', ax=ax)
plt.title('Distribusi Durasi Pemesanan', fontsize=14, fontweight='bold')
ax.set_xlabel("Durasi Pemesanan (Hari)")
ax.set_ylabel("Frekuensi")
st.pyplot(fig)
st.write("""
📌 **Penjelasan:** Histogram ini menunjukkan distribusi durasi pemesanan (waktu antara tanggal pesanan dan tanggal pengiriman). Bentuk distribusi dan letak puncaknya memberikan gambaran tentang seberapa cepat pesanan biasanya diproses dan dikirim. 
    Informasi ini penting untuk memahami efisiensi operasional dan mengidentifikasi potensi area perbaikan dalam proses pemenuhan pesanan.
""")

# 10. Analisis Performa Produk: Produk Terlaris dengan tambahan filter
st.subheader("🏆 Top 10 Produk Terlaris")
top_products = sales_df.groupby('_ProductID')['Order_Quantity'].sum().nlargest(10)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_products.index, y=top_products.values, palette='cool', ax=ax)
plt.title('Top 10 Produk dengan Penjualan Tertinggi', fontsize=14, fontweight='bold')
ax.set_xlabel("Product ID")
ax.set_ylabel("Total Kuantitas Terjual")
st.pyplot(fig)
st.write("""
📌 **Penjelasan:** Grafik batang ini menampilkan 10 produk dengan penjualan tertinggi berdasarkan total kuantitas terjual. 
    Dengan mengetahui produk-produk terlaris, perusahaan dapat fokus pada strategi pemasaran dan pengelolaan inventaris yang tepat untuk produk-produk tersebut.
""")

# 11. Analisis Tren Penjualan Bulanan dengan data smoothing
sales_df['OrderDate'] = pd.to_datetime(sales_df['OrderDate'], errors='coerce')
monthly_sales = sales_df.groupby(sales_df['OrderDate'].dt.to_period("M")).sum(numeric_only=True)

# Smoothing with rolling mean
monthly_sales['smoothed_sales'] = monthly_sales['_SalesTeamID'].rolling(window=3, center=True).mean()

st.subheader("📈 Tren Penjualan Bulanan dengan Smoothing")
fig, ax = plt.subplots(figsize=(12, 6))
monthly_sales['smoothed_sales'].plot(ax=ax, color='blue', label='Smoothed Sales', linewidth=2)
monthly_sales['_SalesTeamID'].plot(ax=ax, color='gray', linestyle='--', label='Original Sales', alpha=0.6)

plt.title('Tren Penjualan Bulanan', fontsize=14, fontweight='bold')
ax.set_xlabel('Bulan')
ax.set_ylabel('Total Penjualan')
ax.legend()
st.pyplot(fig)
st.write("""
📌 **Penjelasan:** Grafik garis ini menunjukkan tren penjualan bulanan dari waktu ke waktu. Garis biru mewakili data penjualan asli, sedangkan garis abu-abu menunjukkan data yang telah dihaluskan (smoothing) untuk mengurangi fluktuasi acak dan melihat pola tren yang lebih jelas. 
    Dengan mengamati tren ini, perusahaan dapat mengidentifikasi pola musiman, memprediksi penjualan di masa depan, dan merencanakan strategi penjualan yang sesuai.
""")

# 8. Analisis Korelasi Antar Variabel Numerik
st.subheader("🔗 Analisis Korelasi antar Variabel Numerik")
fig, ax = plt.subplots(figsize=(10, 6))
correlation_matrix = sales_df.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap='Blues', linewidths=0.5, ax=ax)
plt.title('Heatmap Korelasi')
st.pyplot(fig)
st.write("""
📌 **Penjelasan:** Heatmap ini menunjukkan korelasi antara berbagai variabel numerik dalam dataset. Semakin terang warna biru pada suatu sel, semakin kuat korelasi positif antara dua variabel tersebut. 
    Sebaliknya, warna biru yang lebih gelap menunjukkan korelasi negatif. Informasi ini berguna untuk mengidentifikasi hubungan antara variabel-variabel yang berbeda dan memahami faktor-faktor yang mungkin mempengaruhi penjualan.
""")

# 9. Analisis Outliers di Sales Amount
st.subheader("🚨 Analisis Outliers di Sales Amount")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=sales_df, y='_SalesTeamID', color='lightcoral', ax=ax)
plt.title('Analisis Outliers di Sales Amount')
st.pyplot(fig)
st.write("""
📌 **Penjelasan:** Box plot ini membantu mengidentifikasi outliers (nilai ekstrem) dalam total penjualan. Titik-titik di luar batas atas dan bawah box plot dianggap sebagai outliers. 
    Outliers ini perlu dianalisis lebih lanjut untuk memahami penyebabnya, apakah merupakan kesalahan data atau transaksi yang benar-benar luar biasa.
""")

# Rekomendasi Topik untuk Analisis Lanjutan
st.subheader("💡 Rekomendasi Topik untuk analisis project capstone")
st.write("""
1. **Evaluasi Efektivitas Saluran Penjualan berdasarkan region**: Analisis ini sangat relevan karena kita telah melihat visualisasi distribusi pesanan berdasarkan saluran penjualan. 
                                                                  Analisis lebih lanjut dapat menggali lebih dalam tentang performa masing-masing saluran, seperti membandingkan total penjualan, profitabilitas, atau menganalisis bagaimana kontribusi tiap saluran berbeda di setiap region.
2. **Dampak Diskon terhadap Profitabilitas**: Investigasi lebih lanjut apakah diskon besar meningkatkan atau justru menurunkan profitabilitas.
3. **Performa Produk di Region Berbeda**: Mengetahui produk mana yang laku di region tertentu bisa memberikan insight untuk strategi pemasaran yang lebih baik.
4. **Customer Satisfaction & Order Duration**: Apakah durasi pemesanan berdampak pada tingkat kepuasan pelanggan?
""")