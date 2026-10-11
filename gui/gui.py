import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class Dashboard:
    def __init__(self, app):
        self.app = app
        self.content = ctk.CTkFrame(
            app,
            fg_color="#F5F6F8",
            corner_radius=0
        )
        self.content.pack(
            side="left",
            fill="both",
            expand=True
        )
        self.topbar = ctk.CTkFrame(
            self.content,
            height=65,
            fg_color="white",
            corner_radius=0
        )
        self.topbar.pack(fill="x")
        self.topbar.pack_propagate(False)
        ctk.CTkLabel(
            self.topbar,
            text="Dashboard",
            font=("Arial", 24, "bold"),
            text_color="#222831"
        ).pack(side="left", padx=25)
        ctk.CTkLabel(
            self.topbar,
            text="Smart Waste Management System",
            font=("Arial", 13),
            text_color="#687076"
        ).pack(side="right", padx=25)
        self.body = ctk.CTkScrollableFrame(
            self.content,
            fg_color="#F5F6F8"
        )
        self.body.pack(fill="both", expand=True, padx=20, pady=20)
        ctk.CTkLabel(
            self.body,
            text="Overview",
            font=("Arial", 28, "bold"),
            text_color="#222831"
        ).pack(anchor="w", pady=(0, 20))
        self.stats_frame = ctk.CTkFrame(
            self.body,
            fg_color="transparent"
        )
        self.stats_frame.pack(fill="x", pady=(0, 20))
        statistics = [
            ("Total Vendors", "0"),
            ("New Requests", "0"),
            ("Completed Pickups", "0"),
            ("Pending Requests", "0")
        ]
        for title, value in statistics:
            card = ctk.CTkFrame(
                self.stats_frame,
                fg_color="white",
                corner_radius=12,
                border_width=1,
                border_color="#E4E8EB"
            )
            card.pack(
                side="left",
                fill="both",
                expand=True,
                padx=6
            )
            ctk.CTkLabel(
                card,
                text=title,
                font=("Arial", 13),
                text_color="#555E66"
            ).pack(anchor="w", padx=15, pady=(20, 8))
            ctk.CTkLabel(
                card,
                text=value,
                font=("Arial", 27, "bold"),
                text_color="#079879"
            ).pack(anchor="w", padx=15, pady=(0, 20))
        self.analytics_frame = ctk.CTkFrame(
            self.body,
            fg_color="transparent"
        )
        self.analytics_frame.pack(fill="both", expand=True)

        chart_card = ctk.CTkFrame(
            self.analytics_frame,
            fg_color="white",
            corner_radius=12,
            border_width=1,
            border_color="#E4E8EB"
        )
        chart_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=6
        )

        ctk.CTkLabel(
            chart_card,
            text="Waste Collection Analytics",
            font=("Arial", 18, "bold"),
            text_color="#222831"
        ).pack(anchor="w", padx=15, pady=15)

        figure = Figure(figsize=(5, 3), dpi=90)
        chart = figure.add_subplot(111)

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        waste = [12, 20, 15, 28, 22, 30, 25]
        chart.bar(days, waste, color="#079879", width=0.6)
        chart.set_ylabel("Waste collected")
        chart.set_facecolor("white")
        figure.patch.set_facecolor("white")
        chart.spines["top"].set_visible(False)
        chart.spines["right"].set_visible(False)
        figure.tight_layout()
        canvas = FigureCanvasTkAgg(
            figure,
            master=chart_card
        )
        canvas.draw()
        canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 15)
        )