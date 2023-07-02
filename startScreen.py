import tkinter
from tkinter import *
from PIL import Image, ImageTk

import customtkinter as ctk


class StartScreen(ctk.CTkFrame):
    default_font = ("Ebrima", 32, 'bold')
    default_font_small = ("Ebrima", 18, 'bold')

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=2)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=10)

        self.start_page_content()

    def start_page_content(self):
        frame1 = ctk.CTkFrame(self)
        frame1.grid(column=0, row=0, columnspan=2, sticky="nsew", padx=5, pady=5, ipadx=15)

        ##############  Frame 1 Contents

        username_label = ctk.CTkLabel(frame1, text="DnD Card Generator", font=self.default_font_small)
        username_label.pack(side=ctk.LEFT, padx=15)

        export_button = ctk.CTkButton(frame1, text="Quick Export", font=self.default_font_small)
        export_button.pack(side=ctk.RIGHT, padx=5)

        export_button = ctk.CTkButton(frame1, text="Export", font=self.default_font_small)
        export_button.pack(side=ctk.RIGHT, padx=5)

        reset_button = ctk.CTkButton(frame1, text="Reset", font=self.default_font_small)
        reset_button.pack(side=ctk.RIGHT, padx=5)

        rand_button = ctk.CTkButton(frame1, text="Randomize", font=self.default_font_small)
        rand_button.pack(side=ctk.RIGHT, padx=5)

        ##############
        weapon_frame = ctk.CTkFrame(self)
        weapon_frame.grid(column=0, row=3, sticky="nsew", padx=5, pady=5)

        self.card_type_frame(weapon_frame)

        self.image_import_frame()

        self.image_frame()

    def card_type_frame(self, frame):
        card_type_frame = ctk.CTkFrame(self)
        card_type_frame.grid(column=0, row=1, sticky="nsew", padx=5, pady=5)

        username_label = ctk.CTkLabel(card_type_frame, text="Select Card Type", font=self.default_font)
        username_label.pack(pady=16)

        card_type_grid_frame = ctk.CTkFrame(card_type_frame, bg_color='transparent')
        card_type_grid_frame.pack(pady=5)

        button1 = ctk.CTkButton(card_type_grid_frame, text="Weapon", fg_color="#cfbd00", hover_color="#696003",
                                font=self.default_font_small, command=lambda: self.weapon_content(frame))
        button1.grid(column=0, row=0, sticky="sew", padx=5, pady=5)

        button1 = ctk.CTkButton(card_type_grid_frame, text="Ability", fg_color="#f08502", hover_color="#824800",
                                font=self.default_font_small, command=lambda: self.ability_content(frame))
        button1.grid(column=1, row=0, sticky="sew", padx=5, pady=5)

        button1 = ctk.CTkButton(card_type_grid_frame, text="Armour", fg_color="#e81d07", hover_color="#660b01",
                                font=self.default_font_small)
        button1.grid(column=2, row=0, sticky="sew", padx=5, pady=5)

        button1 = ctk.CTkButton(card_type_grid_frame, text="Proficiency", fg_color="#020bf7", hover_color="#01034f",
                                font=self.default_font_small)
        button1.grid(column=0, row=1, sticky="sew", padx=5, pady=5)

        button1 = ctk.CTkButton(card_type_grid_frame, text="Bonus Action", fg_color="#ed02e9", hover_color="#540153",
                                font=self.default_font_small)
        button1.grid(column=1, row=1, sticky="sew", padx=5, pady=5)

        button1 = ctk.CTkButton(card_type_grid_frame, text="Item", fg_color="#1f9126", hover_color="#0b360e",
                                font=self.default_font_small)
        button1.grid(column=2, row=1, sticky="sew", padx=5, pady=5)

        # button1 = ctk.CTkButton(card_type_grid_frame, text="Artifact", fg_color="#787878", hover_color="#262626",
        #                         font=self.default_font_small)
        # button1.grid(column=0, row=1, sticky="sew", padx=5, pady=5)

    def image_import_frame(self):
        frame = ctk.CTkFrame(self)
        frame.grid(column=0, row=2, sticky="nsew", padx=5, pady=5)

        username_label = ctk.CTkLabel(frame, text="Add Image", font=self.default_font)
        username_label.pack(pady=10)

        import_image_frame = ctk.CTkFrame(frame)
        import_image_frame.pack(pady=20)

        import_button = ctk.CTkButton(import_image_frame, text="Import", font=self.default_font_small)
        import_button.grid(column=0, row=0, sticky="ew")

        canny_detection_chkbox = ctk.CTkCheckBox(frame, text='Egde Detection', onvalue=1, offvalue=0,
                                                 font=self.default_font_small)
        canny_detection_chkbox.pack()

    def delete_all_children_in_frame(self, frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

    def weapon_content(self, frame):
        self.delete_all_children_in_frame(frame)

        username_label4 = ctk.CTkLabel(frame, text="Weapon", font=self.default_font_small)
        username_label4.pack()

        weapon_frame = ctk.CTkFrame(frame)
        weapon_frame.pack()

        weapon_frame.columnconfigure(0, weight=1)
        weapon_frame.columnconfigure(1, weight=4)

        name_line_1_label = ctk.CTkLabel(weapon_frame, text="Line 1 : Name", font=self.default_font_small)
        name_line_1_label.grid(column=0, row=0, padx=10, pady=10)

        name_line_1_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        name_line_1_entry.grid(column=1, row=0, padx=10, pady=10)

        name_line_2_label = ctk.CTkLabel(weapon_frame, text="Line 2 : Name", font=self.default_font_small)
        name_line_2_label.grid(column=0, row=1, padx=10, pady=10)

        name_line_2_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        name_line_2_entry.grid(column=1, row=1, padx=10, pady=10)

        uses_before_overheating_label = ctk.CTkLabel(weapon_frame, text="Uses before Overheating",
                                                     font=self.default_font_small)
        uses_before_overheating_label.grid(column=0, row=2, padx=10, pady=10)

        uses_before_overheating_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        uses_before_overheating_entry.grid(column=1, row=2, padx=10, pady=10)

        overheating_cooldown_label = ctk.CTkLabel(weapon_frame, text="Overheat Cooldown",
                                                  font=self.default_font_small)
        overheating_cooldown_label.grid(column=0, row=3, padx=10, pady=10)

        overheating_cooldown_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        overheating_cooldown_entry.grid(column=1, row=3, padx=10, pady=10)

        range_label = ctk.CTkLabel(weapon_frame, text="Range (in Hex)",
                                   font=self.default_font_small)
        range_label.grid(column=0, row=4, padx=10, pady=10)

        range_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        range_entry.grid(column=1, row=4, padx=10, pady=10)

        hands_label = ctk.CTkLabel(weapon_frame, text="Number of Hands to use",
                                   font=self.default_font_small)
        hands_label.grid(column=0, row=5, padx=10, pady=10)

        hands_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        hands_entry.grid(column=1, row=5, padx=10, pady=10)

        ammo_label = ctk.CTkLabel(weapon_frame, text="Ammo needed to Use",
                                  font=self.default_font_small)
        ammo_label.grid(column=0, row=9, padx=10, pady=10)

        ammo_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        ammo_entry.grid(column=1, row=9, padx=10, pady=10)

        dmg_roll_label = ctk.CTkLabel(weapon_frame, text="Damage Roll",
                                      font=self.default_font_small)
        dmg_roll_label.grid(column=0, row=7, padx=10, pady=10)

        dmg_roll_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        dmg_roll_entry.grid(column=1, row=7, padx=10, pady=10)

        acc_bonus_label = ctk.CTkLabel(weapon_frame, text="Accuracy Bonus",
                                       font=self.default_font_small)
        acc_bonus_label.grid(column=0, row=8, padx=10, pady=10)

        acc_bonus_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        acc_bonus_entry.grid(column=1, row=8, padx=10, pady=10)

        ability_name_label = ctk.CTkLabel(weapon_frame, text="Ability Name",
                                          font=self.default_font_small)
        ability_name_label.grid(column=0, row=6, padx=10, pady=10)

        ability_name_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        ability_name_entry.grid(column=1, row=6, padx=10, pady=10)

        ammo_type_label = ctk.CTkLabel(weapon_frame, text="Ammo Type",
                                       font=self.default_font_small)
        ammo_type_label.grid(column=0, row=10, padx=10, pady=10)

        ammo_type_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        ammo_type_entry.grid(column=1, row=10, padx=10, pady=10)

        enter_button = ctk.CTkButton(weapon_frame, text="Enter", font=self.default_font_small)
        enter_button.grid(column=0, row=11, columnspan=2, padx=10, pady=10)

    def ability_content(self, frame):
        self.delete_all_children_in_frame(frame)

        username_label4 = ctk.CTkLabel(frame, text="Ability", font=self.default_font_small)
        username_label4.pack()

        weapon_frame = ctk.CTkFrame(frame)
        weapon_frame.pack()

        weapon_frame.columnconfigure(0, weight=1)
        weapon_frame.columnconfigure(1, weight=4)

        name_line_1_label = ctk.CTkLabel(weapon_frame, text="Line 1 : Name", font=self.default_font_small)
        name_line_1_label.grid(column=0, row=0, padx=10, pady=10)

        name_line_1_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        name_line_1_entry.grid(column=1, row=0, padx=10, pady=10)

        name_line_2_label = ctk.CTkLabel(weapon_frame, text="Line 2 : Name", font=self.default_font_small)
        name_line_2_label.grid(column=0, row=1, padx=10, pady=10)

        name_line_2_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        name_line_2_entry.grid(column=1, row=1, padx=10, pady=10)

        uses_before_overheating_label = ctk.CTkLabel(weapon_frame, text="Uses before Overheating",
                                                     font=self.default_font_small)
        uses_before_overheating_label.grid(column=0, row=2, padx=10, pady=10)

        uses_before_overheating_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        uses_before_overheating_entry.grid(column=1, row=2, padx=10, pady=10)

        overheating_cooldown_label = ctk.CTkLabel(weapon_frame, text="Overheat Cooldown",
                                                  font=self.default_font_small)
        overheating_cooldown_label.grid(column=0, row=3, padx=10, pady=10)

        overheating_cooldown_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        overheating_cooldown_entry.grid(column=1, row=3, padx=10, pady=10)

        range_label = ctk.CTkLabel(weapon_frame, text="Range (in Hex)",
                                   font=self.default_font_small)
        range_label.grid(column=0, row=4, padx=10, pady=10)

        range_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        range_entry.grid(column=1, row=4, padx=10, pady=10)

        hands_label = ctk.CTkLabel(weapon_frame, text="Number of Hands to use",
                                   font=self.default_font_small)
        hands_label.grid(column=0, row=5, padx=10, pady=10)

        hands_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        hands_entry.grid(column=1, row=5, padx=10, pady=10)

        ammo_label = ctk.CTkLabel(weapon_frame, text="Ammo needed to Use",
                                  font=self.default_font_small)
        ammo_label.grid(column=0, row=9, padx=10, pady=10)

        ammo_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        ammo_entry.grid(column=1, row=9, padx=10, pady=10)

        dmg_roll_label = ctk.CTkLabel(weapon_frame, text="Damage Roll",
                                      font=self.default_font_small)
        dmg_roll_label.grid(column=0, row=7, padx=10, pady=10)

        dmg_roll_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        dmg_roll_entry.grid(column=1, row=7, padx=10, pady=10)

        acc_bonus_label = ctk.CTkLabel(weapon_frame, text="Accuracy Bonus",
                                       font=self.default_font_small)
        acc_bonus_label.grid(column=0, row=8, padx=10, pady=10)

        acc_bonus_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        acc_bonus_entry.grid(column=1, row=8, padx=10, pady=10)

        ability_name_label = ctk.CTkLabel(weapon_frame, text="Ability Name",
                                          font=self.default_font_small)
        ability_name_label.grid(column=0, row=6, padx=10, pady=10)

        ability_name_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        ability_name_entry.grid(column=1, row=6, padx=10, pady=10)

        ammo_type_label = ctk.CTkLabel(weapon_frame, text="Ammo Type",
                                       font=self.default_font_small)
        ammo_type_label.grid(column=0, row=10, padx=10, pady=10)

        ammo_type_entry = ctk.CTkEntry(weapon_frame, font=self.default_font_small, width=300)
        ammo_type_entry.grid(column=1, row=10, padx=10, pady=10)

        enter_button = ctk.CTkButton(weapon_frame, text="Enter", font=self.default_font_small)
        enter_button.grid(column=0, row=11, columnspan=2, padx=10, pady=10)

    def image_frame(self):
        frame = ctk.CTkFrame(self)
        frame.grid(row=1, column=1, rowspan=3)

        scaleFactor = 1.3

        image1 = Image.open("resouces/WEAPOONTEMPLATE.jpg")
        test = image1.resize((round(496 * scaleFactor), round(701 * scaleFactor)), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(test)

        label1 = ctk.CTkLabel(frame, text="", image=test)
        label1.image = test
        label1.pack()
