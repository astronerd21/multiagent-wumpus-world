import tkinter as tk


class WumpusWorldApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiagent Wumpus World")
        self.root.geometry("600x400")

        # Placeholder label for the GUI
        self.label = tk.Label(
            root, text="Multiagent Wumpus World - Initial Setup", font=("Arial", 14)
        )
        self.label.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = WumpusWorldApp(root)
    root.mainloop()
