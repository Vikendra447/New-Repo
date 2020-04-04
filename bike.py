from Tkinter import*
root=Tk()
root.geometry("700x500")
root.config(bg="#2a757a")
Label(root,text="Name:PRAKHAR SHRIVASTAVA ").pack()
Label(root,text="ENROLL NO:151348 ").pack()
def a():
 def pulsar():
      root2=Tk()
      root2.geometry("700x500")
      root2.config(bg="#2a757a")
      w=Label(root2,text="Name:PULSAR 200RS\nMileage:35-40kmpl\nNo.of Gears:6\nTop Speed:140.8kmph\nFuel tank Capacity:13 litres\n Showroom Price:Rs1.35 lakhs",font="Times 20 bold",fg="white",bg="#20182d")
      w.pack(fill="both",side="top",ipady=1)
 def avenger():
      root2=Tk()
      root2.geometry("700x500")
      root2.config(bg="#2a757a")
      w=Label(root2,text="Name:AVENGER STREET 150\nMileage:45-50kmpl\nNo.of Gears:5\nTop Speed:125kmph\nfuel tank Capacity:10 litres\n Showroom Price:Rs95000",font="Times 20 bold",fg="white",bg="#20182d")
      w.pack(fill="both",side="top",ipady=1)
 def v():
      root2=Tk()
      root2.geometry("700x500")
      root2.config(bg="#2a757a")
      w=Label(root2,text="Name:BAJAJ V\nMileage:45-50kmpl\nNo.of Gears:4\nTop Speed:110kmph\nfuel tank Capacity:11 litres\n Showroom Price:Rs80000",font="Times 20 bold",fg="white",bg="#20182d")
      w.pack(fill="both",side="top",ipady=1)
 def platina():
      root2=Tk()
      root2.geometry("700x500")
      root2.config(bg="#2a757a")
      w=Label(root2,text="Name:BAJAJ PLATINA\nMileage:90kmpl\nNo.of Gears:4\nTop Speed:90kmph\nfuel tank Capacity:11 litres\n Showroom Price:Rs60000",font="Times 20 bold",fg="white",bg="#20182d")
      w.pack(fill="both",side="top",ipady=1)
      
 def bajaj():
      
      root1=Tk()
      
     
      root1.geometry("700x500")
      root1.config(bg="#2a757a")
      o=Label(root1,text="BAJAJ BIKE MODELS:",font="Times 20 bold",fg="white",bg="#20182d")
      o.grid(row=0,column=1,sticky="W")
      b5=Button(root1,text="PULSAR 200RS",font="Times 10 bold",command=pulsar)
      b5.grid(row=1,column=0,ipadx=35,ipady=10,sticky="w",padx=5)
      b6=Button(root1,text="AVENGER 150 STREET",font="Times 10 bold",command=avenger)
      b6.grid(row=2,column=0,ipadx=14,ipady=10,sticky="w",padx=5)

      b7=Button(root1,text="BAJAJ V",font="Times 10 bold",command=v)
      b7.grid(row=3,column=0,ipadx=54,ipady=10,sticky="w",padx=5)

      b8=Button(root1,text="BAJAJ PLATINA",font="Times 10 bold",command=platina)
      b8.grid(row=4,column=0,ipadx=31,ipady=10,sticky="w",padx=5)
      
      root1.mainloop()
 def karizma():
      root2=Tk()
      root2.geometry("700x500")
      root2.config(bg="#2a757a")
      w=Label(root2,text="Name:KARIZMA ZMR\nMileage:30-35kmpl\nNo.of Gears:6\nTop Speed:150kmph\nfuel tank Capacity:15 litres\n Showroom Price:Rs1.25lakhs",font="Times 20 bold",fg="white",bg="#20182d")
      w.pack(fill="both",side="top",ipady=1)
 def hunk():
      root2=Tk()
      root2.geometry("700x500")
      root2.config(bg="#2a757a")
      w=Label(root2,text="Name:HERO HUNK\nMileage:40-45kmpl\nNo.of Gears:5\nTop Speed:120kmph\nfuel tank Capacity:11 litres\n Showroom Price:Rs92000",font="Times 20 bold",fg="white",bg="#20182d")
      w.pack(fill="both",side="top",ipady=1)
 def ismart():
      root2=Tk()
      root2.geometry("700x500")
      root2.config(bg="#2a757a")
      w=Label(root2,text="Name:HERO SPLENDOR iSMART\nMileage:60-70kmpl\nNo.of Gears:4\nTop Speed:100kmph\nfuel tank Capacity:10 litres\n Showroom Price:Rs68000",font="Times 20 bold",fg="white",bg="#20182d")
      w.pack(fill="both",side="top",ipady=1)
 def deluxe():
      root2=Tk()
      root2.geometry("700x500")
      root2.config(bg="#2a757a")
      w=Label(root2,text="Name:HERO HF-DELUXE\nMileage:60kmpl\nNo.of Gears:4\nTop Speed:100kmph\nfuel tank Capacity:12 litres\n Showroom Price:Rs63000",font="Times 20 bold",fg="white",bg="#20182d")
      w.pack(fill="both",side="top",ipady=1)      
 def hero():
      
      root1=Tk()
      root1.geometry("700x500")
      root1.config(bg="#2a757a")
      o=Label(root1,text="HERO BIKE MODELS:",font="Times 20 bold",fg="white",bg="#20182d")
      o.grid(row=0,column=1,sticky="W")
      b5=Button(root1,text="KARIZMA ZMR",font="Times 10 bold",command=karizma)
      b5.grid(row=1,column=0,ipadx=34,ipady=10,sticky="w",padx=5)
      b6=Button(root1,text="HERO HUNK",font="Times 10 bold",command=hunk)
      b6.grid(row=2,column=0,ipadx=42.5,ipady=10,sticky="w",padx=5)

      b7=Button(root1,text="HERO SPLENDOR iSMART",font="Times 10 bold",command=ismart)
      b7.grid(row=3,column=0,ipadx=1,ipady=10,sticky="w",padx=5)

      b8=Button(root1,text="HERO HF-DELUXE",font="Times 10 bold",command=deluxe)
      b8.grid(row=4,column=0,ipadx=27,ipady=10,sticky="w",padx=5)
      
      root1.mainloop()
 def shine():
      root2=Tk()
      root2.geometry("700x500")
      root2.config(bg="#2a757a")
      w=Label(root2,text="Name:CB-SHINE\nMileage:50kmpl\nNo.of Gears:5\nTop Speed:110kmph\nfuel tank Capacity:11 litres\n Showroom Price:Rs75000",font="Times 20 bold",fg="white",bg="#20182d")
      w.pack(fill="both",side="top",ipady=1)
 def cbr():
      root2=Tk()
      root2.geometry("700x500")
      root2.config(bg="#2a757a")
      w=Label(root2,text="Name:CBR-250\nMileage:25kmpl\nNo.of Gears:7\nTop Speed:160kmph\nfuel tank Capacity:16 litres\n Showroom Price:Rs2.25lakhs",font="Times 20 bold",fg="white",bg="#20182d")
      w.pack(fill="both",side="top",ipady=1)
 def dazzler():
      root2=Tk()
      root2.geometry("700x500")
      root2.config(bg="#2a757a")
      w=Label(root2,text="Name:DAZZLER\nMileage:40kmpl\nNo.of Gears:5\nTop Speed:110kmph\nfuel tank Capacity:12 litres\n Showroom Price:Rs85000",font="Times 20 bold",fg="white",bg="#20182d")
      w.pack(fill="both",side="top",ipady=1)
 def livo():
      root2=Tk()
      root2.geometry("700x500")
      root2.config(bg="#2a757a")
      w=Label(root2,text="Name:HERO HONDA LIVO\nMileage:60kmpl\nNo.of Gears:4\nTop Speed:110kmph\nfuel tank Capacity:11 litres\n Showroom Price:Rs69000",font="Times 20 bold",fg="white",bg="#20182d")
      w.pack(fill="both",side="top",ipady=1)            

 def honda():
      
      root1=Tk()
      root1.geometry("700x500")
      root1.config(bg="#2a757a")
      o=Label(root1,text="HONDA BIKE MODELS:",font="Times 20 bold",fg="white",bg="#20182d")
      o.grid(row=0,column=1,sticky="W")
      b5=Button(root1,text="CB SHINE",font="Times 10 bold",command=shine)
      b5.grid(row=1,column=0,ipadx=35,ipady=10,sticky="w",padx=5)
      b6=Button(root1,text="CBR-250",font="Times 10 bold",command=cbr)
      b6.grid(row=2,column=0,ipadx=38,ipady=10,sticky="w",padx=5)

      b7=Button(root1,text="DAZZLER",font="Times 10 bold",command=dazzler)
      b7.grid(row=3,column=0,ipadx=35,ipady=10,sticky="w",padx=5)

      b8=Button(root1,text="HONDA LIVO",font="Times 10 bold",command=livo)
      b8.grid(row=4,column=0,ipadx=23.5,ipady=10,sticky="w",padx=5)
      
      root1.mainloop()

      
 def bullet():
      root2=Tk()
      root2.geometry("700x500")
      root2.config(bg="#2a757a")
      w=Label(root2,text="Name:BULLET-350\nMileage:35kmpl\nNo.of Gears:6\nTop Speed:130kmph\nfuel tank Capacity:18 litres\n Showroom Price:Rs1.35lakhs",font="Times 20 bold",fg="white",bg="#20182d")
      w.pack(fill="both",side="top",ipady=1)
 def thunderbird():
      root2=Tk()
      root2.geometry("700x500")
      root2.config(bg="#2a757a")
      w=Label(root2,text="Name:THUNDERBIRD-350\nMileage:30kmpl\nNo.of Gears:7\nTop Speed:130kmph\nfuel tank Capacity:16 litres\n Showroom Price:Rs1.45lakhs",font="Times 20 bold",fg="white",bg="#20182d")
      w.pack(fill="both",side="top",ipady=1)
 def himalayan():
      root2=Tk()
      root2.geometry("700x500")
      root2.config(bg="#2a757a")
      w=Label(root2,text="Name:HIMALAYAN\nMileage:20kmpl\nNo.of Gears:6\nTop Speed:150kmph\nfuel tank Capacity:14 litres\n Showroom Price:Rs2.2 lakhs",font="Times 20 bold",fg="white",bg="#20182d")
      w.pack(fill="both",side="top",ipady=1)
 def continental():
      root2=Tk()
      root2.geometry("700x500")
      root2.config(bg="#2a757a")
      w=Label(root2,text="Name:CONTINENTAL\nMileage:20kmpl\nNo.of Gears:6\nTop Speed:150kmph\nfuel tank Capacity:12 litres\n Showroom Price:Rs2.20lakhs",font="Times 20 bold",fg="white",bg="#20182d")
      w.pack(fill="both",side="top",ipady=1)            
      
 def RE():
      
      root1=Tk()
      root1.geometry("700x500")
      root1.config(bg="#2a757a")
      o=Label(root1,text="ROYAL ENFIELD BIKE MODELS:",font="Times 20 bold",fg="white",bg="#26182d")
      o.grid(row=0,column=1,sticky="W")
      b5=Button(root1,text="BULLET-350",font="Times 10 bold",command=bullet)
      b5.grid(row=1,column=0,ipadx=41,ipady=10,sticky="w",padx=5)
      b6=Button(root1,text="THUNDERBIRD-350",font="Times 10 bold",command=thunderbird)
      b6.grid(row=2,column=0,ipadx=20,ipady=10,sticky="w",padx=5)

      b7=Button(root1,text="HIMALAYAN",font="Times 10 bold",command=himalayan)
      b7.grid(row=3,column=0,ipadx=40,ipady=10,sticky="w",padx=5)

      b8=Button(root1,text="CONTINENTAL",font="Times 10 bold",command=continental)
      b8.grid(row=4,column=0,ipadx=33,ipady=10,sticky="w",padx=5)
      
      root1.mainloop()
            

            

      
            
     
     
 l=Label(root,text="BIKE STORE",font="Times 20 bold",fg="white",bg="#20182d")
 l.pack(fill="both",side="top",ipady=1)
 label=Label(root,bg="#2a757a")
 label.pack(fill="both",expand="yes")
 l2=Label(label,bg="#2a757a")
 l2.grid(row=2,column=0)
 b1=Button(l2,text="Bajaj",font="Times 18 bold",command=bajaj)
 b1.grid(row=2,column=0,ipadx=25,ipady=10,sticky="w",padx=15)
 b2=Button(l2,text="Hero",font="Times 18 bold",command=hero)
 b2.grid(row=2,column=1,ipadx=25,ipady=10,sticky="w",padx=15)
 b3=Button(l2,text="Honda",font="Times 18 bold",command=honda)
 b3.grid(row=2,column=2,ipadx=25,ipady=10,sticky="w",padx=15)

 b4=Button(l2,text="Royal Enflied",font="Times 18 bold",command=RE)
 b4.grid(row=2,column=3,ipadx=1,ipady=10,sticky="w",padx=15)

Button(root,text="CLICK ON BUTTON TO START THE PROJECT",command=a).pack()
root.mainloop()
