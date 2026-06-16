

#REGISTRAR 

from conexion import supabase
from datetime import date

def registrar_prestamo(nombre, monto):

    interes = monto * 5 // 100
    total = monto + interes

    supabase.table("Prestamos").insert({
        "nombre_cliente": nombre,
        "monto": monto,
        "interes": interes,
        "total_pagar": total,
        "fecha_prestamo": str(date.today()),
        "estado": "Activo"
    }).execute()


#OBTENER DATOS 

def obtener_prestamos():
    return supabase.table("Prestamos").select("*").execute().data

#ELIMINAR

def eliminar_prestamo(id):
    supabase.table("Prestamos").delete().eq("id", id).execute()

def marcar_pagado(id):
    supabase.table("Prestamos").update({
        "estado": "Pagado"
    }).eq("id", id).execute()
