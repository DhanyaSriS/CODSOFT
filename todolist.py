import tkinter
from tkinter import *
import tkinter.messagebox
import pickle
root=Tk()
root.title("TO-DO-LIST")
root.geometry("570x600+100+200")
root.resizable(True,True)
root.configure(bg="lightcyan3")


def task_add():
    todo=entry_task.get()
    if todo!="":
        todo_list.insert(tkinter.END,todo)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="WARNING ALERT!!!",message="please select ADD TASK to add the task")


def task_del():
    try:
        selected_index = todo_list.curselection()[0]
        selected_task = todo_list.get(selected_index)
        todo_list.delete(selected_index)
        try:
            with open("tasks.dat", "rb") as file:
                tasks = list(pickle.load(file))  
        except FileNotFoundError:
            tasks = []

        if selected_task in tasks:
            tasks.remove(selected_task)
            with open("tasks.dat", "wb") as file:
                pickle.dump(tasks, file)

            tkinter.messagebox.showinfo("Success", "Task deleted successfully!")
        else:
            tkinter.messagebox.showwarning(title='WARNING ALERT!!!', message="Task not found in the list")

    except IndexError:
        tkinter.messagebox.showwarning(title='WARNING ALERT!!!', message="Please select a TASK to delete")

def task_display():
    try:
        todo_list.delete(0, tkinter.END)
        tasks = pickle.load(open("tasks.dat", "rb"))
        for task in tasks:
            todo_list.insert(tkinter.END, task)
    except FileNotFoundError:
        tkinter.messagebox.showwarning(title="WARNING ALERT!!!", message="Cannot find tasks.dat")

def task_save():
    try:
        todo_list_content = todo_list.get(0, tkinter.END)
        pickle.dump(todo_list_content, open("tasks.dat", "wb"))
    except FileNotFoundError:
        tkinter.messagebox.showwarning(title="WARNING ALERT!!!", message="select a TASK to save")

def task_completed():
    try:
        selected_index = todo_list.curselection()[0]
        todo_list.itemconfig(selected_index, {'fg': 'antiquewhite4'})  
        todo_list.selection_clear(selected_index)  
    except IndexError:
        tkinter.messagebox.showwarning(title='WARNING ALERT!!!', message="Please select a TASK to mark completed")



list_frame=tkinter.Frame(root)
list_frame.pack()


todo_list=tkinter.Listbox(list_frame,height=20,width=70)
todo_list.pack(side=tkinter.LEFT)


scroll=tkinter.Scrollbar(list_frame)
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)

todo_list.config(yscrollcommand=scroll.set)

entry_task=tkinter.Entry(root,width=80)
entry_task.pack()


add_button=Button(root,text='ADD TASK',font=("Lucida Handwriting",20,"bold"),bg="palegreen1",width=40,command=task_add)
add_button.pack()


savetask_button=tkinter.Button(root,text='SAVE TASK',font=("Lucida Handwriting",20,"bold"),bg="pink1",width=40,command=task_save)
savetask_button.pack()


completed_button=tkinter.Button(root,text='MARK AS COMPLETED TASK',font=("Lucida Handwriting",20,"bold"),bg="thistle1",width=40,command=task_completed)
completed_button.pack()


display_button=Button(root,text='DISPLAY TASK',font=("Lucida Handwriting",20,"bold"),bg="lightcyan1",width=40,command=task_display)
display_button.pack()


del_button=Button(root,text='DELETE TASK',font=("Lucida Handwriting",20,"bold"),bg="darkslategray1",width=40,command=task_del)
del_button.pack()



root.mainloop()
