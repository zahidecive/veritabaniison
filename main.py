import mysql.connector
from tkinter import Tk, Label, Entry, Button, Listbox, Scrollbar, messagebox

class ZahideDBInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Zahide Veritabanı Arayüzü")

        self.connection = None
        self.cursor = None

        self.label = Label(master, text="Zahide Veritabanı Arayüzü")
        self.label.pack()

        self.connect_button = Button(master, text="Veritabanına Bağlan", command=self.connect_to_database)
        self.connect_button.pack()

        self.list_tables_button = Button(master, text="Tabloları Listele", command=self.list_tables)
        self.list_tables_button.pack()

        self.table_listbox = Listbox(master, height=5, selectmode="single")
        self.table_listbox.pack()

        self.show_data_button = Button(master, text="Veri Göster", command=self.show_data)
        self.show_data_button.pack()

        self.insert_data_button = Button(master, text="Veri Ekle", command=self.insert_data)
        self.insert_data_button.pack()

        self.delete_data_button = Button(master, text="Veri Sil", command=self.delete_data)
        self.delete_data_button.pack()

        self.disconnect_button = Button(master, text="Bağlantıyı Kes", command=self.disconnect)
        self.disconnect_button.pack()

    def connect_to_database(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="your_username",
                password="your_password",
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
            messagebox.showinfo("Veri", f"{selected_table} tablosundaki veriler:\n{data}")
        else:
            messagebox.showerror("Hata", "Veritabanına bağlandığınızdan ve bir tablo seçtiğinizden emin olun.")

    def insert_data(self):
        # Buraya veri ekleme işlemlerini ekleyebilirsiniz.
        pass

    def delete_data(self):
        # Buraya veri silme işlemlerini ekleyebilirsiniz.
        pass

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
