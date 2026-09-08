import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
ventana = ctk.CTk()
ventana.title("Mi primer kiosco")
ventana.geometry("460x360")
ventana.minsize(480, 300)
ventana.grid_columnconfigure(0, weight=1)
titulo = ctk.CTkLabel(
ventana,
text="enner valencia malo",
font=("Arial", 24 , "bold")
)
titulo.grid(row=0, column=0, padx=0, pady=20)

titulo2 = ctk.CTkLabel(
ventana,
text="volve aranda por favor te lo pido",
font=("Arial", 24 , "bold")
)
titulo2.grid(row=1, column=0, padx=0, pady=20)

ventana.mainloop()