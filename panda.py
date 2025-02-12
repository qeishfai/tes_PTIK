import streamlit as st
import sqlite3
import pandas as pd
st.title("hello panda")
st.write("panda pindi")

st.title("BUNGA")
st.image("https://upload.wikimedia.org/wikipedia/commons/b/bd/Helianthus_annuus_exposed_2004-05-22.jpg")

def main():
    st.set_page_config(page_title="Belajar SQL", layout="wide")
    
    st.title("🗄 Pembelajaran Interaktif: SQL")
    st.sidebar.header("Navigasi")
    pilihan = st.sidebar.radio("Pilih Topik:", ["Pengantar", "SELECT", "WHERE", "ORDER BY", "GROUP BY", "HAVING", 
        "INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN"])
    
    if pilihan == "Pengantar":
        show_pengantar()
    elif pilihan == "SELECT":
        show_select()
    elif pilihan == "WHERE":
        show_where()
    elif pilihan == "ORDER BY":
        show_order_by()
    elif pilihan == "GROUP BY":
        show_group_by()
    elif pilihan == "HAVING":
        show_having()
    elif pilihan == "INNER JOIN":
        show_inner_join()
    elif pilihan == "LEFT JOIN":
        show_left_join()
    elif pilihan == "RIGHT JOIN":
        show_right_join()
    elif pilihan == "FULL OUTER JOIN":
        show_full_outer_join()

def show_pengantar():
    st.header("Selamat Datang di Pembelajaran SQL!")
    st.write("""
    *Apa itu SQL?*  
    SQL (Structured Query Language) adalah bahasa pemrograman yang digunakan untuk mengakses, mengelola, dan memanipulasi database. SQL sangat penting dalam dunia teknologi karena hampir semua aplikasi berbasis data menggunakan SQL untuk mengelola informasi.

    *Fungsi SQL*  
    - Mengambil data dari database menggunakan perintah SELECT.
    - Memfilter data berdasarkan kondisi tertentu dengan WHERE.
    - Mengurutkan data dengan ORDER BY.
    - Mengelompokkan data dengan GROUP BY dan HAVING.
    - Menggabungkan tabel menggunakan JOIN (INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN).
    - Melakukan manipulasi data seperti INSERT, UPDATE, dan DELETE.

    Pada pembelajaran ini, Anda akan memahami bagaimana menggunakan SQL secara interaktif dengan mencoba langsung perintah SQL di berbagai skenario.
    """)

def show_sql_section(title, description, query):
    st.header(title)
    st.write(description)
    st.code(query, language='sql')
    
    st.subheader("📋 Data Sebelum Dieksekusi")
    execute_sql_example(show_before=True)
    
    if st.button(f"Run {title}"):
        st.subheader("📊 Hasil Setelah Eksekusi")
        execute_sql_example(query)

def show_select():
    show_sql_section("🔍 SELECT dalam SQL", "SELECT digunakan untuk mengambil data dari database.", "SELECT * FROM Customers;")

def show_where():
    show_sql_section("🔎 WHERE dalam SQL", "WHERE digunakan untuk memfilter data berdasarkan kondisi tertentu.", "SELECT * FROM Customers WHERE CustomerID = 101;")

def show_order_by():
    show_sql_section("📌 ORDER BY dalam SQL", "ORDER BY digunakan untuk mengurutkan hasil query berdasarkan kolom tertentu.", "SELECT * FROM Customers ORDER BY CustomerName ASC;")

def show_group_by():
    show_sql_section("📊 GROUP BY dalam SQL", "GROUP BY digunakan untuk mengelompokkan data berdasarkan satu atau lebih kolom.", "SELECT CustomerID, COUNT(*) FROM Orders GROUP BY CustomerID;")

def show_having():
    show_sql_section("🔢 HAVING dalam SQL", "HAVING digunakan untuk menyaring data setelah GROUP BY.", "SELECT CustomerID, COUNT() FROM Orders GROUP BY CustomerID HAVING COUNT() > 1;")

def show_inner_join():
    show_sql_section("🔗 INNER JOIN dalam SQL", "INNER JOIN digunakan untuk menggabungkan data dari dua tabel berdasarkan kolom yang sesuai.", "SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate FROM Orders INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;")

def show_left_join():
    show_sql_section("⬅ LEFT JOIN dalam SQL", "LEFT JOIN mengembalikan semua baris dari tabel kiri dan hanya baris yang cocok dari tabel kanan.", "SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate FROM Orders LEFT JOIN Customers ON Orders.CustomerID = Customers.CustomerID;")

def execute_sql_example(query=None, show_before=False):
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Orders (OrderID INTEGER, CustomerID INTEGER, OrderDate TEXT);")
    cursor.execute("CREATE TABLE Customers (CustomerID INTEGER, CustomerName TEXT);")
    cursor.execute("INSERT INTO Orders VALUES (1, 101, '2024-01-01'), (2, 102, '2024-02-01'), (3, 103, '2024-03-01');")
    cursor.execute("INSERT INTO Customers VALUES (101, 'Alice'), (102, 'Bob'), (104, 'Charlie');")
    conn.commit()
    
    if show_before:
        st.subheader("📋 Data Sebelum Perubahan")
        customers_df = pd.read_sql_query("SELECT * FROM Customers", conn)
        orders_df = pd.read_sql_query("SELECT * FROM Orders", conn)
        st.write("*Customers Table:*")
        st.dataframe(customers_df)
        st.write("*Orders Table:*")
        st.dataframe(orders_df)
    
    if query:
        try:
            result = pd.read_sql_query(query, conn)
            st.subheader("📊 Data Setelah Perubahan")
            st.dataframe(result)
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

if _name_ == "_main_":
    main()
