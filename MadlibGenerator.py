from tkinter import *

def create_horror_story():
    top = Toplevel()
    top.title("Scary Story Maker")
    top.geometry("700x800")
    top.config(bg='lightblue')
    
    Label(top, text="Create Your Horror Story", font=("Arial", 20)).pack(pady=10)
    
    labels = [
        "Your name:",
        "A scary place:",
        "A monster:",
        "A weapon:",
        "A strange sound:",
        "A time of night:"
    ]
    
    entries = []
    for i, text in enumerate(labels):
        Label(top, text=text).pack()
        entry = Entry(top, width=30)
        entry.pack()
        entries.append(entry)
    
    def show_story():
        name = entries[0].get()
        place = entries[1].get()
        monster = entries[2].get()
        weapon = entries[3].get()
        sound = entries[4].get()
        time = entries[5].get()
        
        story = f"""One dark night, {name} was walking through {place} when suddenly...
They heard a terrifying {sound}! It was {time} when {monster} appeared!
The creature attacked with a {weapon}, but {name} bravely fought back.
After a scary struggle, {name} escaped - but they'll never forget that night!"""
        
        story_label = Label(top, text=story, wraplength=400, justify="left")
        story_label.pack(pady=20)
    
    Button(top, text="Make My Story!", background='coral',command=show_story).pack(pady=10)

def create_adventure_story():
    top = Toplevel()
    top.title("Ancient Adventure Maker")
    top.geometry("700x800")
    top.config(bg='lightgreen')
    
    Label(top, text="Create Your Ancient Adventure", font=("Arial", 20)).pack(pady=10)
    
    labels = [
        "Explorer's name:",
        "Lost civilization:",
        "Ancient artifact:",
        "Year of discovery:",
        "A dangerous trap:",
        "Final outcome:"
    ]
    
    entries = []
    for i, text in enumerate(labels):
        Label(top, text=text).pack()
        entry = Entry(top, width=30)
        entry.pack()
        entries.append(entry)
    
    def show_story():
        name = entries[0].get()
        civilization = entries[1].get()
        artifact = entries[2].get()
        year = entries[3].get()
        trap = entries[4].get()
        outcome = entries[5].get()
        
        story = f"""In {year}, archaeologist {name} discovered the lost {civilization}.
Deep in the ruins, they found the legendary {artifact}!
But suddenly, a deadly {trap} activated!
After a narrow escape, {name} realized {outcome}.
This discovery would change history forever!"""
        
        story_label = Label(top, text=story, wraplength=400, justify="left")
        story_label.pack(pady=20)
    
    Button(top, text="Make My Adventure!", background='coral',command=show_story).pack(pady=10)

# Main window
root = Tk()
root.title("My Story Maker")
root.geometry("500x500")

Label(root, text="Choose Your Story", font=("Arial", 20)).pack(pady=20)

Button(root, text="Horror Story", background ='grey',command=create_horror_story, height=2, width=15).pack(pady=10)
Button(root, text="Ancient Adventure", background ='grey',command=create_adventure_story, height=2, width=15).pack(pady=10)

root.mainloop()