# Gui Application for pet ID generator
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

from animal_info import Pet
class PetAppGui:
    """Pet App GUI for registering pets"""
    
    def __init__(self, root):
        """Initialize the attributes and the main Tkinter application window"""
        self.root = root 
        self.root.title("Pet ID Profile Generator")
        self.root.geometry("740x450")
        self.root.configure(bg="#DBA674")
        
        self.image = None
        self.pet_object = Pet()
        
        self.input_frame()
        self.create_id_card_frame()
        
        LOGO_IMAGE_FILE = r"D:\PUP\First year - Second Semester\Object Oriented Programming\encapsulation_abstraction_oop_programs\pet_profile_tracker_management_system\pet_system_logo.webp"
        try:
            window_icon_img = Image.open(LOGO_IMAGE_FILE)
            self.window_icon_photo = ImageTk.PhotoImage(window_icon_img)
            self.root.iconphoto(True, self.window_icon_photo)
        except Exception:
            pass
        
    def input_frame(self):
        """Create an entry panel for the user to fill out"""
        input_frame = tk.LabelFrame(self.root,
            text = "Register Your Pet".center(60),
            font = ("Comic Sans MS", 12, "bold"),
            padx=15,
            pady= 15,
            bg= "#D8C8C8"
        )
        input_frame.place(x=20, y=20, width=320, height=400)
        
        tk.Label(input_frame, text = "Pet Name:", bg = "#FFFFFF").pack(anchor="w")
        self.pet_name_entry = tk.Entry(input_frame, font=("Comic Sans MS", 11))
        self.pet_name_entry.pack(fill="x", pady=(0,10))
        
        tk.Label(input_frame, text="Animal Type:", bg="#FFFFFF").pack(anchor="w")
        self.entry_type = tk.Entry(input_frame, font=("Comic Sans MS", 11))
        self.entry_type.pack(fill="x", pady=(0, 10))

        tk.Label(input_frame, text="Age (Years):", bg="#ffffff").pack(anchor="w")
        self.entry_age = tk.Entry(input_frame, font=("Comic Sans MS", 11))
        self.entry_age.pack(fill="x", pady=(0, 15))
        
        self.upload_button = tk.Button(
            input_frame, text = "🖼️ Upload Pet Photo (Optional)",
            command=self.upload_image, bg="#C5AF88", relief="flat"
        )
        self.upload_button.pack(fill="x", pady=(0, 20))
        
        generate_button = tk.Button(input_frame, text="Generate Pet ID Card",
            command= self.generate_id, bg="#C39696", fg="white",
            font=("Comic Sans MS", 11, "bold"), relief="flat",
        )
        generate_button.pack(fill="x", pady=(10, 0))
        
    def generate_id(self):
        """Generate the ID which updates the card display"""
        pet_name = self.pet_name_entry.get().strip()
        animal_type = self.entry_type.get().strip()
        pet_age = self.entry_age.get().strip()
            
        if not pet_name or not animal_type or not pet_age:
            messagebox.showerror("Error", "Please fill all fields!")
            return
            
        try:
            age = int(pet_age)
            if age < 0 :
                raise ValueError
        except ValueError:
            messagebox.showerror("Error!", "Age cannot be negative!")
            return

        self.pet_object.set_name(pet_name)
        self.pet_object.set_animal_type(animal_type)
        self.pet_object.set_age(age)
            
        self.pet_number_id.config(text=f"ID: {self.pet_object.get_id_number()}")
        self.pet_name.config(text=f"Name: {self.pet_object.get_name()}")
        self.pet_animal_type.config(text=f"Type: {self.pet_object.get_animal_type()}")
        self.pet_age.config(text=f"Age:  {self.pet_object.get_age()} yrs old")      
                
        default_image_file = r"D:\PUP\First year - Second Semester\Object Oriented Programming\encapsulation_abstraction_oop_programs\pet_profile_tracker_management_system\no_profile.png"
            
        if self.image:
            check_image = self.image
        else:
            check_image = default_image_file
            
        try:
            image = Image.open(check_image)
            image = image.resize((110, 130), Image.Resampling.LANCZOS)
            self.pet_photo = ImageTk.PhotoImage(image)
            self.photo_label.config(image=self.pet_photo, text="")
        except FileNotFoundError:
            self.photo_label.config(text="Image Not Found", font=("Comic Sans MS", 10))
        except Exception as error:
            messagebox.showwarning("Image Error!", "Failed to load the photo.")
        
    def upload_image(self):
        """Allows users to browse for an image of their pet's profile picture"""
        file_types = [("Image files", "*.jpg *.jpeg *.png *.bmp")]
        path = filedialog.askopenfilename(title="Select Photo", filetypes=file_types)
        
        if path:
            self.image = path
            self.upload_button.config(
                text="✅ Photo Attached", bg="#1CA23B", fg="#FFFFFF"
            )
        
    def create_id_card_frame(self):
        """The backbone and structure of the Card frame"""
        self.card_frame = tk.Frame(self.root, bg = "#FFFFFF", bd=2, relief="groove")
        self.card_frame.place(x=370, y=45, width=350, height=250)
            
        header = tk.Label(self.card_frame, text="OFFICIAL PET ID", bg="#9B0808", fg="#FFFFFF",
            font=("Comic Sans MS", 15, "bold"), pady=8)
        header.pack(fill="x")
            
        self.photo_label = tk.Label(self.card_frame, text="No Photo", bg="#e4e6eb", relief="solid", bd=1
        )
        self.photo_label.place(x=20, y=60, width=150, height=130)
            
        self.pet_number_id = tk.Label(self.card_frame, text="ID: PET-XXXX",
            font=("Comic Sans MS", 12, "bold"), bg="#bcc2c7", fg="#000000",
        )
        self.pet_number_id.place(x=180, y=65)   
            
        self.pet_name = tk.Label(self.card_frame, text="Name: --------",
            font=("Comic Sans MS", 12), bg="#bcc2c7", fg="#000000",
        )
        self.pet_name.place(x=180, y=100)

        self.pet_animal_type = tk.Label(
            self.card_frame, text="Type: --------",
            font=("Comic Sans MS", 12), bg="#bcc2c7", fg="#000000"
        )
        self.pet_animal_type.place(x=180, y=130)

        self.pet_age = tk.Label(self.card_frame, text="Age: --------",
            font=("Comic Sans MS", 12), bg="#bcc2c7", fg="#000000"
        )
        self.pet_age.place(x=180, y=160)

        footer = tk.Label(self.card_frame, text="Happy pets, well-trained",
            bg="#242526", fg="#b0b3b8", font=("Arial", 9, "italic"),
        )
        footer.pack(side="bottom", fill="x", pady=5)
            