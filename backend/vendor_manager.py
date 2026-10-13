import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from backend.database import get_connection
def create_vendor_table():
    connection = get_connection()
    connection.execute("""
        CREATE TABLE IF NOT EXISTS vendors (
            vendor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            city TEXT NOT NULL,
            area TEXT NOT NULL,
            waste_type TEXT NOT NULL,
            contact TEXT,
            availability TEXT DEFAULT 'Available')
    """)
    connection.commit()
    connection.close()
def add_vendor(name, city, area, waste_type, contact=""):
    connection = get_connection()
    cursor = connection.execute("""
        INSERT INTO vendors (name, city, area, waste_type, contact)
        VALUES (?, ?, ?, ?, ?)
    """, (name, city, area, waste_type, contact))
    vendor_id = cursor.lastrowid
    connection.commit()
    connection.close()
    return vendor_id
def view_vendors():
    connection = get_connection()
    cursor = connection.execute("""
        SELECT * FROM vendors
    """)
    vendors = cursor.fetchall()
    connection.close()   
    return vendors
def search_vendors(city, waste_type, area=None):
    connection = get_connection()
    query = """
        SELECT * FROM vendors
        WHERE LOWER(city) = LOWER(?)
        AND LOWER(waste_type) = LOWER(?)
    """
    values = [city, waste_type]
    if area:
        query += " AND LOWER(area) = LOWER(?)"
        values.append(area)
    cursor = connection.execute(query, values)
    vendors = cursor.fetchall()
    connection.close()
    return vendors    
def update_vendor(vendor_id, name, city, area, waste_type, contact=""):
    connection = get_connection()
    connection.execute("""
        UPDATE vendors
        SET name = ?,
            city = ?,
            area = ?,
            waste_type = ?,
            contact = ?
        WHERE vendor_id = ?
    """, (name, city, area, waste_type, contact, vendor_id))
    connection.commit()
    connection.close()    
def delete_vendor(vendor_id):
    connection = get_connection()
    cursor = connection.execute("""
        DELETE FROM vendors
        WHERE vendor_id = ?
    """, (vendor_id,))
    connection.commit()
    deleted = cursor.rowcount
    connection.close()
    return deleted    