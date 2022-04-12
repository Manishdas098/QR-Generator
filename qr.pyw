from tkinter import *
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage
class Qr_genrator:
    def __init__(self,root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QR-genrator | Created with ❤️ by Manish")
        self.root.resizable(False, False)

        title = Label(self.root,text="Qr Generator" ,font=("times new roman",40),fg="white"  ,anchor="w", bg="#053246"  ).place(x = 0, y =0 , relwidth = 1)
        self.root =


#====================================================employ detail frame =======================================================================================================#
#====================================================variable===========================================================================================
        self.var_emp_url = StringVar()
        self.var_name = StringVar()
   
     
     
     
        emp_FRAME =Frame(self.root, bd =2 , relief = RIDGE, bg="white")
        emp_FRAME.place(x = 50, y =100,width =500, height=380)
        
        emp_title = Label(emp_FRAME,text="details" ,font=("goudy old style",20),fg="white" , bg="#053256"  ).place(x = 0, y =0 , relwidth = 1)

#=====================================================employ field ==============================================================================================================#
        lbl_id = Label(emp_FRAME,text="Url" ,font=("times new roman",15 , "bold"), bg="white"  ).place(x = 20, y =60 )

        lbl_name = Label(emp_FRAME,text="Name" ,font=("times new roman",15 , "bold"), bg="white"  ).place(x = 20, y =100 )

       
       
#=====================================================entry field ================================================================================================================#
        text_id = Entry(emp_FRAME, font=("times new roman",15 , ) ,textvariable=self.var_emp_url, bg="lightyellow").place(x = 200, y =60 )

        text_name = Entry(emp_FRAME,font=("times new roman",15 , ), textvariable=self.var_name,bg="lightyellow").place(x = 200, y =100 )

        
       
#======================================================button =====================================================================================================================#


        btn_gen = Button(emp_FRAME,text="Generate" ,command=self.genrate, font=("times new roman",18 , "bold"), bg="#2196f3", fg="white").place(x = 80, y =250, width =180 , height =30)
        
        btn_clr = Button(emp_FRAME,text="Clear" ,command=self.clear, font=("times new roman",18 , "bold"), bg="#2196f3", fg="white").place(x = 270, y =250, width =140 , height =30)


#=======================================================message======================================================================================================================#

        self.msg = ""
        self.lbl_message =Label(emp_FRAME,text=self.msg,font=("times new roman",15 ),fg="green", bg="white"  )
        self.lbl_message.place(x = 0, y =310, relwidth=1 )



#====================================================QR detail frame =======================================================================================================#

        Qr_FRAME =Frame(self.root, bd =2 , relief = RIDGE, bg="white")
        Qr_FRAME.place(x = 600, y =100,width =270, height=380)
        
        Qr_title = Label(Qr_FRAME,text="QR details" ,font=("goudy old style",20),fg="white" , bg="#053256"  ).place(x = 0, y =0 , relwidth = 1)

        
        self.Qr_code = Label(Qr_FRAME,text="No QR Avaliable",bd=0, relief=RIDGE, font=("times new roman" , 15 , "bold"), bg="#3f51b5" , fg="white")
        self.Qr_code.place(x = 35, y =100 ,width = 200 , height= 200 )
   
    def clear(self):
        self.var_emp_url.set("")
        self.var_name.set("")
        self.Qr_code.config(image="" , bd=0)
 
        self.msg =  ""
        self.lbl_message.config(text= self.msg , fg= "green") 
#=======================================================================================gentation ============================================================================================#
    def genrate(self):
        if self.var_emp_url.get() == "" or self.var_name.get() == "":
            self.msg = "All field Require!!!"
            self.lbl_message.config(text= self.msg , fg= "red")
         
        else: 


            qr_data =(f"{self.var_emp_url.get()}")
            qr_code = qrcode.make(qr_data)
            # print(qr_code)
            qr_code = resizeimage.resize_cover(qr_code,[200,200])
            qr_code.save(str(self.var_name.get())+'.png')
#==========================================================================updating variable =======================================================================================#        
           
            self.im = ImageTk.PhotoImage(qr_code)
            self.Qr_code.config(image=self.im,bd=2)
           
           
           
            self.msg =  "QR Generated Successfully!!!" 
            self.lbl_message.config(text= self.msg , fg= "green")       

root = Tk()
obj = Qr_genrator(root)
root.mainloop()
