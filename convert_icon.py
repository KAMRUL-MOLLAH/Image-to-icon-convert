from PIL import Image
import os
from tkinter import Tk, filedialog, Label, Button, StringVar, Frame, ttk

def convert_image_to_icon(input_path, output_path, icon_size=(256, 256)):
    """
    Convert an image to .ico format with specified size.
    """
    try:
        with Image.open(input_path) as img:
            img.save(output_path, format="ICO", sizes=[icon_size])
            return f"Icon successfully saved at {output_path}"
    except Exception as e:
        return f"Error: {e}"

def select_image():
    input_path = filedialog.askopenfilename(
        title="Select Image File",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if input_path:
        input_var.set(input_path)

def convert_image():
    input_path = input_var.get()
    if not input_path:
        output_var.set("Please select an image file first.")
        return

    # Get the selected icon size
    size_str = size_var.get()
    icon_size = tuple(map(int, size_str.strip("()").split(", ")))

    output_dir = "icons"
    os.makedirs(output_dir, exist_ok=True)
    output_filename = os.path.splitext(os.path.basename(input_path))[0] + ".ico"
    output_path = os.path.join(output_dir, output_filename)

    result = convert_image_to_icon(input_path, output_path, icon_size)
    output_var.set(result)

# Set up the main application window
root = Tk()
root.title("Image to Icon Converter")
root.geometry("400x300")

# Header
header_label = Label(root, text="KAMRUL MOLLAH", font=("Arial", 16))
header_label.pack(pady=10)

# Define StringVars for input and output messages
input_var = StringVar()
output_var = StringVar()
size_var = StringVar(value="(256, 256)")  # Default size

# Create a frame for better layout
frame = Frame(root)
frame.pack(pady=20)

# Input label and button
Label(frame, text="Selected Image:").pack()
Label(frame, textvariable=input_var, wraplength=300).pack()
Button(frame, text="Select Image", command=select_image).pack(pady=5)

# Icon size selection
Label(frame, text="Select Icon Size:").pack(pady=5)
size_options = ["(16, 16)", "(32, 32)", "(64, 64)", "(128, 128)", "(256, 256)"]
size_combobox = ttk.Combobox(frame, textvariable=size_var, values=size_options, state="readonly")
size_combobox.pack()

# Convert button
Button(frame, text="Convert to Icon", command=convert_image).pack(pady=5)

# Output message
Label(frame, textvariable=output_var).pack(pady=10)

# Footer
footer_label = Label(root, text="Website: kamrulmollah.com", font=("Arial", 15))
footer_label.pack(side="bottom", pady=10)

# Start the Tkinter event loop
root.mainloop()
