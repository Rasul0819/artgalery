import tkinter

from db import add_datas_to_artists,view_all_artists

window=tkinter.Tk()
window.geometry('800x900')
window.title('Example')
window.config(bg='#BFBDC1')
def add_artist():
	name = name_entry.get()
	address = address_entry.get()
	town = town_entry.get()
	country = country_entry.get()
	post = post_entry.get()
	add_datas_to_artists(name,address,town,country,post)

def view_artists():
	names = view_all_artists()
	for i in names:
		listbox.insert(0,i)


listbox=tkinter.Listbox(bg='white',width=170,height=25)
listbox.place(x=25,y=250)

enter_lbl=tkinter.Label(text= 'Enter new details:',bg='#BFBDC1')
enter_lbl.place(x=10,y=10)

name_lbl=tkinter.Label(text= 'Name:',bg='#BFBDC1')
name_lbl.place(x=20,y=40)

name_entry=tkinter.Entry(bg='white',fg='black',width=18)
name_entry.place(x=80,y=40)

add_but=tkinter.Button(
	window,
	text='Add artist',
	bg='#878D91',
	fg='black',
	width=15,
	command=add_artist)
add_but.place(x=80,y=75)

artist_lbl=name_lbl=tkinter.Label(text= 'Artist ID:',bg='#BFBDC1')
artist_lbl.place(x=20,y=120)

artist_entry=tkinter.Entry(bg='white',fg='black',width=18)
artist_entry.place(x=80,y=120)

piece_but=tkinter.Button(window,text='Add piece',bg='#878D91',fg='black',width=15)
piece_but.place(x=80,y=155)

address_lbl=name_lbl=tkinter.Label(text= 'Adress:',bg='#BFBDC1')
address_lbl.place(x=250,y=40)

address_entry=tkinter.Entry(bg='white',fg='black',width=18)
address_entry.place(x=310,y=40)

clear_but=tkinter.Button(window,text='Clear artist',bg='#878D91',fg='black',width=15)
clear_but.place(x=310,y=75)
                
title_lbl=tkinter.Label(text= 'Title:',bg='#BFBDC1')
title_lbl.place(x=250,y=120)

title_entry=tkinter.Entry(bg='white',fg='black',width=18)
title_entry.place(x=310,y=120)

clearpiece_but=tkinter.Button(window,text='Clear piece',bg='#878D91',fg='black',width=15)
clearpiece_but.place(x=310,y=155)

town_lbl= tkinter.Label(text='Town:',bg='#BFBDC1',fg='black')
town_lbl.place(x=460,y=40)

town_entry=tkinter.Entry(bg='white',fg='black',width=18)
town_entry.place(x=510,y=40)

style_lbl = tkinter.Label(text='Style:',bg='#BFBDC1',fg='black')
style_lbl.place(x=460,y=120)

var = tkinter.StringVar()
var.set('neon')
values = 'oil,watercolor,neon'.split(',')
style_option_1 = tkinter.OptionMenu(window,var,*values)
style_option_1.place(x=510,y=120)

country_lbl=tkinter.Label(text='Country:',bg='#BFBDC1',fg='black')
country_lbl.place(x=650,y=40)

country_entry=tkinter.Entry(bg='white',fg='black',width=18)
country_entry.place(x=710,y=40)

post_lbl=tkinter.Label(text='Post code:',bg='#BFBDC1',fg='black')
post_lbl.place(x=840,y=40)

post_entry=tkinter.Entry(bg='white',fg='black',width=18)
post_entry.place(x=910,y=40)

price_lbl=tkinter.Label(text='Price:',bg='#BFBDC1',fg='black')
price_lbl.place(x=650,y=120)

price_entry=tkinter.Entry(bg='white',fg='black',width=18)
price_entry.place(x=710,y=120)

output_but=tkinter.Button(window,text='Clear output',bg='#878D91',fg='black',width=25)
output_but.place(x=1100,y=250)

view_but=tkinter.Button(
	window,text='View all artists',
	bg='#878D91',fg='black',width=25,
	command=view_artists)
view_but.place(x=1100,y=300)

arts_but=tkinter.Button(window,text='View all arts',bg='#878D91',fg='black',width=25)
arts_but.place(x=1100,y=350)

search_entry=tkinter.Entry(bg='white',fg='black',width=15)
search_entry.place(x=1100,y=400)

search1_but=tkinter.Button(window,text='Search',bg='#878D91',fg='black',width=10)
search1_but.place(x=1200,y=400)

search2_but=tkinter.Button(window,text='Search',bg='#878D91',fg='black',width=10)
search2_but.place(x=1200,y=430)

style2_lbl = tkinter.Label(text='Style',bg='#BFBDC1',fg='black')
style2_lbl.place(x=1150,y=430)


min_lbl=tkinter.Label(text='MIN:',bg='#BFBDC1',fg='black')
min_lbl.place(x=1100,y=480)

max_lbl=tkinter.Label(text='MAX:',bg='#BFBDC1',fg='black')
max_lbl.place(x=1200,y=480)

min_entry=tkinter.Entry(bg='white',fg='black',width=15)
min_entry.place(x=1100,y=510)

max_entry=tkinter.Entry(bg='white',fg='black',width=15)
max_entry.place(x=1200,y=510)

search3_but=tkinter.Button(window,text='Search',bg='#878D91',fg='black',width=25)
search3_but.place(x=1100,y=560)

sold_entry = tkinter.Entry(bg='white',fg='black',width=15)
sold_entry.place(x=1100,y=610)

sold_but =tkinter.Button(window,text='Sold',bg='#878D91',fg='black',width=15)
sold_but.place(x=1200,y=610)



window.mainloop()