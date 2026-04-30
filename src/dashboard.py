import tkinter as tk
import json
import os


class ParkingDashboard:

  def __init__(self, root):
    self.root = root
    self.root.title("PMS - Parking Map")
    self.root.geometry("800x600")

    self.spot_layout = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],                    # top row (far)
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
    [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32],
    [33, 34, 35, 36, 37, 38, 39, 40, 41]                # bottom row (close)
    ]


    # Labels for overall status
    self.status_label = tk.Label(root, text="Fetching data...", font=("Arial", 18))
    self.status_label.pack(pady=10)

    # Container for the parking spot grid
    self.grid_frame = tk.Frame(root)
    self.grid_frame.pack(pady=20)

    self.spot_rects = []
    self.update_ui()


  def update_ui(self):
    json_path = "lot_status.json"

    if os.path.exists(json_path):
      try:
        with open(json_path, "r") as f:
          data = json.load(f)

          if not data.get("system_active", True):
            self.root.destroy()
            return


          # Update the total count
          self.status_label.config(
            text=f"Available Spots: {data['available']} / {data['total']}",
            fg = "darkgreen" if data['available'] > 0 else "red"
          )


          # Clear and redraw the grid 
          for widget in self.grid_frame.winfo_children():
            widget.destroy()

          for i in range(20):
            self.grid_frame.grid_rowconfigure(i, minsize=0)

          # Create visual blocks for each spot
          for r, row in enumerate(self.spot_layout):
            for c, spot_num in enumerate(row):
              
              if spot_num - 1 < len(data['spot_statuses']):
                occupied = data['spot_statuses'][spot_num - 1]
              else:
                occupied = False

              color = "red" if occupied else "green"

              label = tk.Label(self.grid_frame, text=f"P{spot_num}", bg=color, fg="white", width=6, height=3,
                               relief="raised", font=("Arial", 10, "bold"))
              
              label.grid(row=r * 2, column=c, padx=5, pady=10)
          
              self.grid_frame.grid_rowconfigure(r * 2 + 1, minsize=[40, 5, 40, 110][r])

      except Exception as e:
        print(f"Error reading JSON: {e}")

    # Refresh every 2 seconds to meet Performance Requirement
    self.root.after(2000, self.update_ui)

if __name__ == "__main__":
  root = tk.Tk()
  app = ParkingDashboard(root)
  root.mainloop()