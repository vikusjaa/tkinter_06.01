import sqlite3
from tkinter import Tk,Label,Button,END,messagebox,ttk


def init_db():
    try:
        conn=sqlite3.connect('movie.db')
        c=conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS films (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    author TEXT,
                    year INTEGER,
                    genre  TEXT
                )''')
        conn.commit()
        conn.close()

    except Exception as e:
        messagebox.showerror("Datubāzes Ķļūda",f"Neizdevās inicializet datubazi:{e}")
def load_film_titles():
    try:
        film_combobox['values']=()
        conn=sqlite3.connect('movie.db')
        cursor=conn.cursor()
        cursor.execute("SELECT title FROM films")
        titles=[]
        title_all=cursor.fetchall()
        for title in title_all:
            titles.append(title[0])
        conn.close()

        film_combobox['values']=titles

    except Exception as e:
        messagebox.showerror("Ķļūda",f"Neizdevās atrast informāciju par filmu:{e}")

def show_film_details():
    try:
        selected_title=film_combobox.get()
        if not selected_title:
            messagebox.showwarning("Brīdinājums","Lūdzu,izvēlieties filmu no saraksta.")
            return
        
        conn=sqlite3.connect('movie.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM films WHERE title = ?", (selected_title,))
        film=cursor.fetchone()
        conn.close
       
        if film:
         messagebox.showinfo("Filmas informācija",f"Nosaukums: {film[1]}\nAutors: {film[2]}\nIzdošanas Gads: {film[3]}\nŽanrs: {film[4]}")
        else: 
         messagebox.showwarning("Kļūda","Neizdevās atrast informāciju par filmu.")
    except Exception as e:
        messagebox.showerror("Ķļūda",f"Neizdevās parādīt informāciju par filmu.")

     
root=Tk()
root.title("Filmu izvēles sistēma")

Label(root,text="Izvēlēties filmu:").grid(row=0,column=0,padx=10,pady=10)
film_combobox=ttk.Combobox(root,width=47,state="readonly")
film_combobox.grid(row=1,column=0,padx=10,pady=10)

Button(root,text="Rādīt informāciju",command=show_film_details).grid(row=2,column=0,padx=10,pady=10)
 
init_db()
load_film_titles()

root.mainloop()