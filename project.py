import tkinter as tk
from tkinter import messagebox
import random
import time
import threading

paused = False
stopped = False

def generate_random_sequence():
    try:
        num_elements = int(num_elements_var.get())
        if num_elements < 5 or num_elements > 100:
            messagebox.showerror("Eroare", "Numărul de elemente trebuie să fie între 5 și 100.")
            return
        random_sequence = [random.randint(10, 100) for _ in range(num_elements)]


        entry_numbers.delete(0, tk.END)
        entry_numbers.insert(0, " ".join(map(str, random_sequence)))


        draw_bars(random_sequence, ["blue"] * len(random_sequence))
    except ValueError:
        messagebox.showerror("Eroare", "Introduceti un numar valid de elemente.")



def visualize_sort(algorithm):
    global paused, stopped
    try:
        numbers = list(map(int, entry_numbers.get().split()))
        if not numbers:
            messagebox.showerror("Eroare", "Secvența este goală. Vă rugăm să introduceți numere.")
            return

        delay = speed_var.get() / 1000  

        canvas.delete("all")
        draw_bars(numbers, ["blue"] * len(numbers))

        if algorithm == "Bubble Sort":
            bubble_sort_visual(numbers, delay)
        elif algorithm == "Insertion Sort":
            insertion_sort_visual(numbers, delay)
        elif algorithm == "Selection Sort":
            selection_sort_visual(numbers, delay)
        else:
            messagebox.showerror("Eroare", "Selectați un algoritm de sortare.")
    except ValueError:
        messagebox.showerror("Eroare", "Introduceți o listă validă de numere separate prin spațiu.")

def draw_bars(arr, colors):
    canvas_height = 200
    canvas_width = 400


    if len(arr) == 0:
        return

    bar_width = canvas_width / len(arr)
    max_val = max(arr)

    for i, value in enumerate(arr):
        x0 = i * bar_width
        y0 = canvas_height - (value / max_val) * canvas_height
        x1 = (i + 1) * bar_width
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i])
        canvas.create_text((x0 + x1) // 2, y0 - 10, text=str(value), font=("Arial", 10))

def bubble_sort_visual(arr, delay):
    global paused, stopped
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if stopped:
                return
            while paused:
                time.sleep(0.1)
            draw_bars(arr, ["red" if x == j or x == j + 1 else "blue" for x in range(len(arr))])
            canvas.update()
            time.sleep(delay)

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                draw_bars(arr, ["yellow" if x == j or x == j + 1 else "blue" for x in range(len(arr))])
                canvas.update()
                time.sleep(delay)

            draw_bars(arr, ["green" if x <= i else "blue" for x in range(len(arr))])
            canvas.update()
            time.sleep(delay)
    draw_bars(arr, ["green"] * len(arr))


def insertion_sort_visual(arr, delay):
    global paused, stopped
    for i in range(1, len(arr)):
        if stopped:
            return
        while paused:
            time.sleep(0.1)
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            draw_bars(arr, ["red" if x == j or x == j + 1 else "blue" for x in range(len(arr))])
            canvas.update()
            time.sleep(delay)

            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        draw_bars(arr, ["green" if x <= i else "blue" for x in range(len(arr))])
        canvas.update()
        time.sleep(delay)
    draw_bars(arr, ["green"] * len(arr))


def selection_sort_visual(arr, delay):
    global paused, stopped
    for i in range(len(arr)):
        if stopped:
            return
        while paused:
            time.sleep(0.1)
        min_idx = i
        for j in range(i + 1, len(arr)):
            draw_bars(arr, ["red" if x == j or x == min_idx else "blue" for x in range(len(arr))])
            canvas.update()
            time.sleep(delay)

            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_bars(arr, ["green" if x <= i else "blue" for x in range(len(arr))])
        canvas.update()
        time.sleep(delay)
    draw_bars(arr, ["green"] * len(arr))

def reset_visualization():
    global paused, stopped
    paused = False
    stopped = False
    canvas.delete("all")
    entry_numbers.delete(0, tk.END)
    entry_numbers.insert(0, "")

def pause_sorting():
    global paused
    paused = not paused
    button_pause.config(text="Reia sortarea" if paused else "Pauză")


def stop_sorting():
    global stopped
    stopped = True
    reset_visualization()
    button_pause.config(text="Pauză")
    button_sort.config(state="normal")

def reset_all():
    global paused, stopped
    paused = False
    stopped = False
    entry_numbers.delete(0, tk.END)
    entry_numbers.insert(0, "")
    canvas.delete("all")
    num_elements_var.set("10")
    speed_var.set(500)
    button_pause.config(text="Pauză")
    button_sort.config(state="normal")

def exit_application():
    root.quit()

root = tk.Tk()
root.title("Selector de Algoritmi de Sortare cu Vizualizare")

label_num_elements = tk.Label(root, text="Număr de elemente (între 5 și 100):")
label_num_elements.pack(pady=5)

num_elements_var = tk.StringVar(value="10")
entry_num_elements = tk.Entry(root, textvariable=num_elements_var, width=10)
entry_num_elements.pack(pady=5)

label_numbers = tk.Label(root, text="Introduceți numerele de sortat (separate prin spațiu):")
label_numbers.pack(pady=5)

entry_numbers = tk.Entry(root, width=40)
entry_numbers.pack(pady=5)

label_algorithm = tk.Label(root, text="Selectați algoritmul de sortare:")
label_algorithm.pack(pady=5)

algorithm_var = tk.StringVar(value="Bubble Sort")
radio_bubble = tk.Radiobutton(root, text="Bubble Sort", variable=algorithm_var, value="Bubble Sort")
radio_bubble.pack(anchor="w", padx=20)

radio_insertion = tk.Radiobutton(root, text="Insertion Sort", variable=algorithm_var, value="Insertion Sort")
radio_insertion.pack(anchor="w", padx=20)

radio_selection = tk.Radiobutton(root, text="Selection Sort", variable=algorithm_var, value="Selection Sort")
radio_selection.pack(anchor="w", padx=20)

label_speed = tk.Label(root, text="Controlul vitezei:")
label_speed.pack(pady=5)

speed_var = tk.DoubleVar(value=500)
speed_scale = tk.Scale(root, from_=50, to=2000, orient="horizontal", variable=speed_var, label="Viteză (ms)")
speed_scale.pack(pady=5)

button_generate = tk.Button(root, text="Generează secvență aleatorie", command=generate_random_sequence)
button_generate.pack(pady=5)

canvas = tk.Canvas(root, width=400, height=200, bg="white")
canvas.pack(pady=10)

button_sort = tk.Button(root, text="Sortează cu Vizualizare", command=lambda: visualize_sort(algorithm_var.get()))
button_sort.pack(pady=10)

button_pause = tk.Button(root, text="Pauză", command=pause_sorting)
button_pause.pack(pady=5)

button_stop = tk.Button(root, text="Oprește", command=stop_sorting)
button_stop.pack(pady=5)

button_reset = tk.Button(root, text="Resetare completă", command=reset_all)
button_reset.pack(pady=5)

button_exit = tk.Button(root, text="Ieșire din aplicație", command=exit_application)
button_exit.pack(pady=5)

root.mainloop()

