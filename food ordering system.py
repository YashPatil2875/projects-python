from tkinter import *
import random
import time
from tkinter import filedialog, messagebox


def reset():
    textreceipt.delete(0.1, END)
    e_roti.set('0')
    e_paneerchilly.set('0')
    e_makhanwala.set('0')
    e_kolhapuri.set('0')
    e_malaikofta.set('0')
    e_kurma.set('0')
    e_butter.set('0')
    e_rice.set('0')
    e_dalmakhani.set('0')
    e_dalfry.set('0')
    e_paratha.set('0')
    e_chickenchilly.set('0')
    e_tandoori.set('0')
    e_biryani.set('0')
    e_tikka.set('0')
    e_tangdikebab.set('0')
    e_eggbhurji.set('0')
    e_fishfry.set('0')
    e_makhmali.set('0')
    e_afghanipulao.set('0')
    e_tea.set('0')
    e_coffee.set('0')
    e_fruitcocktail.set('0')
    e_lemonade.set('0')
    e_gingerale.set('0')
    e_cocacola.set('0')
    e_coldcoffee.set('0')
    e_mocha.set('0')
    e_mintmojito.set('0')
    e_pinacolada.set('0')
    textroti.config(state=DISABLED)
    textpaneerchilly.config(state=DISABLED)
    textpaneermakhanwala.config(state=DISABLED)
    textvegkolhapuri.config(state=DISABLED)
    textmalaikofta.config(state=DISABLED)
    textnavratankurma.config(state=DISABLED)
    textbuttermasala.config(state=DISABLED)
    textjeerarice.config(state=DISABLED)
    textdalmakhani.config(state=DISABLED)
    textdalfry.config(state=DISABLED)
    textlacchaparatha.config(state=DISABLED)
    textchickenchilly.config(state=DISABLED)
    texttandoorichicken.config(state=DISABLED)
    textmuttonbiryani.config(state=DISABLED)
    textchickentikka.config(state=DISABLED)
    texttangdikebab.config(state=DISABLED)
    texteggbhurji.config(state=DISABLED)
    textfishfry.config(state=DISABLED)
    textmakhmalikebab.config(state=DISABLED)
    textafghanipulao.config(state=DISABLED)
    texttea.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textlemonade.config(state=DISABLED)
    textfruitcocktail.config(state=DISABLED)
    textgingerale.config(state=DISABLED)
    textcocacola.config(state=DISABLED)
    textcoldcoffee.config(state=DISABLED)
    textmocha.config(state=DISABLED)
    textmintmojito.config(state=DISABLED)
    textpinacolada.config(state=DISABLED)
    var1.set('0')
    var2.set('0')
    var3.set('0')
    var4.set('0')
    var5.set('0')
    var6.set('0')
    var7.set('0')
    var8.set('0')
    var9.set('0')
    var10.set('0')
    var11.set('0')
    var12.set('0')
    var13.set('0')
    var14.set('0')
    var15.set('0')
    var16.set('0')
    var17.set('0')
    var18.set('0')
    var19.set('0')
    var20.set('0')
    var21.set('0')
    var22.set('0')
    var23.set('0')
    var24.set('0')
    var25.set('0')
    var26.set('0')
    var27.set('0')
    var28.set('0')
    var29.set('0')
    var30.set('0')
    costofvegvar.set('')
    costofdrinksvar.set('')
    costofnonvegvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')


def save():
    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    bill_data = textreceipt.get(1.0, END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('information', 'Your bill is succesfully saved')
 # total


def totalcost():
    global priceofveg, priceofnonveg, priceofdrinks, subtotalofitems, totalcostofitems, tax
    item1 = int(e_roti.get())
    item2 = int(e_paneerchilly.get())
    item3 = int(e_makhanwala.get())
    item4 = int(e_kolhapuri.get())
    item5 = int(e_malaikofta.get())
    item6 = int(e_kurma.get())
    item7 = int(e_butter.get())
    item8 = int(e_rice.get())
    item9 = int(e_dalmakhani.get())
    item10 = int(e_dalfry.get())

    item11 = int(e_paratha.get())
    item12 = int(e_chickenchilly.get())
    item13 = int(e_tandoori.get())
    item14 = int(e_biryani.get())
    item15 = int(e_tikka.get())
    item16 = int(e_tangdikebab.get())
    item17 = int(e_eggbhurji.get())
    item18 = int(e_fishfry.get())
    item19 = int(e_makhmali.get())
    item20 = int(e_afghanipulao.get())

    item21 = int(e_tea.get())
    item22 = int(e_coffee.get())
    item23 = int(e_fruitcocktail.get())
    item24 = int(e_lemonade.get())
    item25 = int(e_gingerale.get())
    item26 = int(e_cocacola.get())
    item27 = int(e_coldcoffee.get())
    item28 = int(e_mocha.get())
    item29 = int(e_mintmojito.get())
    item30 = int(e_pinacolada.get())

    priceofveg = (item1*7)+(item2*120)+(item3*150)+(item4*110)+(item5*200) + \
        (item6*220)+(item7*150)+(item8*100)+(item9*180)+(item10*90)
    priceofnonveg = (item11*25)+(item12*150)+(item13*180)+(item14*130) + \
        (item15*160)+(item16*120)+(item17*70) + \
        (item18*160)+(item19*120)+(item20*90)
    priceofdrinks = (item21*10)+(item22*15)+(item23*20)+(item24*90) + \
        (item25*300)+(item26*30)+(item27*70) + \
        (item28*80)+(item29*60)+(item30*60)

    costofvegvar.set(str(priceofveg) + ' Rs')
    costofnonvegvar.set(str(priceofnonveg) + ' Rs')
    costofdrinksvar.set(str(priceofdrinks) + ' Rs')

    subtotalofitems = priceofveg+priceofnonveg+priceofdrinks
    subtotalvar.set(str(subtotalofitems) + ' Rs')

    tax = 0.18*subtotalofitems
    servicetaxvar.set(str(tax)+' Rs')

    totalcostofitems = subtotalofitems+tax
    totalcostvar.set(str(totalcostofitems)+' Rs')

 # receipt


def receipt():
    textreceipt.delete(1.0, END)
    x = random.randint(100, 10000)
    billnumbers = 'Bill:'+str(x)
    date = time.strftime('%d/%m/%Y')
    textreceipt.insert(END, 'Receipt Ref:\t\t'+billnumbers+'\t\t'+date+'\n')
    textreceipt.insert(
        END, '*******************************************************************************\n')
    textreceipt.insert(END, 'Items:\t\t Cost of Items(Rs)\n')
    textreceipt.insert(
        END, '*******************************************************************************\n')
    if e_roti.get() != '0':
        textreceipt.insert(END, f'Roti\t\t\t{int(e_roti.get())*7}\n\n')
    if e_paneerchilly.get() != '0':
        textreceipt.insert(
            END, f'Paneer Chilly\t\t\t{int(e_paneerchilly.get()) * 120 }\n\n')
    if e_makhanwala.get() != '0':
        textreceipt.insert(
            END, f'Paneer Makhanwala\t\t\t{int(e_makhanwala.get())*150}\n\n')
    if e_kolhapuri.get() != '0':
        textreceipt.insert(
            END, f'Veg Kolhapuri\t\t\t{int(e_kolhapuri.get())*110}\n\n')
    if e_malaikofta.get() != '0':
        textreceipt.insert(
            END, f'Malai Kofta\t\t\t{int(e_malaikofta.get()) * 200 }\n\n')
    if e_kurma.get() != '0':
        textreceipt.insert(
            END, f'Navratan Kurma\t\t\t{int(e_kurma.get()) * 220 }\n\n')
    if e_butter.get() != '0':
        textreceipt.insert(
            END, f'Paneer Butter Masala\t\t\t{int(e_butter.get()) * 150 }\n\n')
    if e_rice.get() != '0':
        textreceipt.insert(END, f'Jeera Rice\t\t\t{int(e_rice.get())*100}\n\n')
    if e_dalmakhani.get() != '0':
        textreceipt.insert(
            END, f'Dal Makhani\t\t\t{int(e_dalmakhani.get())*180}\n\n')
    if e_dalfry.get() != '0':
        textreceipt.insert(END, f'Dal Fry\t\t\t{int(e_dalfry.get())*90}\n\n')

    if e_paratha.get() != '0':
        textreceipt.insert(
            END, f'Laccha Paratha\t\t\t{int(e_paratha.get())*25}\n\n')
    if e_chickenchilly.get() != '0':
        textreceipt.insert(
            END, f'Chicken Chilly\t\t\t{int(e_chickenchilly.get())*150}\n\n')
    if e_tandoori.get() != '0':
        textreceipt.insert(
            END, f'Tandoori Chicken\t\t\t{int(e_tandoori.get())*180}\n\n')
    if e_biryani.get() != '0':
        textreceipt.insert(
            END, f'Mutton Biryani\t\t\t{int(e_biryani.get())*130}\n\n')
    if e_tikka.get() != '0':
        textreceipt.insert(
            END, f'Chicken Tikka\t\t\t{int(e_tikka.get())*160}\n\n')
    if e_tangdikebab.get() != '0':
        textreceipt.insert(
            END, f'Tangdi Kebab\t\t\t{int(e_tangdikebab.get())*120}\n\n')
    if e_eggbhurji.get() != '0':
        textreceipt.insert(
            END, f'Egg Bhurji\t\t\t{int(e_eggbhurji.get())*70}\n\n')
    if e_fishfry.get() != '0':
        textreceipt.insert(
            END, f'Fish Fry\t\t\t{int(e_fishfry.get())*160}\n\n')
    if e_makhmali.get() != '0':
        textreceipt.insert(
            END, f'Makhmali kebab\t\t\t{int(e_makhmali.get())*120}\n\n')
    if e_afghanipulao.get() != '0':
        textreceipt.insert(
            END, f'Afghani Pulao\t\t\t{int(e_afghanipulao.get())*90}\n\n')

    if e_tea.get() != '0':
        textreceipt.insert(END, f'Tea\t\t\t{int(e_tea.get()) * 10}\n\n')
    if e_coffee.get() != '0':
        textreceipt.insert(END, f'Coffee\t\t\t{int(e_coffee.get()) * 15}\n\n')
    if e_lemonade.get() != '0':
        textreceipt.insert(
            END, f'Lemonade\t\t\t{int(e_lemonade.get()) * 20}\n\n')
    if e_fruitcocktail.get() != '0':
        textreceipt.insert(
            END, f'Fruit Cocktail\t\t\t{int(e_fruitcocktail.get()) * 90}\n\n')
    if e_gingerale.get() != '0':
        textreceipt.insert(
            END, f'Ginger Ale\t\t\t{int(e_gingerale.get()) * 300}\n\n')
    if e_cocacola.get() != '0':
        textreceipt.insert(
            END, f'Coca Cola\t\t\t{int(e_cocacola.get()) * 30}\n\n')
    if e_eggbhurji.get() != '0':
        textreceipt.insert(
            END, f'Egg Bhurji\t\t\t{int(e_eggbhurji.get()) * 70}\n\n')
    if e_mocha.get() != '0':
        textreceipt.insert(END, f'Mocha\t\t\t{int(e_mocha.get()) * 80}\n\n')
    if e_mintmojito.get() != '0':
        textreceipt.insert(
            END, f'Mint Mojito\t\t\t{int(e_mintmojito.get()) * 60}\n\n')
    if e_pinacolada.get() != '0':
        textreceipt.insert(
            END, f'Pinacolada\t\t\t{int(e_pinacolada.get()) * 60}\n\n')
        textreceipt.insert(
            END, '*******************************************************************************\n')
    if costofvegvar.get() != '0 Rs':
        textreceipt.insert(END, f'Cost of Veg:\t\t\t{priceofveg}Rs\n\n')
    if costofnonvegvar.get() != '0 Rs':
        textreceipt.insert(END, f'Cost of Non-Veg:\t\t\t{priceofnonveg}Rs\n\n')
    if costofdrinksvar.get() != '0 Rs':
        textreceipt.insert(END, f'Cost of Drinks:\t\t\t{priceofdrinks}Rs\n\n')
    textreceipt.insert(
        END, '*******************************************************************************\n')
    textreceipt.insert(END, f'Subtotal of items:\t\t\t{subtotalofitems}Rs\n\n')
    textreceipt.insert(END, f'Gst:\t\t\t{tax}Rs\n\n')
    textreceipt.insert(END, f'Total Bill:\t\t\t{totalcostofitems}Rs\n\n')


# 1
def roti():
    if var1.get() == 1:
        textroti.config(state=NORMAL)
        textroti.delete(0, END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')
# 2


def paneerchilly():
    if var2.get() == 1:
        textpaneerchilly.config(state=NORMAL)
        textpaneerchilly.delete(0, END)
        textpaneerchilly.focus()

    else:
        textpaneerchilly.config(state=DISABLED)
        e_paneerchilly.set('0')
# 3


def paneermakhanwala():
    if var3.get() == 1:
        textpaneermakhanwala.config(state=NORMAL)
        textpaneermakhanwala.delete(0, END)
        textpaneermakhanwala.focus()

    else:
        textpaneermakhanwala.config(state=DISABLED)
        e_makhanwala.set('0')

# 4


def Vegkolhapuri():
    if var4.get() == 1:
        textvegkolhapuri.config(state=NORMAL)
        textvegkolhapuri.delete(0, END)
        textvegkolhapuri.focus()
    else:
        textvegkolhapuri.config(state=DISABLED)
        e_kolhapuri.set(0)

# 5


def MalaiKofta():
    if var5.get() == 1:
        textmalaikofta.config(state=NORMAL)
        textmalaikofta.delete(0, END)
        textmalaikofta.focus()
    else:
        textmalaikofta.config(state=DISABLED)
        e_malaikofta.set(0)

# 6


def Navratakurma():
    if var6.get() == 1:
        textnavratankurma.config(state=NORMAL)
        textnavratankurma.delete(0, END)
        textnavratankurma.focus()
    else:
        textnavratankurma.config(state=DISABLED)
        e_kurma.set(0)

# 7


def Paneerbutter():
    if var7.get() == 1:
        textbuttermasala.config(state=NORMAL)
        textbuttermasala.delete(0, END)
        textbuttermasala.focus()
    else:
        textbuttermasala.config(state=DISABLED)
        e_butter.set(0)
# 8


def jeerarice():
    if var8.get() == 1:
        textjeerarice.config(state=NORMAL)
        textjeerarice.delete(0, END)
        textjeerarice.focus()
    else:
        textjeerarice.config(state=DISABLED)
        e_rice.set(0)

# 9


def Dalmakhani():
    if var9.get() == 1:
        textdalmakhani.config(state=NORMAL)
        textdalmakhani.delete(0, END)
        textdalmakhani.focus()
    else:
        textdalmakhani.config(state=DISABLED)
        e_dalmakhani.set(0)

# 10


def Dalfry():
    if var10.get() == 1:
        textdalfry.config(state=NORMAL)
        textdalfry.delete(0, END)
        textdalfry.focus()
    else:
        textdalfry.config(state=DISABLED)
        e_dalfry.set(0)

# 11


def lacchaparatha():
    if var11.get() == 1:
        textlacchaparatha.config(state=NORMAL)
        textlacchaparatha.delete(0, END)
        textlacchaparatha.focus()
    else:
        textlacchaparatha.config(state=DISABLED)
        e_paratha.set(0)
# 12


def chickenchilly():
    if var12.get() == 1:
        textchickenchilly.config(state=NORMAL)
        textchickenchilly.delete(0, END)
        textchickenchilly.focus()
    else:
        textchickenchilly.config(state=DISABLED)
        e_chickenchilly.set(0)

# 13


def tandoorichicken():
    if var13.get() == 1:
        texttandoorichicken.config(state=NORMAL)
        texttandoorichicken.delete(0, END)
        texttandoorichicken.focus()
    else:
        texttandoorichicken.config(state=DISABLED)
        e_tandoori.set(0)

# 14


def Muttonbiryani():
    if var14.get() == 1:
        textmuttonbiryani.config(state=NORMAL)
        textmuttonbiryani.delete(0, END)
        textmuttonbiryani.focus()
    else:
        textmuttonbiryani.config(state=DISABLED)
        e_biryani.set(0)
# 15


def chickentikka():
    if var15.get() == 1:
        textchickentikka.config(state=NORMAL)
        textchickentikka.delete(0, END)
        textchickentikka.focus()
    else:
        textchickentikka.config(state=DISABLED)
        e_tikka.set(0)

# 16


def tangdikebab():
    if var16.get() == 1:
        texttangdikebab.config(state=NORMAL)
        texttangdikebab.delete(0, END)
        texttangdikebab.focus()
    else:
        texttangdikebab.config(state=DISABLED)
        e_tangdikebab.set(0)
# 17


def Eggbhurji():
    if var17.get() == 1:
        texteggbhurji.config(state=NORMAL)
        texteggbhurji.delete(0, END)
        texteggbhurji.focus()
    else:
        texteggbhurji.config(state=DISABLED)
        e_eggbhurji.set(0)
# 18


def fishfry():
    if var18.get() == 1:
        textfishfry.config(state=NORMAL)
        textfishfry.delete(0, END)
        textfishfry.focus()
    else:
        textfishfry.config(state=DISABLED)
        e_fishfry.set(0)
# 19


def makhmalikebab():
    if var19.get() == 1:
        textmakhmalikebab.config(state=NORMAL)
        textmakhmalikebab.delete(0, END)
        textmakhmalikebab.focus()
    else:
        textmakhmalikebab.config(state=DISABLED)
        e_makhmali.set(0)
# 20


def afghanipulao():
    if var20.get() == 1:
        textafghanipulao.config(state=NORMAL)
        textafghanipulao.delete(0, END)
        textafghanipulao.focus()
    else:
        textafghanipulao.config(state=DISABLED)
        e_afghanipulao.set(0)
# 21


def tea():
    if var21.get() == 1:
        texttea.config(state=NORMAL)
        texttea.delete(0, END)
        texttea.focus()
    else:
        texttea.config(state=DISABLED)
        e_tea.set(0)
# 22


def coffee():
    if var22.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0, END)
        textcoffee.focus()
    else:
        textcoffee.config(state=DISABLED)
        e_coffee.set(0)
# 23


def lemonade():
    if var23.get() == 1:
        textlemonade.config(state=NORMAL)
        textlemonade.delete(0, END)
        textlemonade.focus()
    else:
        textlemonade.config(state=DISABLED)
        e_lemonade.set(0)
# 24


def fruitcocktail():
    if var24.get() == 1:
        textfruitcocktail.config(state=NORMAL)
        textfruitcocktail.delete(0, END)
        textfruitcocktail.focus()
    else:
        textfruitcocktail.config(state=DISABLED)
        e_fruitcocktail.set(0)
# 25


def gingerale():
    if var25.get() == 1:
        textgingerale.config(state=NORMAL)
        textgingerale.delete(0, END)
        textgingerale.focus()
    else:
        textgingerale.config(state=DISABLED)
        e_gingerale.set(0)
# 26


def cocacola():
    if var26.get() == 1:
        textcocacola.config(state=NORMAL)
        textcocacola.delete(0, END)
        textcocacola.focus()
    else:
        textcocacola.config(state=DISABLED)
        e_cocacola.set(0)
# 27


def coldcoffee():
    if var27.get() == 1:
        textcoldcoffee.config(state=NORMAL)
        textcoldcoffee.delete(0, END)
        textcoldcoffee.focus()
    else:
        textcoldcoffee.config(state=DISABLED)
        e_coldcoffee.set(0)
# 28


def mocha():
    if var28.get() == 1:
        textmocha.config(state=NORMAL)
        textmocha.delete(0, END)
        textmocha.focus()
    else:
        textmocha.config(state=DISABLED)
        e_mocha.set(0)
# 29


def mintmojito():
    if var29.get() == 1:
        textmintmojito.config(state=NORMAL)
        textmintmojito.delete(0, END)
        textmintmojito.focus()
    else:
        textmintmojito.config(state=DISABLED)
        e_mintmojito.set(0)

# 30


def pinacolada():
    if var30.get() == 1:
        textpinacolada.config(state=NORMAL)
        textpinacolada.delete(0, END)
        textpinacolada.focus()
    else:
        textpinacolada.config(state=DISABLED)
        e_pinacolada.set(0)
# total button function


root = Tk()
root.geometry('1270x690+0+0')
# root.resizable(0,0)#false to disable maximise button
root.title('Doorstep')  # title
root.config(bg='turquoise')
topFrame = Frame(root, bd=10, relief=RIDGE, bg='black')
topFrame.pack(side=TOP)
lableTitle = Label(topFrame, text='Doorstep Restaurant', font=(
    'arial', 30, 'bold'), fg='mediumorchid3', bg='grey81', width=51)
lableTitle.grid(row=0, column=0)
# framemenu
menuFrame = Frame(root, bd=10, relief=RIDGE)
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame, bd=4, relief=RIDGE)
costFrame.pack(side=BOTTOM)

vegFrame = LabelFrame(menuFrame, text='Veg Menu', font=(
    'arial', 19, 'bold'), bd=10, relief=RIDGE)
vegFrame.pack(side=LEFT)

nonvegFrame = LabelFrame(menuFrame, text='Non-Veg Menu',
                         font=('arial', 19, 'bold'), bd=10, relief=RIDGE)
nonvegFrame.pack(side=LEFT)

drinksFrame = LabelFrame(menuFrame, text='Drinks Menu', font=(
    'arial', 19, 'bold'), bd=10, relief=RIDGE)
drinksFrame.pack(side=LEFT)

rightFrame = Frame(root, bd=15, relief=RIDGE)
rightFrame.pack(side=RIGHT)

calculatorFrame = Frame(rightFrame, bd=1, relief=RIDGE)
calculatorFrame.pack()

recieptFrame = Frame(rightFrame, bd=4, relief=RIDGE)
recieptFrame.pack()

buttonFrame = Frame(rightFrame, bd=3, relief=RIDGE)
buttonFrame.pack()

# variables

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()

e_roti = StringVar()
e_paneerchilly = StringVar()
e_makhanwala = StringVar()
e_kolhapuri = StringVar()
e_malaikofta = StringVar()
e_kurma = StringVar()
e_butter = StringVar()
e_rice = StringVar()
e_dalmakhani = StringVar()
e_dalfry = StringVar()

e_roti.set('0')
e_paneerchilly.set('0')
e_makhanwala.set('0')
e_kolhapuri.set('0')
e_malaikofta.set('0')
e_kurma.set('0')
e_butter.set('0')
e_rice.set('0')
e_dalmakhani.set('0')
e_dalfry.set('0')


var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()

e_paratha = StringVar()
e_chickenchilly = StringVar()
e_tandoori = StringVar()
e_biryani = StringVar()
e_tikka = StringVar()
e_tangdikebab = StringVar()
e_eggbhurji = StringVar()
e_fishfry = StringVar()
e_makhmali = StringVar()
e_afghanipulao = StringVar()

e_paratha.set('0')
e_chickenchilly.set('0')
e_tandoori.set('0')
e_biryani.set('0')
e_tikka.set('0')
e_tangdikebab.set('0')
e_eggbhurji.set('0')
e_fishfry.set('0')
e_makhmali.set('0')
e_afghanipulao.set('0')

var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
var28 = IntVar()
var29 = IntVar()
var30 = IntVar()

e_tea = StringVar()
e_coffee = StringVar()
e_fruitcocktail = StringVar()
e_lemonade = StringVar()
e_gingerale = StringVar()
e_cocacola = StringVar()
e_coldcoffee = StringVar()
e_mocha = StringVar()
e_mintmojito = StringVar()
e_pinacolada = StringVar()

e_tea.set('0')
e_coffee.set('0')
e_fruitcocktail.set('0')
e_lemonade.set('0')
e_gingerale.set('0')
e_cocacola.set('0')
e_coldcoffee.set('0')
e_mocha.set('0')
e_mintmojito.set('0')
e_pinacolada.set('0')

costofvegvar = StringVar()
costofnonvegvar = StringVar()
costofdrinksvar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()

# food
roti = Checkbutton(vegFrame, text='Roti', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var1, command=roti)
roti.grid(row=0, column=0, sticky=W)

paneerchilly = Checkbutton(vegFrame, text='Paneer chilly', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var2, command=paneerchilly)
paneerchilly.grid(row=1, column=0, sticky=W)

paneermakhanwala = Checkbutton(vegFrame, text='Paneer Makhanwala', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var3, command=paneermakhanwala)
paneermakhanwala.grid(row=2, column=0, sticky=W)

Vegkolhapuri = Checkbutton(vegFrame, text='Veg Kolhapuri ', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var4, command=Vegkolhapuri)
Vegkolhapuri.grid(row=3, column=0, sticky=W)

Malaikofta = Checkbutton(vegFrame, text='Malai kofta ', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var5, command=MalaiKofta)
Malaikofta.grid(row=4, column=0, sticky=W)

Navratankurma = Checkbutton(vegFrame, text=' Navratan kurma', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var6, command=Navratakurma)
Navratankurma.grid(row=5, column=0, sticky=W)

Paneerbutter = Checkbutton(vegFrame, text='Paneer Butter Masala', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var7, command=Paneerbutter)
Paneerbutter.grid(row=6, column=0, sticky=W)

Jeerarice = Checkbutton(vegFrame, text=' Jeera rice ', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var8, command=jeerarice)
Jeerarice.grid(row=7, column=0, sticky=W)

Dalmakhani = Checkbutton(vegFrame, text=' Dal Makhani', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var9, command=Dalmakhani)
Dalmakhani.grid(row=8, column=0, sticky=W)

Dalfry = Checkbutton(vegFrame, text='Dal fry ', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var10, command=Dalfry)
Dalfry.grid(row=9, column=0, sticky=W)

# nonveg
lacchaparatha = Checkbutton(nonvegFrame, text='laccha paratha', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var11, command=lacchaparatha)
lacchaparatha.grid(row=0, column=1, sticky=W)

Chickenchilly = Checkbutton(nonvegFrame, text=' Chicken chilly', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var12, command=chickenchilly)
Chickenchilly.grid(row=1, column=1, sticky=W)

Tandoorichicken = Checkbutton(nonvegFrame, text='Tandoori chicken ', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var13, command=tandoorichicken)
Tandoorichicken.grid(row=2, column=1, sticky=W)

MuttonBiryani = Checkbutton(nonvegFrame, text=' Mutton Biryani ', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var14, command=Muttonbiryani)
MuttonBiryani.grid(row=3, column=1, sticky=W)

Chickentikka = Checkbutton(nonvegFrame, text='Chicken tikka ', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var15, command=chickentikka)
Chickentikka.grid(row=4, column=1, sticky=W)

Tangdikebab = Checkbutton(nonvegFrame, text=' Tangdi kebab ', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var16, command=tangdikebab)
Tangdikebab.grid(row=5, column=1, sticky=W)

Eggbhurji = Checkbutton(nonvegFrame, text='Egg bhurji', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var17, command=Eggbhurji)
Eggbhurji.grid(row=6, column=1, sticky=W)

fishfry = Checkbutton(nonvegFrame, text=' fish fry ', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var18, command=fishfry)
fishfry.grid(row=7, column=1, sticky=W)

makhmalikebab = Checkbutton(nonvegFrame, text=' Makhmali kebab', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var19, command=makhmalikebab)
makhmalikebab.grid(row=8, column=1, sticky=W)

Afghanipulao = Checkbutton(nonvegFrame, text='Afghani pulao ', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var20, command=afghanipulao)
Afghanipulao.grid(row=9, column=1, sticky=W)

# drinks

tea = Checkbutton(drinksFrame, text='Tea', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var21, command=tea)
tea.grid(row=0, column=2, sticky=W)

coffee = Checkbutton(drinksFrame, text=' Coffee', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var22, command=coffee)
coffee.grid(row=1, column=2, sticky=W)

lemonade = Checkbutton(drinksFrame, text='Lemonade ', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var23, command=lemonade)
lemonade.grid(row=2, column=2, sticky=W)

fruitcocktail = Checkbutton(drinksFrame, text=' Fruit cocktail ', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var24, command=fruitcocktail)
fruitcocktail.grid(row=3, column=2, sticky=W)

gingerale = Checkbutton(drinksFrame, text='Ginger ale ', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var25, command=gingerale)
gingerale.grid(row=4, column=2, sticky=W)

cocacola = Checkbutton(drinksFrame, text=' Coca Cola ', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var26, command=cocacola)
cocacola.grid(row=5, column=2, sticky=W)

coldcoffee = Checkbutton(drinksFrame, text='Cold coffee', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var27, command=coldcoffee)
coldcoffee.grid(row=6, column=2, sticky=W)

mocha = Checkbutton(drinksFrame, text=' mocha ', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var28, command=mocha)
mocha.grid(row=7, column=2, sticky=W)

mintmojito = Checkbutton(drinksFrame, text=' Mint Mojito', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var29, command=mintmojito)
mintmojito.grid(row=8, column=2, sticky=W)

pinacolada = Checkbutton(drinksFrame, text='Pinacolada ', font=(
    'arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var30, command=pinacolada)
pinacolada.grid(row=9, column=2, sticky=W)

# entry field for veg items

textroti = Entry(vegFrame, font=('arial', 18, 'bold'), bd=7,
                 width=4, state=DISABLED, textvariable=e_roti)
textroti.grid(row=0, column=1)

textpaneerchilly = Entry(vegFrame, font=(
    'arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_paneerchilly)
textpaneerchilly.grid(row=1, column=1)

textpaneermakhanwala = Entry(vegFrame, font=(
    'arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_makhanwala)
textpaneermakhanwala.grid(row=2, column=1)

textvegkolhapuri = Entry(vegFrame, font=(
    'arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_kolhapuri)
textvegkolhapuri.grid(row=3, column=1)

textmalaikofta = Entry(vegFrame, font=('arial', 18, 'bold'),
                       bd=7, width=4, state=DISABLED, textvariable=e_malaikofta)
textmalaikofta.grid(row=4, column=1)

textnavratankurma = Entry(vegFrame, font=(
    'arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_kurma)
textnavratankurma.grid(row=5, column=1)

textbuttermasala = Entry(vegFrame, font=(
    'arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_butter)
textbuttermasala.grid(row=6, column=1)

textjeerarice = Entry(vegFrame, font=('arial', 18, 'bold'),
                      bd=7, width=4, state=DISABLED, textvariable=e_rice)
textjeerarice.grid(row=7, column=1)

textdalmakhani = Entry(vegFrame, font=('arial', 18, 'bold'),
                       bd=7, width=4, state=DISABLED, textvariable=e_dalmakhani)
textdalmakhani.grid(row=8, column=1)

textdalfry = Entry(vegFrame, font=('arial', 18, 'bold'), bd=7,
                   width=4, state=DISABLED, textvariable=e_dalfry)
textdalfry.grid(row=9, column=1)

# entry field for non veg

textlacchaparatha = Entry(nonvegFrame, font=(
    'arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_paratha)
textlacchaparatha.grid(row=0, column=2)

textchickenchilly = Entry(nonvegFrame, font=(
    'arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_chickenchilly)
textchickenchilly.grid(row=1, column=2)

texttandoorichicken = Entry(nonvegFrame, font=(
    'arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_tandoori)
texttandoorichicken.grid(row=2, column=2)

textmuttonbiryani = Entry(nonvegFrame, font=(
    'arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_biryani)
textmuttonbiryani.grid(row=3, column=2)

textchickentikka = Entry(nonvegFrame, font=(
    'arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_tikka)
textchickentikka.grid(row=4, column=2)

texttangdikebab = Entry(nonvegFrame, font=(
    'arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_tangdikebab)
texttangdikebab.grid(row=5, column=2)

texteggbhurji = Entry(nonvegFrame, font=('arial', 18, 'bold'),
                      bd=7, width=4, state=DISABLED, textvariable=e_eggbhurji)
texteggbhurji.grid(row=6, column=2)

textfishfry = Entry(nonvegFrame, font=('arial', 18, 'bold'),
                    bd=7, width=4, state=DISABLED, textvariable=e_fishfry)
textfishfry.grid(row=7, column=2)

textmakhmalikebab = Entry(nonvegFrame, font=(
    'arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_makhmali)
textmakhmalikebab.grid(row=8, column=2)

textafghanipulao = Entry(nonvegFrame, font=(
    'arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_afghanipulao)
textafghanipulao.grid(row=9, column=2)

# entry field for drinks

texttea = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7,
                width=4, state=DISABLED, textvariable=e_tea)
texttea.grid(row=0, column=3)

textcoffee = Entry(drinksFrame, font=('arial', 18, 'bold'),
                   bd=7, width=4, state=DISABLED, textvariable=e_coffee)
textcoffee.grid(row=1, column=3)

textlemonade = Entry(drinksFrame, font=('arial', 18, 'bold'),
                     bd=7, width=4, state=DISABLED, textvariable=e_lemonade)
textlemonade.grid(row=2, column=3)

textfruitcocktail = Entry(drinksFrame, font=(
    'arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_fruitcocktail)
textfruitcocktail.grid(row=3, column=3)

textgingerale = Entry(drinksFrame, font=('arial', 18, 'bold'),
                      bd=7, width=4, state=DISABLED, textvariable=e_gingerale)
textgingerale.grid(row=4, column=3)

textcocacola = Entry(drinksFrame, font=('arial', 18, 'bold'),
                     bd=7, width=4, state=DISABLED, textvariable=e_cocacola)
textcocacola.grid(row=5, column=3)

textcoldcoffee = Entry(drinksFrame, font=(
    'arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_coldcoffee)
textcoldcoffee.grid(row=6, column=3)

textmocha = Entry(drinksFrame, font=('arial', 18, 'bold'),
                  bd=7, width=4, state=DISABLED, textvariable=e_mocha)
textmocha.grid(row=7, column=3)

textmintmojito = Entry(drinksFrame, font=(
    'arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_mintmojito)
textmintmojito.grid(row=8, column=3)

textpinacolada = Entry(drinksFrame, font=(
    'arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_pinacolada)
textpinacolada.grid(row=9, column=3)

#costlabels & entryfields

labelcostofveg = Label(costFrame, text='Cost of Veg items',
                       font=('arial', 16, 'bold'))
labelcostofveg.grid(row=0, column=0, sticky=W)

textcostofveg = Entry(costFrame, font=('arial', 16, 'bold'),
                      bd=4, state='readonly', textvariable=costofvegvar)
textcostofveg.grid(row=0, column=1)

labelcostofnonveg = Label(
    costFrame, text='Cost of Non-Veg items', font=('arial', 16, 'bold'))
labelcostofnonveg.grid(row=1, column=0, sticky=W)

textcostofnonveg = Entry(costFrame, font=(
    'arial', 16, 'bold'), bd=4, state='readonly', textvariable=costofnonvegvar)
textcostofnonveg.grid(row=1, column=1)

labelcostofdrinks = Label(
    costFrame, text='Cost of Drinks', font=('arial', 16, 'bold'))
labelcostofdrinks.grid(row=2, column=0, sticky=W)

textcostofdrinks = Entry(costFrame, font=(
    'arial', 16, 'bold'), bd=4, state='readonly', textvariable=costofdrinksvar)
textcostofdrinks.grid(row=2, column=1)

labelsubtotal = Label(costFrame, text='Sub Total', font=('arial', 16, 'bold'))
labelsubtotal.grid(row=0, column=2, sticky=W, padx='41')

textsubtotal = Entry(costFrame, font=('arial', 16, 'bold'),
                     bd=4, state='readonly', textvariable=subtotalvar)
textsubtotal.grid(row=0, column=3, padx='41')

labelservicetax = Label(costFrame, text='Service tax',
                        font=('arial', 16, 'bold'))
labelservicetax.grid(row=1, column=2, sticky=W, padx='41')

textservicetax = Entry(costFrame, font=('arial', 16, 'bold'),
                       bd=4, state='readonly', textvariable=servicetaxvar)
textservicetax.grid(row=1, column=3, padx='41')

labelTotalcost = Label(costFrame, text='Total cost',
                       font=('arial', 16, 'bold'))
labelTotalcost.grid(row=2, column=2, sticky=W, padx='41')

textTotalcost = Entry(costFrame, font=('arial', 16, 'bold'),
                      bd=4, state='readonly', textvariable=totalcostvar)
textTotalcost.grid(row=2, column=3, padx='41')

# buttons
buttontotal = Button(buttonFrame, text='Total', font=(
    'arial', 14, 'bold'), bd=3, padx=5, command=totalcost)
buttontotal.grid(row=0, column=0)

buttonreceipt = Button(buttonFrame, text='Receipt', font=(
    'arial', 14, 'bold'), bd=3, padx=5, command=receipt)
buttonreceipt.grid(row=0, column=1)

buttonsave = Button(buttonFrame, text='Save', font=(
    'arial', 14, 'bold'), bd=3, padx=5, command=save)
buttonsave.grid(row=0, column=2)

buttonreset = Button(buttonFrame, text='Reset', font=(
    'arial', 14, 'bold'), bd=3, padx=5, command=reset)
buttonreset.grid(row=0, column=3)

# receipt area

textreceipt = Text(recieptFrame, font=('arial', 12, 'bold'), bd=3)
textreceipt.grid(row=0, column=0)


root.mainloop()
