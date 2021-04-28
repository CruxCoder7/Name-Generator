import random
import requests
import os
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox

# Web Scraping for Male First Names
mf_URL = "https://www.familyeducation.com/baby-names/popular-names/boys"
mf_headers = {
    "User-Agent": 'Mozilla/5.0(Windows NT 6.1Win64x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 87.0 .4280 .141 Safari / 537.36 '}
mf_page = requests.get(mf_URL, headers=mf_headers)
mf_soup = BeautifulSoup(mf_page.content, 'html.parser')

# Web Scraping for Female First Names
ff_URL = "https://www.familyeducation.com/baby-names/popular-names/girls"
ff_headers = {
    "User-Agent": 'Mozilla/5.0(Windows NT 6.1Win64x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 87.0 .4280 .141 Safari / 537.36 '}
ff_page = requests.get(ff_URL, headers=ff_headers)
ff_soup = BeautifulSoup(ff_page.content, 'html.parser')

# Web Scraping for Male and Female Last Names
mfl_URL = "https://www.al.com/news/2019/10/50-most-common-last-names-in-america.html"
mfl_headers = {
    "User-Agent": 'Mozilla/5.0(Windows NT 6.1Win64x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 87.0 .4280 .141 Safari / 537.36 '}
mfl_page = requests.get(mfl_URL, headers=mfl_headers)
mfl_soup = BeautifulSoup(mfl_page.content, 'html.parser')

# Male First Names
male_first_names_list = []
mf_ul = mf_soup.find_all('ul', {'class': 'static-top-names part1'})
for i in mf_ul:
    req = i.find_all('a')
    for j in range(0, len(req)):
        male_first_names_list.append(req[j].get_text())

# Female First Names
female_first_names_list = []
ff_ul = ff_soup.find_all('ul', {'class': 'static-top-names part1'})
for k in ff_ul:
    res = k.find_all('a')
    for l in range(0, len(res)):
        female_first_names_list.append(res[l].get_text())

# Male Last Names and Female Last Names
male_female_last_names_list = []
mfl_p = mfl_soup.find_all(
    'p', {'class': 'article__paragraph article__paragraph--left'})
del mfl_p[:4]
mfl_p.pop(50)
for n in range(0, len(mfl_p)):
    male_female_last_names_list.append(mfl_p[n].get_text()[3:])

# Male Full Names
male_full_names_list = []
male_full_names_list.extend(male_first_names_list)
for p in range(0, len(male_first_names_list)):
    combination_one = random.randint(0, 49)
    male_full_names_list[p] += ' ' + \
        male_female_last_names_list[combination_one]
# Female Full Names
female_full_names_list = []
female_full_names_list.extend(female_first_names_list)
for q in range(0, len(female_first_names_list)):
    combination_two = random.randint(0, 49)
    female_full_names_list[q] += ' ' + \
        male_female_last_names_list[combination_two]

saved_names_list = []

# contains the appended tuples from the get() method of listbox
saved_fn_list_init = []
saved_fun_list_init = []
saved_ln_list_init = []

# contains the actual names that are entered under the respective categories
saved_fn_list = []
saved_fun_list = []
saved_ln_list = []


def search():
    list_box.delete(0, END)
    global gender
    gender = gender_select.get()
    global typee
    typee = type_select.get()

    # Generated Names
    global mfu_name
    mfu_name = random.choice(male_full_names_list)
    global mf_name
    mf_name = random.choice(male_first_names_list)
    global ffu_name
    ffu_name = random.choice(female_full_names_list)
    global ff_name
    ff_name = random.choice(female_first_names_list)
    global mfl_name
    mfl_name = random.choice(male_female_last_names_list)

    if gender == "Male" and typee == "Full Name":
        list_box.insert(1, mfu_name)
    elif gender == "Male" and typee == "First Name":
        list_box.insert(1, mf_name)
    elif gender == "Male" and typee == "Last Name":
        list_box.insert(1, mfl_name)

    elif gender == "Female" and typee == "Full Name":
        list_box.insert(1, ffu_name)
    elif gender == "Female" and typee == "First Name":
        list_box.insert(1, ff_name)
    elif gender == "Female" and typee == "Last Name":
        list_box.insert(1, mfl_name)
    else:
        messagebox.showerror("Error", "Enter All The Fields!")


def save_label():
    saved_label = Label(window, text="SAVED", bg="white",
                        fg="green", font=('Calibri', 15))
    saved_label.place(x=300, y=390)
    window.after(2000, saved_label.destroy)

    show_saved_btn = Button(window, text="Saved Names", command=saved_names)
    show_saved_btn.place(x=600, y=30)


def save(genderr, typeee):
    if genderr == "Male" and typeee == "Full Name":
        if mfu_name in saved_names_list:
            already_saved_label = Label(window, text="ALREADY SAVED", bg="white",
                                        fg="red", font=('Calibri', 15))
            already_saved_label.place(x=300, y=390)
            window.after(2000, already_saved_label.destroy)
        else:
            saved_names_list.append(mfu_name)
            save_label()
    elif genderr == "Male" and typeee == "First Name":
        if mf_name in saved_names_list:
            already_saved_label_2 = Label(window, text="ALREADY SAVED", bg="white",
                                          fg="red", font=('Calibri', 15))
            already_saved_label_2.place(x=300, y=390)
            window.after(2000, already_saved_label_2.destroy)
        else:
            saved_names_list.append(mf_name)
            save_label()
    elif genderr == "Male" and typeee == "Last Name":
        if mfl_name in saved_names_list:
            already_saved_label_3 = Label(window, text="ALREADY SAVED", bg="white",
                                          fg="red", font=('Calibri', 15))
            already_saved_label_3.place(x=300, y=390)
            window.after(2000, already_saved_label_3.destroy)
        else:
            saved_names_list.append(mfl_name)
            save_label()
    elif genderr == "Female" and typeee == "Full Name":
        if ffu_name in saved_names_list:
            already_saved_label_4 = Label(window, text="ALREADY SAVED", bg="white",
                                          fg="red", font=('Calibri', 15))
            already_saved_label_4.place(x=300, y=390)
            window.after(2000, already_saved_label_4.destroy)
        else:
            saved_names_list.append(ffu_name)
            save_label()
    elif genderr == "Female" and typeee == "First Name":
        if ff_name in saved_names_list:
            already_saved_label_5 = Label(window, text="ALREADY SAVED", bg="white",
                                          fg="red", font=('Calibri', 15))
            already_saved_label_5.place(x=300, y=390)
            window.after(2000, already_saved_label_5.destroy)
        else:
            saved_names_list.append(ff_name)
            save_label()
    elif genderr == "Female" and typeee == "Last Name":
        if mfl_name in saved_names_list:
            already_saved_label_6 = Label(window, text="ALREADY SAVED", bg="white",
                                          fg="red", font=('Calibri', 15))
            already_saved_label_6.place(x=300, y=390)
            window.after(2000, already_saved_label_6.destroy)
        else:
            saved_names_list.append(mfl_name)
            save_label()


file_count = -1


def text_file():
    '''
    Only the last element(tuple) of the list contains all the names that are saved, the previous tuples contain these names in a 
    sequential order, which is not desired. So, only the last tuple of the list is needed.
    '''
    if len(saved_fn_list_init) > 1 or len(saved_ln_list_init) > 1 or len(saved_fun_list_init) > 1:
        del saved_fn_list_init[:len(saved_fn_list_init)-1]
        del saved_ln_list_init[:len(saved_ln_list_init)-1]
        del saved_fun_list_init[:len(saved_fun_list_init)-1]

    # Traversing the tuples inside the lists to get the names
    for i in saved_fn_list_init:
        for j in i:
            saved_fn_list.append(j)

    for k in saved_ln_list_init:
        for m in k:
            saved_ln_list.append(m)

    for n in saved_fun_list_init:
        for p in n:
            saved_fun_list.append(p)

    global file_count
    file_count += 1
    # Saves the text file in the Desktop of any user (works in any computer!)
    user = os.getlogin()
    os.chdir(f"C:\\Users\\{user}\\Desktop")
    if f"names_{file_count}.txt" in os.listdir():
        with open(f"names_{file_count+1}.txt", "w") as f2:
            f2.write("----FIRST NAMES----\n\n")
            if len(saved_fn_list_init) == 0:
                f2.write(2*"\n")
            else:
                for z in range(0, len(saved_fn_list)):
                    f2.write(f"{1+z}. {saved_fn_list[z]}\n\n\n")
            f2.write("----LAST NAMES----\n\n")
            if len(saved_ln_list_init) == 0:
                f2.write(2*"\n")
            else:
                for x in range(0, len(saved_ln_list)):
                    f2.write(f"{1+x}. {saved_ln_list[x]}\n\n\n")
            f2.write("----FULL NAMES----\n\n")
            if len(saved_fun_list_init) == 0:
                f2.write(2*"\n")
            else:
                for w in range(0, len(saved_fun_list)):
                    f2.write(f"{1+w}. {saved_fun_list[w]}\n\n\n")
        messagebox.showinfo(
            "Success", "A New Text is File Created at Desktop !!")
    else:
        with open("names_1.txt", "w") as f:
            f.write("----FIRST NAMES----\n\n")
            if len(saved_fn_list_init) == 0:
                f.write(2*"\n")
            else:
                for g in range(0, len(saved_fn_list)):
                    f.write(f"{1+g}. {saved_fn_list[g]}\n\n\n")

            f.write("----LAST NAMES----\n\n")
            if len(saved_ln_list_init) == 0:
                f.write(2*'\n')
            else:
                for h in range(0, len(saved_ln_list)):
                    f.write(f"{1+h}. {saved_ln_list[h]}\n\n\n")
            f.write("----FULL NAMES----\n\n")
            if len(saved_fun_list_init) == 0:
                f.write(2*"\n")
            else:
                for a in range(0, len(saved_fun_list)):
                    f.write(f"{1+a}. {saved_fun_list[a]}\n\n\n")

        # These lists have to be cleared in order for the 2nd,3rd files..etc to be created and written properly.
        # If not done, the names saved in the 1st text file that's created will be carried over to the next files that are created.
        saved_fn_list.clear()
        saved_ln_list.clear()
        saved_fun_list.clear()
        messagebox.showinfo("Success", "Text File Created at Desktop !!")


def saved_names():
    global screen
    screen = Tk()
    screen.geometry("450x400")
    screen.title("Saved Names")
    screen.configure(bg="light green")
    global li_box_fn
    global li_box_ln
    global li_box_fun

    first_names_label = Label(screen, text="First Names", font=(
        'Calibri', 15), fg="black", bg="light green")
    first_names_label.place(x=0, y=100)

    li_box_fn = Listbox(screen, height=30, width=12,
                        font=('Calibri', 13), fg="black", bg="light green")
    li_box_fn.place(x=0, y=150)

    last_names_label = Label(screen, text="Last Names", font=(
        'Calibri', 15), fg="black", bg="light green")
    last_names_label.place(x=150, y=100)

    li_box_ln = Listbox(screen, height=30, width=12,
                        font=('Calibri', 13), fg="black", bg="light green")
    li_box_ln.place(x=150, y=150)

    full_names_label = Label(screen, text="Full Names", font=(
        'Calibri', 15), fg="black", bg="light green")
    full_names_label.place(x=280, y=100)

    li_box_fun = Listbox(screen, height=30, width=18,
                         font=('Calibri', 13), fg="black", bg="light green")
    li_box_fun.place(x=280, y=150)
    heading = Label(screen, text="YOUR SAVED NAMES", fg="black",
                    bg="light green", font=('Times New Roman', 18))
    heading.place(x=15, y=30)

    for t in range(0, len(saved_names_list)):
        if saved_names_list[t] in male_first_names_list or saved_names_list[t] in female_first_names_list:
            li_box_fn.insert(t, saved_names_list[t])
            saved_fn_list_init.append(li_box_fn.get(0, li_box_fn.size()))

        if saved_names_list[t] in male_female_last_names_list:
            li_box_ln.insert(t, saved_names_list[t])
            saved_ln_list_init.append(li_box_ln.get(0, li_box_ln.size()))

        if saved_names_list[t] in male_full_names_list or saved_names_list[t] in female_full_names_list:
            li_box_fun.insert(t, saved_names_list[t])
            saved_fun_list_init.append(li_box_fun.get(0, li_box_fun.size()))

    save_as_txt = Button(screen, text="Save As Txt File",
                         fg="blue", bg="white", font=('Calibri', 11), command=text_file)
    save_as_txt.place(x=300, y=30)

    clear_list = Button(screen, text="Clear", bg="red",
                        fg="white", width=14, command=clear_saved_list_box)
    clear_list.place(x=300, y=65)


def clear_saved_list_box():
    li_box_fn.delete(0, END)
    li_box_fun.delete(0, END)
    li_box_ln.delete(0, END)
    saved_names_list.clear()


def clear_search_list_box():
    list_box.delete(0, END)


def main_screen():
    global window
    window = Tk()
    window.title("Names Generator")
    window.configure(bg="light blue")
    window.geometry("700x500")

    global gender_select
    gender_select = StringVar()

    global type_select
    type_select = StringVar()

    title_label = Label(window, text="NAME GENERATOR",
                        fg="black", bg="light blue", font=("Times New Roman", 18))
    title_label.place(x=250, y=30)

    gender_label = Label(window, text="Gender:",
                         bg="light blue", fg="black", font=("Calibri", 15))
    gender_label.place(x=50, y=150)

    gender_entry = OptionMenu(window, gender_select, "Male", "Female")
    gender_entry.place(x=60, y=180)

    type_label = Label(window, text="Choose The Type:",
                       bg="light blue", fg="black", font=("Calibri", 15))
    type_label.place(x=250, y=150)

    type_entry = OptionMenu(window, type_select,
                            "Full Name", "First Name", "Last Name")
    type_entry.place(x=275, y=180)

    search_button = Button(window, text="SEARCH", fg="black", command=search)
    search_button.place(x=500, y=180)

    global list_box
    list_box = Listbox(window, height=1, width=18, font=("Verdena", 12))
    list_box.place(x=235, y=240)

    save_button = Button(window, text="Save This Name",
                         bg="light pink", command=lambda: save(gender, typee))
    save_button.place(x=450, y=240)

    clear_button = Button(window, text="Clear", fg="white",
                          bg="red", width=12, command=clear_search_list_box)
    clear_button.place(x=452, y=280)

    window.mainloop()


main_screen()
