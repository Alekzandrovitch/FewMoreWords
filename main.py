from tkinter import *
from RhymeZone import *
#

#main
def DisplayWords(word, rhymes):
	
    doct_words[word] = rhymes
    searched_x_coord = 100
    searched_y_coord = 100
    diamter = len(doct_words[word]) *2
    print(diamter)
    radius = diamter / 2
    
    x0 = game_canvas.canvasx(searched_x_coord)
    y0 = game_canvas.canvasy(searched_y_coord)
    searched_circle = game_canvas.create_oval(x0,y0,x0+diamter,y0+diamter,fill="blue",outline="#DDD", width=5)
    searched_text = game_canvas.create_text(x0+radius,y0+radius,tag="seached_output",text=word)
    angle = 0
    inc = 0
    for each in doct_words[word]:
        #print(each)

        display_x_coord = searched_x_coord + (radius+30)  * math.cos(angle)
        display_y_coord = searched_y_coord +(radius+30) * math.sin(angle)
        if angle <= 20:
            display_noun = game_canvas.create_text(display_x_coord+radius,display_y_coord+radius+inc,tag="rhyme_output",text=each["word"])
        
        angle +=1

def rhyme_callback():
    s = content.get()
    a = Rhyme(s)
    intr = 0
    
    game_canvas.delete("rhyme_output")
    for item in a:
        output = game_canvas.create_text(50,50+(intr*13),tag="rhyme_output",text=item['word'])
        intr+=1
    flag_rhyme_out = "On"

def reverse_dictionary_callback():
    s = content.get()
    a = ReverseDictionary(s)
    intr = 0
    game_canvas.delete("rd_output")
    for item in a:
        output_rd = game_canvas.create_text(150,50+(intr*13),tag="rd_output",text=item['word'])
        intr+=1

def adjective_callback():
    s = content.get()
    a = Adjective(s)
    intr =0
    game_canvas.delete("adj_output")
    for item in a:
        output_adj = game_canvas.create_text(250,50+(intr*13),tag="adj_output",text=item['word'])
        intr+=1

def noun_callback():
    s = content.get()
    a = Noun(s)
    intr=0
    game_canvas.delete("noun_output")
    for item in a:
        output_noun = game_canvas.create_text(350,50+(intr*13),tag="noun_output",text=item['word'])
        intr+=




root = Tk()
content = StringVar()
label_name = Label(root,text='PoeMore').grid(row=0,column=0)
tkvar = StringVar(root)
#This should be for old poems saved

#drop_down_search = OptionMenu(root,tkvar, *choices).grid(row=1)

search_text = Entry(root, textvariable=content)
rhyme_button = Button(root,text='Rhyme',command= rhyme_callback)
adjective_button = Button(root,text="Adjective",command=adjective_callback)
reverse_dictionary_button = Button(root,text='Reverse Dictionary',command=reverse_dictionary_callback)
noun_button = Button(root, text='Noun',command=noun_callback)
label_noun = Label(root, text='Find nouns that go with an adjective')
label_rhyme = Label(root,text='Finds a rhyming word for your query')
label_adjective = Label(root, text='adjectives that are often used to describe')
label_RD = Label(root, text='Used to find words with a searched definition')
game_canvas = Canvas(root, width=600, height=600)
entry_text = Text(root)

entry_text.grid(row=4, column=5, columnspan=3)
search_text.grid(row=1,column=2,columnspan=6)
rhyme_button.grid(row=2,column=0)
label_rhyme.grid(row=0,column=3)
label_adjective.grid(row=0,column=3)
adjective_button.grid(row=2,column=1)
label_RD.grid(row=0,column=3)
reverse_dictionary_button.grid(row=3,column=1)
label_noun.grid(row=0,column=2)
noun_button.grid(row=3,column=0)
game_canvas.grid(row=4,column=0,columnspan=4)

flag_rhyme_out = "Off";

display_var = StringVar()



root.geometry('1400x900')
root.mainloop()



