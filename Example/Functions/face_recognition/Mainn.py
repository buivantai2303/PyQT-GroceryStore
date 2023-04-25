import random
import tkinter as tk


class RandomNumberGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Number Generator")
        self.master.geometry("300x150")

        self.random_number = tk.StringVar()
        self.random_number.set("00000")

        self.label = tk.Label(self.master, textvariable=self.random_number, font=("Arial", 32))
        self.label.pack(pady=10)

        self.button = tk.Button(self.master, text="Quay số", command=self.generate_random_number)
        self.button.pack(pady=10)

    def generate_random_number(self):
        number = random.randint(0, 99999)
        self.random_number.set(str(number).zfill(5))


if __name__ == "__main__":
    root = tk.Tk()
    app = RandomNumberGenerator(root)
    root.mainloop()
