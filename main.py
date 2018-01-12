
#Created by Ian Kretz
#A crime of passion by python standards i know
#Using Python 3 call main.py
#You will need to pip install PyDictionary, and Requests
#You will need the internet.
#Version V1.01 i think
#There is no control Z for text box
from tkinter import *
from RhymeZone import *
from PyDictionary import PyDictionary
import math
#
#get highlighted text, create timer for app.py to be called

#main

doct_words = {}
#Calls the API for antoymns
def PyAntnon(word):
    return pDict.antonym(word)
#Calls the API for synonymns
def PySynonym(word):
    return pDict.synonym(word)
#Calls the API for dictionary
def PyDictionMeaning(word):
    mean = pDict.meaning(word)
    print(mean)
    return mean
#Callback for button Antoynm
def PyDictAnton_Callback():
    game_canvas.delete("PyD")
    search = content.get()
    bler = PyAntnon(search)
    y = 0
    for each in bler:
        game_canvas.create_text(850,100+y,text=each, tag="PyD")
        y+=20
#call back for synonym        
def PyDictSynon_Callback():
    game_canvas.delete("PyD")
    search = content.get()
    bleg = PySynonym(search)
    y = 0
    for each in bleg:
        game_canvas.create_text(850,100+y,text=each,tag="PyD")
        y+=20
#Cal back for dictionary
def PyDictMeaning_Callback():
    game_canvas.delete("PyD")
    search = content.get()
    bleh = PyDictionMeaning(search)
    y = 0
    x = 0
    for each in bleh:
        for item in bleh[each]:
            game_canvas.create_text(850,120+y,text=item,tag="PyD")
            y+=10
#Unused function to display words in a circle
def DisplayWords(word, rhymes):
	
    doct_words[word] = rhymes
    searched_x_coord = 100
    searched_y_coord = 100
    diamter = len(doct_words[word]) * 3
    oval_offset = diamter * 2 
    diamterY =  oval_offset
    print(diamter)
    radius = diamter / 2
    radiusY = diamterY / 2
    x0 = game_canvas.canvasx(searched_x_coord)
    y0 = game_canvas.canvasy(searched_y_coord)
    searched_circle = game_canvas.create_oval(x0,y0,x0+diamter,y0+diamterY,fill="blue",outline="#DDD", width=5)
    searched_text = game_canvas.create_text(x0+radius,y0+radiusY,tag="seached_output",text=word)
    angle = 0
    inc = 0
    for each in doct_words[word]:
        #print(each)

        display_x_coord = searched_x_coord + (radius+ 30)  * math.sin(math.degrees(angle))
        display_y_coord = searched_y_coord +(radiusY + 30) * math.cos(math.degrees(angle))
        
        #display_x_coord = searched_x_coord * math.cos(math.degrees(angle)) + searched_y_coord * math.sin(math.degrees(angle))
        #isplay_y_coord = -searched_x_coord * math.sin(math.degrees(angle)) + searched_y_coord * math.cos(math.degrees(angle))

        #print(angle) 
        theta = math.atan((display_x_coord/display_y_coord))
        #print(theta)
        #print(math.radians(90))
        
        display_noun = game_canvas.create_text(display_x_coord+radius,display_y_coord+radiusY,angle=math.degrees(theta),tag="rhyme_output",text=each["word"])
        #elif theta > math.radians(90) and theta <= math.radians(180):
            #display_noun = game_canvas.create_text(display_x_coord+radius,display_y_coord+radiusY+inc,angle=math.degrees(theta),tag="rhyme_output",text=each["word"])
        #elif theta > math.radians(180) and theta <= math.radians(270):
           # display_noun = game_canvas.create_text(display_x_coord+radius,display_y_coord+radiusY+inc,angle=math.degrees(theta),tag="rhyme_output",text=each["word"])
        #elif theta > math.radians(270) and theta <= math.radians(360):
          #  display_noun = game_canvas.create_text(display_x_coord+radius,display_y_coord+radiusY+inc,angle=math.degrees(theta),tag="rhyme_output",text=each["word"])
        angle += 360/ len(doct_words[word])
       # angle = math.floor(angle)
        print(angle)
#callback for start with
def start_with_callback():
    game_canvas.delete("start_with_output")
    search = content.get()
    rhymes = StartWithAndRelated(search)
    #DisplayWords(search,rhymes)
    intr = 0
    
    
    for item in rhymes:
        output = game_canvas.create_text(750,50+(intr*13),tag="start_with_output",text=item['word'])
        intr+=1
#call back for end with
def end_with_callback():
    game_canvas.delete("end_with_output")
    search = content.get()
    rhymes = EndWithAndRelated(search)
    #DisplayWords(search,rhymes)
    intr = 0
    
    
    for item in rhymes:
        output = game_canvas.create_text(650,50+(intr*13),tag="end_with_output",text=item['word'])
        intr+=1
#call back for button related to rhyme
def rhyme_related_callback():
    game_canvas.delete("rhyme_related_output")
    search = content.get()
    rhymes = RhymeAndRelated(search)
    #DisplayWords(search,rhymes)
    intr = 0
    
    
    for item in rhymes:
        output = game_canvas.create_text(550,50+(intr*13),tag="rhyme_related_output",text=item['word'])
        intr+=1
#call back for rhyme
def rhyme_callback():
    game_canvas.delete("rhyme_output")
    search = content.get()
    rhymes = Rhyme(search)
    #DisplayWords(search,rhymes)
    intr = 0
    
    
    for item in rhymes:
        output = game_canvas.create_text(450,50+(intr*13),tag="rhyme_output",text=item['word'])
        intr+=1
    #flag_rhyme_out = "On"
#call back for reverse dictionary API
def reverse_dictionary_callback():
    s = content.get()
    a = ReverseDictionary(s)
    intr = 0
    game_canvas.delete("rd_output")
    for item in a:
        output_rd = game_canvas.create_text(150,50+(intr*13),tag="rd_output",text=item['word'])
        intr+=1
#Call back for adjective
def adjective_callback():
    s = content.get()
    a = Adjective(s)
    intr =0
    game_canvas.delete("adj_output")
    for item in a:
        output_adj = game_canvas.create_text(250,50+(intr*13),tag="adj_output",text=item['word'])
        intr+=1
#Call back for noun
def noun_callback():
    s = content.get()
    a = Noun(s)
    intr=0
    game_canvas.delete("noun_output")
    for item in a:
        output_noun = game_canvas.create_text(350,50+(intr*13),tag="noun_output",text=item['word'])
        intr+=1

root = Tk()
pDict = PyDictionary()
frame_buttons=Frame(root, width=500, height=100,borderwidth=1,relief=SUNKEN)
frame_text = Frame(root, width= 500, height=200,borderwidth=1,relief=SUNKEN)
frame_display = Frame(root, width=500, height=600,borderwidth=1,relief=SUNKEN)
frame_results = Frame(root,width=1400-500, height=600,borderwidth=1,relief=SUNKEN)

frame_buttons.grid(row=0,column=0)
frame_text.grid(row=1,column=0)
frame_display.grid(row=2,column=0)
frame_results.grid(row=0,column=2,rowspan=2)

#frame_buttons.columnconfigure(1,weight=1)
frame_text.columnconfigure(1,weight=3)
content = StringVar()
#label_name = Label(frame,text='PoeMore').grid(row=0,column=0)
#tkvar = StringVar(frame)
#This should be for old poems saved

#drop_down_search = OptionMenu(root,tkvar, *choices).grid(row=1)
entry_text = Text(frame_text)
search_text = Entry(frame_buttons, textvariable=content)
rhyme_button = Button(frame_buttons,text='Rhyme',command= rhyme_callback)
adjective_button = Button(frame_buttons,text="Adjective",command=adjective_callback)
reverse_dictionary_button = Button(frame_buttons,text='Reverse Dictionary',command=reverse_dictionary_callback)
noun_button = Button(frame_buttons, text='Noun',command=noun_callback)
#label_noun = Label(frame, text='Find nouns that go with an adjective')
#label_rhyme = Label(frame,text='Finds a rhyming word for your query')
#label_adjective = Label(frame, text='adjectives that are often used to describe')
#label_RD = Label(frame, text='Used to find words with a searched definition')
game_canvas = Canvas(frame_results, width=600, height=600, scrollregion=(0,0,1500,1500))
display_canvas = Canvas(frame_display, width=500, height=600, scrollregion=(0,0,1500,1500))
hbar = Scrollbar(frame_results,orient=HORIZONTAL)
vbar = Scrollbar(frame_results,orient=VERTICAL)
hbar2 = Scrollbar(frame_display,orient=HORIZONTAL)
vbar2 = Scrollbar(frame_display,orient=VERTICAL)
start_with_button = Button(frame_buttons, text="Starts with", command=start_with_callback)
end_with_button = Button(frame_buttons, text="Ends with", command=end_with_callback)
rhyme_related_button = Button(frame_buttons, text="Rhyme Related", command=rhyme_related_callback)
meaning_button = Button (frame_buttons, text="Dictionary",command=PyDictMeaning_Callback)
antonym_button = Button (frame_buttons, text="Antoyn",command=PyDictAnton_Callback)
synonym_button = Button(frame_buttons, text="Synonyn",command=PyDictSynon_Callback)

hbar.config(command=game_canvas.xview)
vbar.config(command=game_canvas.yview)
hbar2.config(command=display_canvas.xview)
vbar2.config(command=display_canvas.yview)

game_canvas.config(xscrollcommand=hbar.set,yscrollcommand=vbar.set)
display_canvas.config(xscrollcommand=hbar2.set,yscrollcommand=vbar2.set)

#search_text.pack()
#rhyme_button.pack()
#adjective_button.pack()
#reverse_dictionary_button.pack()
#noun_button.pack()
#hbar.pack(side=BOTTOM,fill=X)
#hbar.pack(side=RIGHT,fill=Y)
#game_canvas.pack(side=LEFT,expand=True,fill=BOTH)
#entry_text.grid(row=4, column=5, columnspan=3)
search_text.grid(row=1,column=2)
rhyme_button.grid(row=2,column=0)
#label_rhyme.grid(row=0,column=3)
#label_adjective.grid(row=0,column=3)
adjective_button.grid(row=2,column=1)
#label_RD.grid(row=0,column=3)
reverse_dictionary_button.grid(row=3,column=1)
#label_noun.grid(row=0,column=2)
noun_button.grid(row=3,column=0)
rhyme_related_button.grid(row=2,column=2)
start_with_button.grid(row=3, column=2)
end_with_button.grid(row=2, column=3)
meaning_button.grid(row=2, column=4)
antonym_button.grid(row=2,column=5)
synonym_button.grid(row=3,column=5)

game_canvas.grid(row=0,column=0)
hbar.grid(row=1,column=0)
vbar.grid(row=0,column=1)
#hbar.columnconfigure(1,weight=1)
#vbar.columnconfigure(1,weight=1)
entry_text.grid(row=0, column=0)

display_canvas.grid(row=1,column=1)
hbar2.grid(row=0,column=0)
vbar2.grid(row=0,column=0,rowspan=4)
#flag_rhyme_out = "Off";
#w.pack()
#w.create_line(0, 0, 200, 100)
#w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
display_var = StringVar()

#display_entry.insert(0,)
# while True:                 # Infinite loop simulation
 #   space.step(0.02)        # Step the simulation one step forward
    

root.geometry('1400x900')
root.mainloop()



