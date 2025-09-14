github: https://www.figma.com/design/SPgof7mOfhH23cAKOdbhX4/Untitled?node-id=0-1&p=f&m=draw

import tkinter as tk
from pages.info_page import InfoPage
from pages.create_folder_page import CreateFolderPage
from pages.check_files_page import CheckFilesPage
from pages.translate_page import TranslatePage
from pages.consolidate_page import ConsolidatePage
from pages.open_working_file_page import OpenWorkingFilePage

class CommuteApp(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("COMMUTE WFH")
        self.geometry("900x500")
        self.configure(bg="#2C2F38")

        self.current_path = tk.StringVar()
        self.select_path  = tk.StringVar()

        # --- Layout frames ---
        sidebar = tk.Frame(self, bg="#1F2127", width=150)
        sidebar.pack(side="left", fill="y")
        self.content = tk.Frame(self, bg="#2C2F38")
        self.content.pack(side="right", fill="both", expand=True)

        # --- Pages ---
        self.pages = {
            "Info": InfoPage(self.content, self),
            "Create": CreateFolderPage(self.content, self),
            "Check": CheckFilesPage(self.content, self),
            "Translate": TranslatePage(self.content, self),
            "Consolidate": ConsolidatePage(self.content, self),
            "Open": OpenWorkingFilePage(self.content, self),
        }
        for page in self.pages.values():
            page.place(relwidth=1, relheight=1)

        # --- Sidebar buttons ---
        for text, key in [
            ("Info","Info"),
            ("Create folder","Create"),
            ("Check files","Check"),
            ("Translate","Translate"),
            ("Consolidate","Consolidate"),
            ("Open working file","Open")
        ]:
            tk.Button(
                sidebar, text=text,
                bg="#3C3F47", fg="white", relief="flat",
                font=("Arial",11,"bold"),
                command=lambda k=key: self.show_page(k)
            ).pack(pady=5, padx=10, fill="x")

        self.show_page("Info")

    def show_page(self, key):
        page = self.pages[key]
        page.tkraise()















        import tkinter as tk
from tkinter import filedialog, messagebox
import os

class CreateFolderPage(tk.Frame):
    def _init_(self, parent, controller):
        super()._init_(parent, bg="#2C2F38")
        self.controller = controller

        tk.Label(self, text="Create Folder", fg="white", bg="#2C2F38",
                 font=("Arial",16,"bold")).pack(pady=10)

        tk.Entry(self, textvariable=controller.select_path,
                 width=50, font=("Arial",11)).pack(pady=5)

        tk.Button(self, text="Browse",
                  command=self.browse).pack()

        tk.Button(self, text="Create Folder",
                  command=self.create_folder).pack(pady=15)

    def browse(self):
        folder = filedialog.askdirectory()
        if folder:
            self.controller.select_path.set(folder)

    def create_folder(self):
        path = self.controller.select_path.get() or os.getcwd()
        os.makedirs(path, exist_ok=True)
        messagebox.showinfo("Success", f"Folder ensured at: {path}")
