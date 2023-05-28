import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import *
from tkinter import messagebox, filedialog
import tkinter as tk
import datetime
import csv

iconpath =''

Program = ttk.Window(themename='journal')
Program.title('SellerApp')
Program.geometry('600x500')

# Frame1
Box1 = ttk.LabelFrame(Program, text=' Seller Dashboard ',bootstyle="success")
Box1.place(x=60, y=190, width=490, height=230)

style = ttk.Style()
style.configure('Treeview.Heading', font=('yu gothic ui', 9, 'bold'))

Tapbar = ttk.Treeview(Program,bootstyle='success')
Tapbar.place(x=70, y=210, width=470, height=200)

scrollbarx1 = ttk.Scrollbar(Program, orient=HORIZONTAL,bootstyle="success-round")
scrollbary1 = ttk.Scrollbar(Program, orient=VERTICAL,bootstyle="success-round")
Tapbar.configure(yscrollcommand=scrollbary1.set, xscrollcommand=scrollbarx1.set)
Tapbar.configure(selectmode='extended')

scrollbary1.configure(command=Tapbar.yview)
scrollbarx1.configure(command=Tapbar.xview)

scrollbary1.place(x=517, y=234, width=22, height=175)
scrollbarx1.place(x=72, y=387, width=445, height=22)

Tapbar.configure(
    columns=(
        'Name',
        'price',
        'category',
        'quantity',
        'type',
        'size',
        'Time',
        'seller'
    )
)

Tapbar.heading('#0', text='No', anchor=CENTER)
Tapbar.heading('Name', text='Name', anchor=CENTER)
Tapbar.heading('price', text='price', anchor=W)
Tapbar.heading('category', text='category', anchor=W)
Tapbar.heading('quantity', text='quantity', anchor=W)
Tapbar.heading('type', text='type', anchor=W)
Tapbar.heading('size', text='size', anchor=W)
Tapbar.heading('Time', text='Time', anchor=W)
Tapbar.heading('seller', text='seller', anchor=W)

Tapbar.column('#0', stretch=NO, minwidth=0, width=0)
Tapbar.column('Name', stretch=NO, minwidth=0, width=100)
Tapbar.column('price', stretch=NO, minwidth=0, width=70)
Tapbar.column('category', stretch=NO, minwidth=0, width=70)
Tapbar.column('quantity', stretch=NO, minwidth=0, width=70)
Tapbar.column('type', stretch=NO, minwidth=0, width=70)
Tapbar.column('size', stretch=NO, minwidth=0, width=50)
Tapbar.column('Time', stretch=NO, minwidth=0, width=150)
Tapbar.column('seller', stretch=NO, minwidth=0, width=90)

products = []





product_name_label = ttk.Label(Program, text="Product Name:")
product_name_label.grid(row=1, column=0, padx=5,pady=2)

product_name_entry = ttk.Entry(Program,bootstyle="success")
product_name_entry.grid(row=1, column=1, padx=5,pady=2)

product_price_label = tk.Label(Program, text="Product Price:")
product_price_label.grid(row=1, column=2, padx=5,pady=2)

product_price_entry = ttk.Entry(Program,bootstyle="success")
product_price_entry.grid(row=1, column=3, padx=5,pady=2)



category = {'เสื้อ': ['แขนยาว','แขนสั้น','เสื้อกล้าม'],
    'กางเกง': ['ขายาว','ขาสั้น','ยีนส์'],
    'กระโปรง':['ยาว','สั้น']}

def getUpdateData(event):
    AccountCombo['values'] = category[CategoryCombo.get()]
Label(text = 'Category:').grid(row = 2,column = 0,padx = 10,pady=2)
Label(text = 'Type:').grid(row = 2,column = 2,padx = 10,pady=2)
AccountCombo = ttk.Combobox( width = 17,bootstyle="success")
AccountCombo.grid(row = 2,column = 3,padx = 10,pady=2)

CategoryCombo = ttk.Combobox(width = 17,  values = list(category.keys()),bootstyle="success")
CategoryCombo.bind('<<ComboboxSelected>>', getUpdateData)
CategoryCombo.grid(row = 2,column = 1,padx = 10,pady=2)



product_quantity_label = tk.Label(Program, text="Quantity:")
product_quantity_label.grid(row=3, column=2, padx=5,pady=2)

product_quantity_entry = ttk.Entry(Program,bootstyle="success")
product_quantity_entry.grid(row=3, column=3, padx=5,pady=2)
# Adding combobox drop down list


size = tk.StringVar()
size_box = tk.Label(Program, text="Size:")
size_box.grid(row=3, column=0, padx=5,pady=2)
size_box = ttk.Combobox(Program, width = 17, 
                            textvariable = size,bootstyle="success")
size_box['values'] = (' S', 
                    ' M',
                    ' L',
                    ' XL',
                    ' XXL',
                    ' XXXL'      
                         )
size_box.grid(row=3, column=1, padx=5,pady=2)


seller_box = tk.Label(Program, text="Seller Name:")
seller_box.grid(row=8, column=0, padx=5, pady=10)
seller = tk.StringVar()
seller_box = ttk.Combobox(Program, width = 17, 
                            textvariable = seller,bootstyle="success")


# Adding combobox drop down list
seller_box['values'] = (' ณัชพล พลแหลม', 
                          ' ขยัน ขันแข็ง',
                          
                         )
  
seller_box.grid(row=8, column=1, padx=5,pady=10)


def add_product():
    time = datetime.datetime.now()
   
    product_name = product_name_entry.get()
    product_price = product_price_entry.get()
    category = CategoryCombo.get()
    product_type = AccountCombo.get()
    size = size_box.get()
    date = time.strftime('%c')
    seller_name = seller_box.get()
    quantity = product_quantity_entry.get()
    
    product = {
        'product_name': product_name,
        'product_price': product_price,
        'category': category,
        'type': product_type,
        'quantity': quantity,
        'size': size,
        'date': date,
        'seller_name': seller_name
    }
    
    products.append(product)
   
    
    # Add the product to the Treeview
    Tapbar.insert('', 'end', text=product_name, values=(

        product_name,
        product_price,
        category,
        quantity,  # quantity (empty for now)
        product_type,
        size,
        date,
        seller_name
    ))
    
    # Clear the entry fields
    product_name_entry.delete(0, 'end')
    product_price_entry.delete(0, 'end')
    seller_box.delete(0,'end')
    AccountCombo.delete(0, 'end')
    size_box.delete(0,'end')
    CategoryCombo.delete(0,'end')
    product_quantity_entry.delete(0,'end')
    

  

def remove_product():
    selected_items = Tapbar.selection()
    for item in selected_items:
        product_name = Tapbar.item(item, 'text')
        for product in products:
            if product['product_name'] == product_name:
                products.remove(product)
                Tapbar.delete(item)
                break

    # Remove the product from the CSV file
    with open('sold_products.csv', 'r', newline='', encoding='utf-8') as file:
        rows = list(csv.reader(file))

    new_rows = []
    for row in rows:
        if row[0] != product_name:
            new_rows.append(row)

    with open('sold_products.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(new_rows)


remove_button = ttk.Button(Program,bootstyle="success",text="Remove Product", command=remove_product)
remove_button.place(x=240,y=450)
def sell_product():
    time = datetime.datetime.now()
   
    product_name = product_name_entry.get()
    product_price = product_price_entry.get()
    category = CategoryCombo.get()
    product_type = AccountCombo.get()
    size = size_box.get()
    date = time.strftime('%c')
    seller_name = seller_box.get()
    quantity = product_quantity_entry.get()
    
    product = {
        'product_name': product_name,
        'product_price': product_price,
        'category': category,
        'type': product_type,
        'quantity': quantity,
        'size': size,
        'date': date,
        'seller_name': seller_name
    }
    
    products.append(product)
   
    
    # Add the product to the Treeview
    Tapbar.insert('', 'end', text=product_name, values=(

        product_name,
        product_price,
        category,
        quantity,  # quantity (empty for now)
        product_type,
        size,
        date,
        seller_name
    ))
    
    # Clear the entry fields
    product_name_entry.delete(0, 'end')
    product_price_entry.delete(0, 'end')
    seller_box.delete(0,'end')
    AccountCombo.delete(0, 'end')
    size_box.delete(0,'end')
    CategoryCombo.delete(0,'end')
    product_quantity_entry.delete(0,'end')
    


    print("Sold Product:")
    print("Product Name:", product['product_name'])
    print("Product Price:", product['product_price'])
    print("Category:", product['category'])
    print("quantity:", product['quantity'])
    print("Type:", product['type'])
    print("Size:", product['size'])
    print("Date:", product['date'])
    print("Seller Name:", product['seller_name'])
    print()
                
                # Save the sold product's data to a CSV file
    with open('sold_products.csv', mode='a', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
                product['product_name'],
                product['product_price'],
                product['category'],
                product['type'],
                product['quantity'],
                product['size'],
                product['date'],
                product['seller_name']
                    ])
                
                # Remove the sold product from the list and Treeview
               
              

sell_button = ttk.Button(Program, bootstyle="success",text="Add/Sell Product", command=sell_product)
sell_button.place(x=75,y=450)




def generate_sales_summary():
    total_sales = len(products)
    total_revenue = sum(float(product['product_price']) for product in products)
    print(total_revenue)
    average_price = total_revenue / total_sales

    messagebox.showinfo('Sales Summary',
                        f'Total Sales: {total_sales}\n'
                        f'Total Revenue: {total_revenue}\n'
                        f'Average Price: {average_price:.2f}')
sales_summary_button = ttk.Button(Program, bootstyle="success", text="Generate Sales Summary",
                                 command=generate_sales_summary)
sales_summary_button.place(x=400, y=450)

Program.mainloop()
