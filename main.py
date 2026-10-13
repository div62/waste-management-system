import customtkinter as ctk
from gui.gui import Dashboard
BG_COLOR = "#C9CEE0"
GREEN = "#079879"
LIGHT_GREEN = "#E5F5F0"
TEXT_COLOR = "#222831"
MUTED_COLOR = "#687076"
class BinGoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Window settings
        self.title("BinGo | Smart Waste Management")
        self.geometry("1250x780")
        self.minsize(1050, 680)
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")
        self.configure(fg_color=BG_COLOR)
        # Main white container
        self.container = ctk.CTkFrame(
            self,
            fg_color="white",
            corner_radius=20,
            border_width=1,
            border_color="#FFFFFF"
        )
        self.container.pack(
            fill="both",
            expand=True,
            padx=18,
            pady=18
        )
        # Sidebar
        self.sidebar = ctk.CTkFrame(
            self.container,
            width=175,
            fg_color="#F7F8FA",
            corner_radius=14
        )
        self.sidebar.pack(
            side="left",
            fill="y",
            padx=(12, 5),
            pady=12
        )
        self.sidebar.pack_propagate(False)
        # Logo
        ctk.CTkLabel(
            self.sidebar,
            text="♻️BinGo",
            font=("Segoe UI", 21, "bold"),
            text_color=TEXT_COLOR
        ).pack(pady=(25, 35))
        # Sidebar heading
        ctk.CTkLabel(
            self.sidebar,
            text="MENU",
            font=("Segoe UI", 11, "bold"),
            text_color=MUTED_COLOR
        ).pack(anchor="w", padx=15, pady=(0, 10))
        # Navigation buttons
        menu_items = [
            "Dashboard",
            "Pickup Requests",
            "Vendor Management",
            "Recyclables",
            "Pickup Summary",
            "Reports",
            "Settings"
        ]
        self.menu_buttons = {}
        for item in menu_items:
            button = ctk.CTkButton(
                self.sidebar,
                text=item,
                height=36,
                anchor="w",
                corner_radius=8,
                font=("Segoe UI", 12),
                fg_color=GREEN if item == "Dashboard" else "transparent",
                text_color="white" if item == "Dashboard" else TEXT_COLOR,
                hover_color=LIGHT_GREEN,
                command=lambda name=item: self.navigate(name)
            )
            button.pack(fill="x", padx=9, pady=3)
            self.menu_buttons[item] = button
        # Logout button (visual only for now)
        ctk.CTkButton(
            self.sidebar,
            text="↪  Logout",
            height=35,
            corner_radius=9,
            fg_color=GREEN,
            hover_color="#067D64",
            text_color="white",
            font=("Segoe UI", 12)
        ).pack(side="bottom", fill="x", padx=12, pady=15)
        # Main content area
        self.content = ctk.CTkFrame(
            self.container,
            fg_color="white",
            corner_radius=12
        )
        self.content.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(5, 12),
            pady=12
        )
        # Open dashboard
        self.navigate("Dashboard")
    def navigate(self, page_name):
        # Update selected sidebar button
        for name, button in self.menu_buttons.items():
            if name == page_name:
                button.configure(
                    fg_color=GREEN,
                    text_color="white"
                )
            else:
                button.configure(
                    fg_color="transparent",
                    text_color=TEXT_COLOR
                )
        # Clear previous page
        for widget in self.content.winfo_children():
            widget.destroy()
        # Open selected page
        if page_name == "Dashboard":
            Dashboard(self.content)
        else:
            ctk.CTkLabel(
                self.content,
                text=page_name,
                font=("Segoe UI", 26, "bold"),
                text_color=TEXT_COLOR
            ).pack(anchor="w", padx=25, pady=25)
            ctk.CTkLabel(
                self.content,
                text="This page will be implemented next.",
                font=("Segoe UI", 14),
                text_color=MUTED_COLOR
            ).pack(anchor="w", padx=25)
if __name__ == "__main__":
    app = BinGoApp()
    app.mainloop()