# Gui Application for pet ID generator
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class PetAppGui:
    
    def __init__(self, root):
        self.root = root 
        self.root.title("Pet ID Profile Generator")
        self.root.geometry("365x425")
        self.root.configure(bg="#DBA674")
        
        self.input_frame()
        
        self.image = None
        self.upload_image()
        
    def input_frame(self):
        input_frame = tk.LabelFrame(self.root,
            text = "Register Your pet".center(60),
            font = ("Cosmic Sans MS", 12, "bold"),
            padx=15,
            pady= 15,
            bg= "#D8C8C8"
        )
        input_frame.place(x=20, y=20, width=320, height=400)\
        
        tk.Label(input_frame, text = "Pet Name:", bg = "#FFFFFF").pack(anchor="w")
        self.pet_name = tk.Entry(input_frame, font=("Cosmic Sans MS", 11))
        self.pet_name.pack(fill="x", pady=(0,10))
        
        tk.Label(input_frame, text="Animal Type:", bg="#FFFFFF").pack(anchor="w")
        self.entry_type = tk.Entry(input_frame, font=("Cosmic Sans MS", 11))
        self.entry_type.pack(fill="x", pady=(0, 10))

        tk.Label(input_frame, text="Age (Years):", bg="#ffffff").pack(anchor="w")
        self.entry_age = tk.Entry(input_frame, font=("Cosmic Sans MS", 11))
        self.entry_age.pack(fill="x", pady=(0, 15))
        
        self.upload_button = tk.Button(
            self.input_frame, text = "🖼️ Upload Pet Photo (Optional)",
            command=self.upload_image, bg="#C5AF88", relief="flat"
        )
        self.upload_button.pack(fill="x", pady=(0, 20))
        
        generate_button = tk.Button(input_frame, text="Generate Pet ID Card",
            command= self.generate_id, bg="#C39696", fg="white",
            qfont=("Cosmic Sans MS", 11, "bold"), relief="flat",
        )
        generate_button.pack(fill="x", pady=(10, 0))
        
        def generate_id(self):
            default_image_file = r"D:\PUP\First year - Second Semester\Object Oriented Programming\encapsulation_abstraction_oop_programs\pet_profile_tracker_management_system\no_profile.png"
            
            if self.image_path:
                check_image = self.image_path
            else:
                check_image = default_image_file
            
            try:
                image = Image.open(check_image)
                image = image.resize((110, 130), Image.Resampling.LANCZOS)
                self.pet_photo = ImageTk.PhotoImage(image)
                self.photo_label_config(image=self.pet_photo, text="")
            except FileNotFoundError:
                self.photo_label_config(text="Image Not Found", font=("Cosmic Sans MS", 10))
            except Exception as e:
                messagebox.showwarning("Image Error!", "Failed to load the photo.")
        
        def upload_image(self):
            file_types = [("Image files", "*.jpg *.jpeg *.png *.bmp")]
            path = filedialog.askopenfilename(title="Select Photo", filetypes=file_types)
        
            if path:
                self.image_path = path
                self.upload_button.config(
                    text="✅ Photo Attached", bg="#1CA23B", fg="#FFFFFF"
                )
        
        def create_id_card_frame(self):
            self.card_frame = tk.Frame(self.root, bg = "#FFFFFF", bd=2, relief="groove")
            self.card_frame.place(x=370, y=45, width=350, height=320)
            
            header = tk.Label(self.card_frame, text="OFFICIAL PET ID", bg="#B0A9A2", fg="#FFFFFF",
                            font=("Cosmic Sans MS", 14, "bold"), pady=8)
            header.pack(fill="x")