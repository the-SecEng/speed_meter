import tkinter as tk

class SpeedMeter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Digital Speed Meter")
        self.geometry("400x450")
        self.configure(bg="black")  # Set the window background to black

        self.canvas = tk.Canvas(self, width=400, height=400, bg="black", highlightthickness=0)
        self.canvas.pack()

        self.speed = tk.DoubleVar()
        self.speed.set(0)  # Initial speed

        self.transmission = tk.IntVar()
        self.transmission.set(1)  # Initial transmission

        self.velocity_label = tk.Label(self, text="0 km/h", bg="black", fg="white", font=("Helvetica", 36))
        self.velocity_label.place(relx=0.5, rely=0.5, anchor="center")

        self.transmission_label = tk.Label(
            self,
            text="1",
            bg="black",
            fg="#39FF14",
            font=("Helvetica", 18, "bold"),
            bd=2,
            relief="solid",
            highlightbackground="#C0C0C0",
            highlightcolor="#C0C0C0",
            padx=8,
            pady=4,  # Added padding to make the border more visible
        )
        self.transmission_label.place(relx=0.9, rely=0.02, anchor="ne")

        self.bind("<Up>", self.accelerate)
        self.bind("<Down>", self.decelerate)
        self.bind("<Shift-Up>", self.increase_transmission)
        self.bind("<Command-Down>", self.decrease_transmission)

        self.update_speed_meter()

    def accelerate(self, event):
        # Increase the speed when the up arrow key is pressed
        current_speed = self.speed.get()
        new_speed = min(current_speed + 5, 230)  # Limit speed to 230 km/h
        self.speed.set(new_speed)
        self.update_velocity_label()

    def decelerate(self, event):
        # Decrease the speed when the down arrow key is pressed
        current_speed = self.speed.get()
        new_speed = max(current_speed - 5, 0)  # Minimum speed is 0 km/h
        self.speed.set(new_speed)
        self.update_velocity_label()

    def increase_transmission(self, event):
        # Increase the transmission when the Shift key and Up arrow key are pressed
        current_transmission = self.transmission.get()
        new_transmission = min(current_transmission + 1, 5)  # Limit transmission to 5
        self.transmission.set(new_transmission)
        self.update_transmission_label()

    def decrease_transmission(self, event):
        # Decrease the transmission when the Cmd key and Down arrow key are pressed
        current_transmission = self.transmission.get()
        new_transmission = max(current_transmission - 1, 1)  # Minimum transmission is 1
        self.transmission.set(new_transmission)
        self.update_transmission_label()

    def update_velocity_label(self):
        # Update the velocity label based on the current speed
        velocity_text = f"{int(self.speed.get())} km/h"
        self.velocity_label.config(text=velocity_text)

    def update_transmission_label(self):
        # Update the transmission label based on the current transmission
        transmission_text = str(self.transmission.get())
        self.transmission_label.config(text=transmission_text)

    def update_speed_meter(self):
        # Update the speed meter every 100 milliseconds (adjust as needed)
        self.after(100, self.update_speed_meter)

if __name__ == "__main__":
    app = SpeedMeter()
    app.mainloop()
