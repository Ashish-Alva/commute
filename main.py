import tkinter as tk
from tkinter import filedialog, messagebox
import os

class CommuteApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("COMMUTE WFH")
        self.geometry("900x500")
        self.configure(bg="#2C2F38")

        # ---------- Path Variables ----------
        self.current_path = tk.StringVar(value=os.getcwd())  
        self.select_path = tk.StringVar()

        # Title
        title_label = tk.Label(
            self, text="COMMUTE WFH", font=("Arial", 16, "bold"), bg="#2C2F38", fg="white"
        )
        title_label.pack(side="top", pady=5)

        # Main Frame
        main_frame = tk.Frame(self, bg="#2C2F38")
        main_frame.pack(fill="both", expand=True)

        # Sidebar
        sidebar = tk.Frame(main_frame, bg="#1F2127", width=150)
        sidebar.pack(side="left", fill="y")

        # Content Area
        self.content = tk.Frame(main_frame, bg="#2C2F38")
        self.content.pack(side="right", fill="both", expand=True)

        # Buttons
        buttons = [
            ("Info", self.show_info),
            ("Create folder", self.show_create_folder),
            ("Check files", self.show_check_files),
            ("Translate", self.show_translate),
            ("Consolidate", self.show_consolidate),
            ("Open working file", self.show_open_working_file),
        ]

        for text, command in buttons:
            btn = tk.Button(
                sidebar,
                text=text,
                font=("Arial", 11, "bold"),
                bg="#3C3F47",
                fg="white",
                relief="flat",
                command=command,
                height=2,
                width=18,
            )
            btn.pack(pady=5, padx=10)

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    # ---------- Info page ----------
    def show_info(self):
        self.clear_content()
        tk.Label(self.content, text="Info Page", font=("Arial", 14), bg="#2C2F38", fg="white").pack(pady=20)

    # ---------- Create folder page ----------
    def show_create_folder(self):
        self.clear_content()

        # Instruction text
        tk.Label(
            self.content,
            text="Creates a new folder at the specified path. If no path is provided, the folder is created in the current working directory.",
            wraplength=700,
            justify="left",
            font=("Arial", 10),
            bg="#2C2F38",
            fg="white"
        ).pack(anchor="w", padx=20, pady=10)

        # Current path label
        tk.Label(
            self.content, text="Current path:", bg="#2C2F38", fg="white", font=("Arial", 11, "bold")
        ).pack(anchor="w", padx=20, pady=(10, 0))

        # Show current working directory (read-only)
        current_entry = tk.Entry(self.content, width=60, font=("Arial", 11), textvariable=self.current_path, state="readonly")
        current_entry.pack(padx=20, pady=5, anchor="w")

        # Or text
        tk.Label(self.content, text="Or", bg="#2C2F38", fg="white", font=("Arial", 11, "bold")).pack(pady=5)

        # Select path label
        tk.Label(
            self.content, text="Select path:", bg="#2C2F38", fg="white", font=("Arial", 11, "bold")
        ).pack(anchor="w", padx=20)

        # Frame for Entry + Browse button
        select_frame = tk.Frame(self.content, bg="#2C2F38")
        select_frame.pack(padx=20, pady=5, fill="x")

        select_entry = tk.Entry(select_frame, width=50, font=("Arial", 11), textvariable=self.select_path)
        select_entry.pack(side="left", fill="x", expand=True)

        def browse_path():
            folder = filedialog.askdirectory()
            if folder:
                self.select_path.set(folder)

        browse_btn = tk.Button(
            select_frame,
            text="Browse",
            font=("Arial", 10, "bold"),
            bg="#3C3F47",
            fg="white",
            relief="flat",
            command=browse_path
        )
        browse_btn.pack(side="right", padx=5)

        # Create folder button
        def create_folder():
            path = self.select_path.get().strip()
            if not path:  # if empty, use current path
                path = self.current_path.get()

            try:
                if not os.path.exists(path):
                    os.makedirs(path)
                    messagebox.showinfo("Success", f"Folder created at: {path}")
                else:
                    messagebox.showwarning("Exists", "Folder already exists at this path.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create folder.\n{e}")

        create_btn = tk.Button(
            self.content,
            text="Create folder",
            font=("Arial", 12, "bold"),
            bg="#3C3F47",
            fg="white",
            relief="flat",
            width=20,
            command=create_folder
        )
        create_btn.pack(pady=20)

    # ---------- Check files page ----------
    def show_check_files(self):
        self.clear_content()

        tk.Label(self.content, text="COMMUTE WFH", fg="white", bg="#23272a", font=("Arial", 16, "bold")).pack(pady=10)

        # Frame for top buttons
        button_frame = tk.Frame(self.content, bg="#23272a")
        button_frame.pack(pady=20)

        check_btn = tk.Button(button_frame, text="Check files", command=self.check_files)
        check_btn.grid(row=0, column=0, padx=10)

        create_log_btn = tk.Button(button_frame, text="Create log", command=self.create_log)
        create_log_btn.grid(row=0, column=1, padx=10)

        convert_excel_btn = tk.Button(button_frame, text="Convert to excel", command=self.convert_to_excel)
        convert_excel_btn.grid(row=0, column=2, padx=10)

        # Status Label
        self.status_label = tk.Label(self.content, text="Status will appear here.", fg="white", bg="#23272a", font=("Arial", 12))
        self.status_label.pack(pady=20)

    def check_files(self):
        required_files = ["file1.txt", "file2.txt", "file3.txt"]  # Change to your actual filenames
        missing_files = [f for f in required_files if not os.path.exists(os.path.join(self.current_path.get(), f))]

        if missing_files:
            self.status_label.config(text=f"Missing files: {', '.join(missing_files)}", fg="red")
        else:
            self.status_label.config(text="✅ All required files are present.", fg="lightgreen")

    def create_log(self):
        messagebox.showinfo("Log", "Log created successfully!")

    def convert_to_excel(self):
        messagebox.showinfo("Excel", "Converted to Excel successfully!")

    # ---------- translate page ----------
    def show_translate(self):
        self.clear_content()
        tk.Label(self.content, text="Translate Page", font=("Arial", 14), bg="#2C2F38", fg="white").pack(pady=20)

    # ---------- consolidate page ----------
    def show_consolidate(self):
        self.clear_content()
        tk.Label(self.content, text="Consolidate Page", font=("Arial", 14), bg="#2C2F38", fg="white").pack(pady=20)

    # ---------- open working file page ----------
    def show_open_working_file(self):
        self.clear_content()
        tk.Label(self.content, text="Open Working File Page", font=("Arial", 14), bg="#2C2F38", fg="white").pack(pady=20)


if __name__ == "__main__":
    app = CommuteApp()
    app.mainloop()


