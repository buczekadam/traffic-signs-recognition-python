import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
from tensorflow.keras.models import load_model

model = load_model("C:/Users/Adam/PycharmProjects/traffic-signs-recognition-python/traffic_signs_model.h5")

classes = {0: 'Speed limit (20km/h)',
           1: 'Speed limit (30km/h)',
           2: 'Speed limit (50km/h)',
           3: 'Speed limit (60km/h)',
           4: 'Speed limit (70km/h)',
           5: 'Speed limit (80km/h)',
           6: 'End of speed limit (80km/h)',
           7: 'Speed limit (100km/h)',
           8: 'Speed limit (120km/h)',
           9: 'No passing',
           10: 'No passing veh over 3.5 tons',
           11: 'Right-of-way at intersection',
           12: 'Priority road',
           13: 'Yield',
           14: 'Stop',
           15: 'No vehicles',
           16: 'Veh > 3.5 tons prohibited',
           17: 'No entry',
           18: 'General caution',
           19: 'Dangerous curve left',
           20: 'Dangerous curve right',
           21: 'Double curve',
           22: 'Bumpy road',
           23: 'Slippery road',
           24: 'Road narrows on the right',
           25: 'Road work',
           26: 'Traffic signals',
           27: 'Pedestrians',
           28: 'Children crossing',
           29: 'Bicycles crossing',
           30: 'Beware of ice/snow',
           31: 'Wild animals crossing',
           32: 'End speed + passing limits',
           33: 'Turn right ahead',
           34: 'Turn left ahead',
           35: 'Ahead only',
           36: 'Go straight or right',
           37: 'Go straight or left',
           38: 'Keep right',
           39: 'Keep left',
           40: 'Roundabout mandatory',
           41: 'End of no passing',
           42: 'End no passing veh > 3.5 tons'}

top = tk.Tk()
top.geometry('640x480')
top.title('Traffic sign recognition')
top.configure(background='#3949AB')
label = Label(top, background='#3949AB', font=('arial', 15, 'bold'))
sign_image = Label(top)


def recognize_sign(file_path):
    image = Image.open(file_path)
    image = image.resize((30, 30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    sign = classes[model.predict_classes([image])[0]]
    label.configure(foreground='#011638', text=sign)


def show_recognize_button(file_path):
    recognize_button = Button(top, text="Recognize", command=lambda: recognize_sign(file_path), padx=10, pady=5)
    recognize_button.configure(background='#C2185B', foreground='#000000', font=('arial', 10, 'bold'))
    recognize_button.place(relx=0.79, rely=0.46)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.pack(side=BOTTOM, expand=True)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_recognize_button(file_path)
    except:
        pass


upload_button = Button(top, text="Upload", command=upload_image, padx=10, pady=5)
upload_button.configure(background='#C2185B', foreground='#000000', font=('arial', 10, 'bold'))
upload_button.pack(side=BOTTOM, pady=50)

label.pack(side=BOTTOM, expand=True)
title = Label(top, text="Recognize traffic sign", pady=20, font=('arial', 20, 'bold'))
title.configure(background='#3949AB', foreground='#000000')
title.pack()
top.mainloop()
