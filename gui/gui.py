import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from backend.vendor_manager import view_vendors

GREEN = "#079879"
DARK_GREEN = "#087F68"
LIGHT_GREEN = "#E5F5F0"
BACKGROUND = "#F7F8FA"
TEXT = "#222831"
MUTED = "#7B858D"
BORDER = "#EDF0F2"
RED = "#F04444"
DARK = "#242D3C"
class Dashboard:
    def __init__(self, app):
        self.app = app
        self.content = ctk.CTkFrame(
            app,
            fg_color="white",
            corner_radius=0
        )
        self.content.pack(
            fill="both",
            expand=True
        )
        self.create_topbar()
        # Scrollable dashboard body
        self.body = ctk.CTkScrollableFrame(
            self.content,
            fg_color=BACKGROUND,
            corner_radius=12
        )
        self.body.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=(5, 0)
        )
        self.create_heading()
        self.create_statistics()
        self.create_analytics()

    def create_topbar(self):
        topbar = ctk.CTkFrame(
            self.content,
            height=48,
            fg_color="white",
            corner_radius=0
        )
        topbar.pack(fill="x", padx=10)
        topbar.pack_propagate(False)
        navigation = ctk.CTkFrame(
            topbar,
            fg_color="transparent"
        )
        navigation.pack(side="left", padx=5)

        tabs = ["Dashboard", "Reports", "Campaigns",
                "Team Management"]
        for index, tab in enumerate(tabs):
            ctk.CTkButton(
                navigation,
                text=tab,
                height=30,
                corner_radius=15,
                font=("Segoe UI", 11),
                fg_color=GREEN if index == 0 else "#F5F6F8",
                text_color="white" if index == 0 else TEXT,
                hover_color=LIGHT_GREEN,
                command=lambda name=tab: self.top_tab_message(name)
            ).pack(side="left", padx=3, pady=8)
        ctk.CTkLabel(
            topbar,
            text="●",
            text_color=GREEN,
            font=("Arial", 15)
        ).pack(side="right", padx=12)

    def top_tab_message(self, name):
        if name != "Dashboard":
            print(name, "section will be implemented later.")

    def create_heading(self):
        heading = ctk.CTkFrame(
            self.body,
            fg_color="transparent"
        )
        heading.pack(fill="x", padx=8, pady=(10, 14))
        ctk.CTkLabel(
            heading,
            text="Dashboard",
            font=("Segoe UI", 25, "bold"),
            text_color=TEXT
        ).pack(anchor="w")
        ctk.CTkLabel(
            heading,
            text="Garbage Collection and Disposal Services",
            font=("Segoe UI", 11),
            text_color=MUTED
        ).pack(anchor="w", pady=(2, 0))

    def create_statistics(self):
        stats_frame = ctk.CTkFrame(
            self.body,
            fg_color="transparent"
        )
        stats_frame.pack(fill="x", padx=5, pady=(0, 10))
        total_vendors = len(view_vendors())
        statistics = [
            ("Total Vendors", "01", "Registered vendors"),
            ("New Requests", "00", "Awaiting collection"),
            ("Declined Requests", "00", "Review requests"),
            ("Pending Requests", "00", "Waiting for attention")
        ]
        for index, (title, value, description) in enumerate(statistics):
            stats_frame.grid_columnconfigure(
                index,
                weight=1,
                uniform="stats"
            )
            card = ctk.CTkFrame(
                stats_frame,
                fg_color=GREEN if index == 0 else "white",
                corner_radius=12,
                border_width=1 if index != 0 else 0,
                border_color=BORDER
            )
            card.grid(
                row=0,
                column=index,
                sticky="nsew",
                padx=4,
                pady=3
            )
            main_text = "white" if index == 0 else TEXT
            sub_text = "#E4FFF6" if index == 0 else MUTED
            ctk.CTkLabel(
                card,
                text=title,
                font=("Segoe UI", 11),
                text_color=main_text
            ).pack(anchor="w", padx=12, pady=(13, 4))
            ctk.CTkLabel(
                card,
                text=value,
                font=("Segoe UI", 23, "bold"),
                text_color=main_text
            ).pack(anchor="w", padx=12, pady=(0, 3))
            ctk.CTkLabel(
                card,
                text=description,
                font=("Segoe UI", 9),
                text_color=sub_text
            ).pack(anchor="w", padx=12, pady=(0, 13))

    def create_analytics(self):
        # Two-column layout
        self.body.grid_columnconfigure(0, weight=3)
        self.body.grid_columnconfigure(1, weight=2)
        analytics = ctk.CTkFrame(
            self.body,
            fg_color="transparent"
        )
        analytics.pack(fill="both", expand=True, padx=4)
        analytics.grid_columnconfigure(0, weight=3)
        analytics.grid_columnconfigure(1, weight=2)
        left_column = ctk.CTkFrame(
            analytics,
            fg_color="transparent"
        )
        left_column.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=4
        )
        left_column.grid_columnconfigure(0, weight=1)
        right_column = ctk.CTkFrame(
            analytics,
            fg_color="transparent"
        )
        right_column.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=4
        )
        right_column.grid_columnconfigure(0, weight=1)
        # Pickup bar chart
        self.create_bar_chart(left_column)
        # Today's requests timeline
        self.create_timeline(left_column)

        self.create_donut_chart(
            right_column,
            "Avg. Pickups",
            [60, 25, 15],
            ["Successful Pickups", "Declined Pickups",
             "Pending Pickups"],
            [GREEN, RED, DARK]
        )

        self.create_donut_chart(
            right_column,
            "Avg. Recycle",
            [49, 31, 20],
            ["Recycle Complete", "Under Process",
             "Total Collections"],
            [GREEN, DARK, RED],
            center_text="49%"
        )
        # Smooth trend chart
        self.create_line_chart(right_column)

    def create_chart_card(self, parent, title):
        card = ctk.CTkFrame(
            parent,
            fg_color="white",
            corner_radius=12,
            border_width=1,
            border_color=BORDER
        )
        card.pack(
            fill="both",
            expand=True,
            pady=4
        )
        ctk.CTkLabel(
            card,
            text=title,
            font=("Segoe UI", 13, "bold"),
            text_color=TEXT
        ).pack(anchor="w", padx=13, pady=(12, 3))
        return card

    def create_bar_chart(self, parent):
        card = self.create_chart_card(
            parent,
            "Pickup Analytics"
        )
        figure = Figure(figsize=(5, 1.65), dpi=90)
        figure.patch.set_facecolor("white")
        chart = figure.add_subplot(111)
        days = ["Mon", "Tue", "Wed", "Thu",
                "Fri", "Sat", "Sun"]
        pickups = [42, 25, 48, 28, 58, 35, 44]
        chart.bar(
            days,
            pickups,
            color=GREEN,
            width=0.58
        )
        chart.set_facecolor("white")
        chart.spines["top"].set_visible(False)
        chart.spines["right"].set_visible(False)
        chart.spines["left"].set_visible(False)
        chart.spines["bottom"].set_visible(False)
        chart.set_yticks([])
        chart.tick_params(
            axis="x",
            labelsize=8,
            colors=MUTED,
            length=0
        )
        chart.set_ylim(0, 70)
        figure.tight_layout(pad=1)
        canvas = FigureCanvasTkAgg(
            figure,
            master=card
        )
        canvas.draw()
        canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=8,
            pady=(0, 8)
        )

    def create_donut_chart(self,parent, title, values,labels,colors,center_text=None):
        card = self.create_chart_card(parent, title)
        figure = Figure(figsize=(3, 1.65), dpi=90)
        figure.patch.set_facecolor("white")
        chart = figure.add_subplot(111)
        chart.pie(
            values,
            colors=colors,
            startangle=90,
            counterclock=False,
            wedgeprops={
                "width": 0.28,
                "edgecolor": "white",
                "linewidth": 2
            }
        )
        if center_text:
            chart.text(0,0.08,center_text,ha="center",va="center",fontsize=17,fontweight="bold",color=TEXT)
            chart.text( 0,-0.19,"Recycled",ha="center",va="center",fontsize=8,color=MUTED)

        chart.set_aspect("equal")
        figure.tight_layout(pad=0.1)
        canvas = FigureCanvasTkAgg(
            figure,
            master=card
        )
        canvas.draw()
        canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=8,
            pady=(0, 0)
        )

        # Chart legend
        legend = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )
        legend.pack(
            fill="x",
            padx=10,
            pady=(0, 10)
        )
        for label, color in zip(labels, colors):

            ctk.CTkLabel(
                legend,
                text=f"● {label}",
                font=("Segoe UI", 8),
                text_color=TEXT
            ).pack(anchor="w", pady=1)

    def create_timeline(self, parent):
        card = self.create_chart_card(
            parent,
            "Today's Requests"
        )
        timeline = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )
        timeline.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=8
        )
        times = [
            ("10:00", "Request 01", GREEN),
            ("12:00", "Request 02", DARK),
            ("14:00", "Request 03", GREEN),
            ("16:00", "Request 04", RED)
        ]
        for time, request, color in times:
            row = ctk.CTkFrame(
                timeline,
                fg_color="#F8F9FA",
                corner_radius=7
            )
            row.pack(
                fill="x",
                pady=3
            )
            ctk.CTkLabel(
                row,
                text=time,
                font=("Segoe UI", 10, "bold"),
                text_color=MUTED,
                width=55
            ).pack(side="left", padx=8, pady=7)
            ctk.CTkLabel(
                row,
                text="●",
                font=("Arial", 11),
                text_color=color
            ).pack(side="left", padx=3)
            ctk.CTkLabel(
                row,
                text=request,
                font=("Segoe UI", 10),
                text_color=TEXT
            ).pack(side="left", padx=5)

    def create_line_chart(self, parent):
        card = self.create_chart_card(
            parent,
            "Pickup Analytics — Trend"
        )

        figure = Figure(figsize=(4, 1.35), dpi=90)
        figure.patch.set_facecolor("white")
        chart = figure.add_subplot(111)
        hours = list(range(8))
        collections = [18, 10, 25, 21, 34, 16, 28, 42]
        chart.plot(
            hours,
            collections,
            color=GREEN,
            linewidth=2.2
        )
        chart.fill_between(
            hours,
            collections,
            min(collections) - 5,
            color=GREEN,
            alpha=0.08
        )
        chart.set_facecolor("white")
        chart.spines["top"].set_visible(False)
        chart.spines["right"].set_visible(False)
        chart.spines["left"].set_visible(False)
        chart.spines["bottom"].set_visible(False)
        chart.set_xticks([])
        chart.set_yticks([])
        chart.tick_params(length=0)
        figure.tight_layout(pad=0.4)
        canvas = FigureCanvasTkAgg(
            figure,
            master=card
        )
        canvas.draw()
        canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=8,
            pady=(0, 8)
        )