"""from supabase import create_client
from datetime import date

SUPABASE_URL = "https://ravmabpzapwezdazhxia.supabase.co"
SUPABASE_KEY = "sb_publishable_qGcDZpSPBI_IRk8e-DfRZQ_JkNWowMl"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

supabase.table("Prestamos").insert({
    "nombre_cliente": "Juan Perez",
    "monto": 100000,
    "interes": 5000,
    "total_pagar": 105000,
    "fecha_prestamo": str(date.today()),
    "estado": "Activo"
}).execute()

print("Préstamo guardado")"""

import customtkinter as ctk
from tkinter import ttk

from funciones import (
    registrar_prestamo,
    obtener_prestamos,
    eliminar_prestamo,
    marcar_pagado
)
# ---------------- CONFIG ----------------
ctk.set_appearance_mode("dark")

# ---------------- FUNCIONES UI ----------------

def cargar_datos():

    for row in tabla.get_children():
        tabla.delete(row)

    data = obtener_prestamos()

    for item in data:
        tabla.insert("", "end", values=(
    item.get("id", ""),
    item.get("nombre_cliente", ""),
    item.get("monto", ""),
    item.get("interes", ""),
    item.get("total_pagar", ""),
    item.get("estado", ""),
    item.get("fecha_prestamo", "")
))


def registrar():

    nombre = entry_cliente.get()
    monto_texto = entry_monto.get()

    if not nombre or not monto_texto:
        print("Campos vacíos")
        return

    try:
        monto = int(float(monto_texto))

        registrar_prestamo(nombre, monto)

        entry_cliente.delete(0, "end")
        entry_monto.delete(0, "end")

        cargar_datos()

    except Exception as e:
        print("Error:", e)


def eliminar():

    seleccionado = tabla.selection()

    if not seleccionado:
        print("Selecciona un registro")
        return

    item = tabla.item(seleccionado)
    prestamo_id = item["values"][0]

    eliminar_prestamo(prestamo_id)

    cargar_datos()


def pagar():

    seleccionado = tabla.selection()

    if not seleccionado:
        print("Selecciona un registro")
        return

    item = tabla.item(seleccionado)
    prestamo_id = item["values"][0]

    marcar_pagado(prestamo_id)

    cargar_datos()


# ---------------- VENTANA ----------------

ventana = ctk.CTk()
ventana.title("QCAZE - Sistema de Préstamos")
ventana.geometry("1000x650")

titulo = ctk.CTkLabel(
    ventana,
    text="QCAZE - Sistema de Préstamos",
    font=("Arial", 24, "bold"),
    text_color="white"
)
titulo.pack(pady=20)

# ---------------- FORMULARIO ----------------

frame_formulario = ctk.CTkFrame(ventana)
frame_formulario.pack(pady=10)

ctk.CTkLabel(
    frame_formulario,
    text="Nombre del cliente",
    font=("Arial", 16, "bold")
).grid(row=0, column=0, padx=10, pady=10)

entry_cliente = ctk.CTkEntry(frame_formulario, width=250)
entry_cliente.grid(row=0, column=1, padx=10)

ctk.CTkLabel(
    frame_formulario,
    text="Monto",
    font=("Arial", 16, "bold")
).grid(row=1, column=0, padx=10, pady=10)

entry_monto = ctk.CTkEntry(frame_formulario, width=250)
entry_monto.grid(row=1, column=1, padx=10)

ctk.CTkButton(
    frame_formulario,
    text="Registrar Préstamo",
    command=registrar
).grid(row=2, column=0, columnspan=2, pady=15)

# ---------------- TABLA ----------------

frame_tabla = ctk.CTkFrame(ventana)
frame_tabla.pack(pady=10, fill="both", expand=True)

frame_tabla.grid_rowconfigure(0, weight=1)
frame_tabla.grid_columnconfigure(0, weight=1)

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background="#2b2b2b",
    foreground="white",
    fieldbackground="#2b2b2b",
    rowheight=25
)

style.configure(
    "Treeview.Heading",
    background="#1f538d",
    foreground="white",
    font=("Arial", 10, "bold")
)

tabla = ttk.Treeview(
    frame_tabla,
    columns=("id", "nombre", "monto", "interes", "total", "estado", "fecha"),
    show="headings"
)

tabla.heading("id", text="ID")
tabla.heading("nombre", text="Cliente")
tabla.heading("monto", text="Monto")
tabla.heading("interes", text="Interés")
tabla.heading("total", text="Total")
tabla.heading("estado", text="Estado")
tabla.heading("fecha", text="Fecha")

tabla.column("id", width=60, anchor="center")
tabla.column("nombre", width=180)
tabla.column("monto", width=120, anchor="center")
tabla.column("interes", width=120, anchor="center")
tabla.column("total", width=120, anchor="center")
tabla.column("estado", width=120, anchor="center")
tabla.column("fecha", width=120, anchor="center")

tabla.grid(row=0, column=0, sticky="nsew")

# ---------------- BOTONES ----------------

frame_botones = ctk.CTkFrame(ventana)
frame_botones.pack(pady=10)

ctk.CTkButton(
    frame_botones,
    text="Cargar",
    command=cargar_datos
).grid(row=0, column=0, padx=10)

ctk.CTkButton(
    frame_botones,
    text="Eliminar",
    command=eliminar
).grid(row=0, column=1, padx=10)

ctk.CTkButton(
    frame_botones,
    text="Marcar Pagado",
    command=pagar
).grid(row=0, column=2, padx=10)

# ---------------- INICIO ----------------

ventana.after(200, cargar_datos)

ventana.mainloop()






