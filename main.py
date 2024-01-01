import mysql.connector
from tkinter import Tk, Label, Entry, Button, Listbox, messagebox, ttk

class ZahideDBInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Zahide Veritabanı Arayüzü")

        self.connection = None
        self.cursor = None

        # Başlık etiketi
        self.label = Label(master, text="Zahide Veritabanı Arayüzü", font=("Helvetica", 16, "bold"))
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        # Bağlantı düğmesi
        self.connect_button = Button(master, text="Veritabanına Bağlan", command=self.connect_to_database, bg="#4CAF50", fg="white")
        self.connect_button.grid(row=1, column=0, pady=5, padx=10, sticky="w")

        # Tabloları listele düğmesi
        self.list_tables_button = Button(master, text="Tabloları Listele", command=self.list_tables, bg="#2196F3", fg="white")
        self.list_tables_button.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        # Tablo listesi
        self.table_listbox = Listbox(master, height=5, selectmode="single")
        self.table_listbox.grid(row=2, column=0, columnspan=2, pady=5, padx=10, sticky="w")

        # Treeview tablo
        self.tree = ttk.Treeview(master, columns=("column1", "column2", "column3"), show="headings", selectmode="browse")
        self.tree.grid(row=3, column=0, columnspan=3, pady=5, padx=10, sticky="nsew")

        # Sütun başlıkları
        self.tree.heading("column1", text="Sütun 1")
        self.tree.heading("column2", text="Sütun 2")
        self.tree.heading("column3", text="Sütun 3")

        # Sütun genişlikleri
        self.tree.column("column1", width=100)
        self.tree.column("column2", width=100)
        self.tree.column("column3", width=100)

        # Yatay scrollbar
        xscroll = ttk.Scrollbar(master, orient="horizontal", command=self.tree.xview)
        xscroll.grid(row=4, column=0, columnspan=3, sticky="ew")

        self.tree.configure(xscrollcommand=xscroll.set)

        # Veri göster düğmesi
        self.show_data_button = Button(master, text="Veri Göster", command=self.show_data, bg="#FFC107", fg="black")
        self.show_data_button.grid(row=5, column=0, pady=5, padx=10, sticky="w")

        # Veri ekle düğmesi
        self.insert_data_button = Button(master, text="Veri Ekle", command=self.show_insert_data_popup, bg="#FF5722", fg="white")
        self.insert_data_button.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        # Veri sil düğmesi
        self.delete_data_button = Button(master, text="Veri Sil", command=self.show_delete_data_popup, bg="#E91E63", fg="white")
        self.delete_data_button.grid(row=5, column=2, pady=5, padx=10, sticky="w")

        # Bağlantıyı kes düğmesi
        self.disconnect_button = Button(master, text="Bağlantıyı Kes", command=self.disconnect, bg="#607D8B", fg="white")
        self.disconnect_button.grid(row=6, column=0, columnspan=3, pady=10)

        # Veri ekleme penceresi bileşeni
        self.insert_popup = None
        self.insert_entry1 = None
        self.insert_entry2 = None
        self.insert_entry3 = None

        # Veri silme penceresi bileşeni
        self.delete_popup = None
        self.delete_entry = None

    def connect_to_database(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="zahide"
            )
            self.cursor = self.connection.cursor()
            messagebox.showinfo("Bağlantı", "Veritabanına bağlantı başarılı.")
        except mysql.connector.Error as err:
            messagebox.showerror("Hata", f"Bağlantı hatası: {err}")

    def list_tables(self):
        if self.connection:
            self.cursor.execute("SHOW TABLES")
            tables = self.cursor.fetchall()
            self.table_listbox.delete(0, "end")
            for table in tables:
                self.table_listbox.insert("end", table[0])
        else:
            messagebox.showerror("Hata", "Veritabanına bağlanmadınız.")

    def show_data(self):
        if self.connection and self.table_listbox.curselection():
            selected_table = self.table_listbox.get(self.table_listbox.curselection())
            self.cursor.execute(f"SELECT * FROM {selected_table}")
            data = self.cursor.fetchall()

            # Temizleme
            for row in self.tree.get_children():
                self.tree.delete(row)

            # Verileri ekleme
            for row in data:
                self.tree.insert("", "end", values=row)
        else:
            messagebox.showerror("Hata", "Veritabanına bağlandığınızdan ve bir tablo seçtiğinizden emin olun.")

    def show_insert_data_popup(self):
        self.insert_popup = Tk()
        self.insert_popup.title("Veri Ekle")

        label1 = Label(self.insert_popup, text="Sütun 1:")
        label1.grid(row=0, column=0, padx=10, pady=5)
        self.insert_entry1 = Entry(self.insert_popup)
        self.insert_entry1.grid(row=0, column=1, padx=10, pady=5)

        label2 = Label(self.insert_popup, text="Sütun 2:")
        label2.grid(row=1, column=0, padx=10, pady=5)
        self.insert_entry2 = Entry(self.insert_popup)
        self.insert_entry2.grid(row=1, column=1, padx=10, pady=5)

        label3 = Label(self.insert_popup, text="Sütun 3:")
        label3.grid(row=2, column=0, padx=10, pady=5)
        self.insert_entry3 = Entry(self.insert_popup)
        self.insert_entry3.grid(row=2, column=1, padx=10, pady=5)

        insert_button = Button(self.insert_popup, text="Veri Ekle", command=self.insert_data_to_table)
        insert_button.grid(row=3, column=0, columnspan=2, pady=10)

    def insert_data_to_table(self):
        if self.connection and self.table_listbox.curselection():
            selected_table = self.table_listbox.get(self.table_listbox.curselection())
            values = (
                self.insert_entry1.get(),
                self.insert_entry2.get(),
                self.insert_entry3.get()
            )
            query = f"INSERT INTO {selected_table} VALUES (%s, %s, %s)"
            self.cursor.execute(query, values)
            self.connection.commit()
            messagebox.showinfo("Başarı", "Veri eklendi.")
            self.show_data()
            self.insert_popup.destroy()
        else:
            messagebox.showerror("Hata", "Veritabanına bağlandığınızdan ve bir tablo seçtiğinizden emin olun.")

    def show_delete_data_popup(self):
        self.delete_popup = Tk()
        self.delete_popup.title("Veri Sil")

        label = Label(self.delete_popup, text="Silinecek satırın ID'sini girin:")
        label.grid(row=0, column=0, padx=10, pady=5)
        self.delete_entry = Entry(self.delete_popup)
        self.delete_entry.grid(row=0, column=1, padx=10, pady=5)

        delete_button = Button(self.delete_popup, text="Veri Sil", command=self.delete_data_from_table)
        delete_button.grid(row=1, column=0, columnspan=2, pady=10)

    def delete_data_from_table(self):
        if self.connection and self.table_listbox.curselection():
            selected_table = self.table_listbox.get(self.table_listbox.curselection())
            row_id = self.delete_entry.get()
            query = f"DELETE FROM {selected_table} WHERE id = {row_id}"
            self.cursor.execute(query)
            self.connection.commit()
            messagebox.showinfo("Başarı", "Veri silindi.")
            self.show_data()
            self.delete_popup.destroy()
        else:
            messagebox.showerror("Hata", "Veritabanına bağlandığınızdan ve bir tablo seçtiğinizden emin olun.")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            messagebox.showinfo("Bağlantı", "Veritabanı bağlantısı kesildi.")
            self.master.destroy()
        else:
            messagebox.showerror("Hata", "Zaten bağlı değilsiniz.")

if __name__ == "__main__":
    root = Tk()
    app = ZahideDBInterface(root)
    root.mainloop()
