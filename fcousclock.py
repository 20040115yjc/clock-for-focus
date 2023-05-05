import tkinter as tk
import time

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")
        
        self.time_remaining = 25 * 60 # 25 minutes in seconds
        self.is_running = False
        
        self.timer_label = tk.Label(self.master, text="25:00", font=("Helvetica", 48))
        self.timer_label.pack(pady=20)
        
        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=10)
        
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
    def start_timer(self):
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.NORMAL)
        self.countdown()
        
    def pause_timer(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        
    def reset_timer(self):
        self.is_running = False
        self.time_remaining = 25 * 60
        self.timer_label.config(text="25:00")
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
        
    def countdown(self):
        if self.is_running and self.time_remaining > 0:
            minutes, seconds = divmod(self.time_remaining, 60)
            self.timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.time_remaining -= 1
            self.master.after(1000, self.countdown)
        elif self.time_remaining == 0:
            self.timer_label.config(text="Time's up!")
            self.is_running = False
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.DISABLED)
            
if __name__ == "__main__":
    root = tk.Tk()
    timer = PomodoroTimer(root)
    root.mainloop()
