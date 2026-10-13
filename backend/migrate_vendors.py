import openpyxl
from pathlib import Path
from backend.database import get_connection
EXCEL_FILE = Path(__file__).resolve().parent.parent / "vendors.xlsx"
def migrate_vendors():
    if not EXCEL_FILE.exists():
        print("Excel file not found!")
        return
    workbook = openpyxl.load_workbook(EXCEL_FILE)
    sheet = workbook.active
    connection = get_connection()
    for row in sheet.iter_rows(min_row=2, values_only=True):
        vendor_id, name, city, area, waste_type = row[:5]
        connection.execute("""
            INSERT INTO vendors
            (vendor_id, name, city, area, waste_type)
            VALUES (?, ?, ?, ?, ?)
        """, (vendor_id, name, city, area, waste_type))
    connection.commit()
    connection.close()
    workbook.close()
    print("Vendor data migrated successfully!")
if __name__ == "__main__":
    migrate_vendors()