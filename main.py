import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from tkinter import font as tkFont
import time

click_count= 0 
orginal_photos = []
watermark_path = ""
watermark_png = False
is_true = False
button_again_clicked = False
confirm = None
again_button = None
end_button = None
file_explorer = None
button = None
again_do = False
def browse():
   global click_count, orginal_photos, watermark_path, watermark_png
   if not is_true:           
      if click_count == 0:
         op_path = askopenfilename(parent=root, multiple=True,initialdir=r"/",
            title="Select Photo", filetypes=(("Photo files","*.jpg*; *.png*"),("All Files","*.*")))
         file_explorer['text'] = "Select watermark"
         for photo in op_path:
            orginal_photos.append(photo)
         click_count += 1
         file_explorer['text'] = "Select watermark"
         
      elif click_count == 1:
         watermark_path = askopenfilename(parent=root,initialdir=r"/",
            title="Select Watermark", filetypes=(("Photo files","*.jpg*; *.png*"),("All Files","*.*")))
         watermark_open = Image.open(watermark_path)
         if watermark_open.format == "PNG":
            watermark_png = True
            watermark_open = watermark_open.convert('RGB')
            watermark_open.save('watermark/watermark.jpg', 'JPEG') 
      
         choose()

   elif is_true:
      global confirm2, again_do
      question_menu.destroy()
      question_menu2.place(x=290, y= 50)
      confirm2=tk.Button(root, text="confirm", font =helv20,background='purple4', width=15,
      command=watermark_position) 
      confirm2.place(x=250, y=175)

           
def watermark_position():
   global button_again_clicked
   for photos in orginal_photos:
      end_button.place(x=250, y=280)
      org_photo = Image.open(f"{photos}")
      im = Image.open(f"watermark/watermark.jpg")
      if org_photo.format == "PNG":
         org_photo_edited = org_photo.convert('RGB')
         org_photo_edited.save('orginal.jpg')
         org_photo = org_photo_edited 
      width, height = org_photo.size
      width_water, height_water = im.size
      if value_inside2.get() == "left top corner":
         Image.Image.paste(org_photo, im, (width-width, height-height))
         org_photo.save('result/complete.jpg')


      elif value_inside2.get() == "right top corner":
         Image.Image.paste(org_photo, im, (width - width_water, width-width))
         org_photo.save('result/complete.jpg')
         
      elif value_inside2.get() == "center":
         Image.Image.paste(org_photo, im, ((width - width_water)//2, (height - height_water)//2))
         org_photo.save('result/complete.jpg')

      elif value_inside2.get() == "left down corner":
         Image.Image.paste(org_photo, im, (width-width, height - height_water))
         org_photo.save('result/complete.jpg')

      elif value_inside2.get() == "right down corner":
         Image.Image.paste(org_photo, im, (width - width_water, height - height_water))
         org_photo.save('result/complete.jpg')
   
      
  
      
   


   
def choose():
   global is_true, confirm
   file_explorer.destroy()
   button.destroy()
   question_menu.place(x=290, y= 50)
   confirm=tk.Button(root, text="confirm", font =helv20,background='purple4', width=15,
      command=change_size) 
   confirm.place(x=250, y=175)
   while is_true:
      confirmr=tk.Button(root, text="confirm", font =helv20,background='purple4', width=15,
      command=change_size) 


def change_size(): 
   global watermark_path, watermark_png, is_true
   if watermark_png:
      watermark = 'watermark/watermark.jpg'
      
   elif not watermark_png:
      watermark = watermark_path
     
   print("Selected Option: {}".format(value_inside.get())) 
   if value_inside.get() == "50x50":
      new_watermark = Image.open(watermark)
      new_watermark = new_watermark.resize((50, 50))
      new_watermark.save('watermark/watermark.jpg')
      is_true=True
      browse()

   elif value_inside.get() == "100x100":
      new_watermark = Image.open(watermark)
      new_watermark = new_watermark.resize((100, 100))
      new_watermark.save('watermark/watermark.jpg')
      is_true=True
      browse()


   elif value_inside.get() == "150x150":
      new_watermark = Image.open(watermark)
      new_watermark = new_watermark.resize((150, 150))
      new_watermark.save('watermark/watermark.jpg')
      is_true=True
      browse()

   else:
      new_watermark = Image.open(watermark)
      new_watermark = new_watermark.resize((50, 50))
      new_watermark.save('watermark/watermark.jpg')
      is_true=True
      browse()


root = tk.Tk()
root.title("Watermark app")
root.geometry("750x350")
root.config(background="black")
root.wm_attributes('-transparentcolor', '#ab23ff')
canvas = tk.Canvas(root, width = 30, height = 20)
helv36 = tkFont.Font(family="Helvetica",size=36,weight="bold")
helv20 = tkFont.Font(family="Helvetica",size=20,weight="bold")
bg = tk.PhotoImage(file=r"background3.png")
label1 = tk.Label( root, image = bg, text='Select photo', fg='white') 
label1.place(x = 0,y = 0)
options_list = ["50x50", "100x100", "150x150"] 
options_list2 = ["left top corner", "right top corner", "center", "left down corner", "right down corner"] 
value_inside = tk.StringVar(root) 
value_inside.set("Select size of Watermark") 
value_inside2 = tk.StringVar(root) 
value_inside2.set("Where past watermark") 
question_menu = tk.OptionMenu(root, value_inside, *options_list) 
question_menu2 = tk.OptionMenu(root, value_inside2, *options_list2) 
question_menu.configure(background="mediumpurple4", width=20, highlightthickness=0)
question_menu2.configure(background="mediumpurple4", width=20, highlightthickness=0)


canvas.create_text(20,20, text='',fill='darkblue', font='Helvetica')
file_explorer = tk.Label(root, text="Selec Photo",
   font=helv20,
   width=45,
   height=2, fg="white", bg='purple4')
button=tk.Button(root, text="File", font =helv20,background='purple4', width=15,
   command=browse)
end_button=tk.Button(root, text="End", font =helv20,background='darkorchid2', width=15,
   command=root.destroy)
file_explorer.place(x=0, y=10)
button.place(x=250, y=175)
canvas.place(x=20,y=20)

root.mainloop()