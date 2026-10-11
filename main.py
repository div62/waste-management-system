import customtkinter as ctk
from gui.gui import Dashboard
ctk.set_appearance_mode("Default")
ctk.set_default_color_theme("green")
app = ctk.CTk()
app.title("Smart Waste Management System")
app.geometry("1200x750")
app.minsize(1000, 650)
sidebar = ctk.CTkFrame(
    app,
    width=220,
    fg_color="#FFFFFF",
    corner_radius=0,
    border_width=1,
    border_color="#E4E8EB"
)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

ctk.CTkLabel(
    sidebar,
    text="♻️BinGo",
    font=("Segoe UI", 25, "bold"),
    text_color="#079879"
).pack(pady=(25, 35))

ctk.CTkLabel(
    sidebar,
    text="MAIN MENU",
    font=("Arial", 11, "bold"),
    text_color="#8A939B"
).pack(anchor="w", padx=20, pady=(0, 10))

menu_items = [
    "Dashboard",
    "Pickup Requests",
    "Vendor Management",
    "Recyclables",
    "Pickup Summary",
    "Reports & Analytics",
    "Settings"
]

for item in menu_items:
    ctk.CTkButton(
        sidebar,
        text=item,
        height=40,
        anchor="w",
        fg_color="#E8F8F2" if item == "Dashboard" else "transparent",
        text_color="#078568" if item == "Dashboard" else "#454D55",
        hover_color="#E8F8F2",
        corner_radius=8,
        font=("Arial", 13)
    ).pack(fill="x", padx=12, pady=4)

dashboard = Dashboard(app)

app.mainloop()