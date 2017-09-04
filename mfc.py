from tkinter import font 
from time import sleep
from tkinter import *

root = Tk()

root.title("MFC - Multiple Files Creator")
root.resizable(height=False, width=False)
root.geometry("627x400")

#Fonts
arial11 = font.Font(family="arial", size=11)
arial13 = font.Font(family="arial", size=13)


class FileAttribute:
    
    row_num = 0

    def __init__(self, description_text, general_height):
        #Text that shows what kind of information the user should input
        self.attr_info_text = Label(root, height=general_height, width=30, bg="#A7A7A7", anchor="w", font=arial11, text=description_text)
        self.attr_info_text.grid(row=FileAttribute.row_num, column=0, pady=1)
        
        #Text input
        self.attr_input = Text(root, height=general_height,font=arial11, width=43)
        self.attr_input.grid(row=FileAttribute.row_num, column=1)

        FileAttribute.row_num += 1


#Instances/Objects
obj_name = FileAttribute("Name for the files", 2)
obj_content = FileAttribute("Text that you want in all the files", 7)
obj_filetype = FileAttribute("Filetype(leave it blank for .txt)", 2)
obj_amount = FileAttribute("How many files do you want to create?", 2)


#Gather all the attributes/variables(name, content, filetype, amount) and create the files
def create_files():
    
    #Making the variables more accessable
    name = obj_name.attr_input.get("1.0", "end-1c")
    content = obj_content.attr_input.get("1.0", "end-1c")
    filetype = obj_filetype.attr_input.get("1.0", "end-1c")
    amount = int(obj_amount.attr_input.get("1.0", "end-1c"))
   
    #If filetype is empty reassign '.txt' to it
    if not filetype or filetype == "txt":
        filetype = ".txt"
    elif filetype != ".":
        filetype = "." + filetype
    
    for num in range(amount):
        target_file = open("{}{}{}".format(name, num, filetype), "w")
        target_file.write(content)


confirm_button = Button(root, height=3, width=40, bg="#A7A7A7", relief="flat", font=arial13, text="Create", command=create_files)
confirm_button.grid(row=FileAttribute.row_num + 1 , columnspan=2, padx=100, pady=40)

root.mainloop()
