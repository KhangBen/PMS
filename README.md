# Parking Management System (PMS)

## Overview
This project uses YOLOv8 and OpenCV to detect and track vehicles in a parking lot video.  
It determines parking spot occupancy and displays availability through a web-based dashboard.

---

## Features
- Vehicle detection using YOLOv8  
- Parking spot occupancy detection  
- Real-time data updates (via JSON)  
- Map view with visual parking layout  
- List view with availability and occupancy percentage  
- System status indicator (Active / Offline)  

---

## Getting Started

**1. Clone the Repository**
```bash
git clone https://github.com/KhangBen/PMS.git
cd PMS
```

**2. Create Virtual Environment**

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### MacOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

> Note: To exit the virtual environment at any time, run:  
```bash
(venv) deactivate
````

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the Program**  
This system requires running **two components at the same time**:
- the detection system ('main.py')
- the web server ('app.py')

#### 4.1 – Start Detection System 

#### Windows
```bash
python src/main.py
```

#### MacOS / Linux
```bash
python3 src/main.py
```

#### 4.2 – Start Web Server (in a new terminal/cmd)
Open a **second terminal window** and run:

#### Windows
```bash
python src/app.py
```

#### MacOS / Linux
```bash
python3 src/app.py
```

#### 4.3 – Open the Application
Go to the following URL in your browser:
```bash
http://127.0.0.1:5000/
```
> Note: The detection system (`main.py`) must also be running for live updates.

---

#### Usage
#### List View  
- Display total spaces available  
- Shows percentage of occupancy  
- Includes sustem status and last updated time  

#### Map View
- Visual layout of parking spots  
- Green = available 
- Red = occupied  
- Each spot labeled (P1,P2, etc.)  

---

#### Known Limitations  
- Uses pre-recorded video instead of live camera feed  
- Detection accuracy depends on camera angle  
- JSON is used instead of a database (for simplicity)  
- Currently support a single parking lot  

---

#### Future Improvements  
- Live camera integration  
- Multi-lot support  
- Database integration  
- Mobile-friendly UI  
- Improved detection accuracy  

---

#### Technologies Used  
- Python  
- OpenCV  
- YOLOv8 (Ultralytics)  
- Flask  
- HTML / CSS / JavaScript  

---

## Troubleshoting

### Reset localhost connection (Chrome)  
If the UI is not updated or appears stuck, you may need to clear Chrome socket connections:  

1. Go to:  
```bash
chrome://net-internals/#sockets
```

2. Click:  
- "Flush socket pools"  

3. Retry:
```bash
http://127.0.0.1:5000/
```
> Note: The detection system (`main.py`) must also be running for live updates.

