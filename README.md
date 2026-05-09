# Parking Management System (PMS)
## Overview
This project uses YOLOv8 and OpenCV to detect and track vehicles in a parking lot video. 

## Getting Started

**1. Clone the Repository**
```bash
git clone https://github.com/KhangBen/PMS.git
cd PMS
```

**2. Create Virtual Environment**

#### MacOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### deactivate venv environment
```bash
(venv) deactivate
````

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the Program**
This system requires running **two components at the same time**:
- the detection system ('main.py)
- the web server ('app.py)

---

#### Step 4.1 – Start Detection System 

### Windows
```bash
python src/main.py
```

#### MacOS / Linux
```bash
python3 src/main.py
```

#### Step 4.2 – Start Web Server (in a new terminal/cmd)
Open a **second terminal window** and run:

### Windows
```bash
python src/app.py
```

#### MacOS / Linux
```bash
python3 src/app.py
```

#### Step 4.3 – Open the Application
Go to the following URL in your browser:
```bash
http://127.0.0.1:5000/
```




