import tkinter as tk

root = tk.Tk()
root.geometry("800x500")
root.title("Face Recognition Attendance System")
root.mainloop()



# from tkinter import messagebox
# from PIL import Image, ImageTk

# class FaceRecognitionApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Face Recognition Attendance System")
#         self.root.geometry("800x500")

#         # Load and place background image
#         bg_image = Image.open(".\images\ocean.jpeg")  # Replace with your image path
#         bg_image = bg_image.resize((800, 500))
#         self.bg_photo = ImageTk.PhotoImage(bg_image)

#         bg_label = tk.Label(self.root, image=self.bg_photo)
#         bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#         # Title (on top of bg)
#         title = tk.Label(self.root, text="Welcome to Face Recognition Attendance System",
#                          font=("Helvetica", 20, "bold"), bg="white", fg="#2c3e50")
#         title.place(relx=0.5, y=40, anchor="center")

#         # Buttons (on top of bg)
#         btn1 = tk.Button(self.root, text="Start Face Recognition", font=("Helvetica", 14), width=25,
#                          bg="#2980b9", fg="white", command=self.start_face_recognition)
#         btn1.place(relx=0.5, y=150, anchor="center")

#         btn2 = tk.Button(self.root, text="View Attendance", font=("Helvetica", 14), width=25,
#                          bg="#27ae60", fg="white", command=self.view_attendance)
#         btn2.place(relx=0.5, y=210, anchor="center")

#         btn3 = tk.Button(self.root, text="Exit", font=("Helvetica", 14), width=25,
#                          bg="#c0392b", fg="white", command=self.root.quit)
#         btn3.place(relx=0.5, y=270, anchor="center")

#     def start_face_recognition(self):
#         messagebox.showinfo("Face Recognition", "This would start the face recognition function.")

#     def view_attendance(self):
#         messagebox.showinfo("Attendance", "This would display attendance records.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = FaceRecognitionApp(root)
#     root.mainloop()
