# Sector 21 - Authorization System

## Features
- Multi-layer authentication (Digi-code + S-code)
- Agent data management
- Admin control panel
- Helpdesk system (Tkinter UI)

##  Technologies Used
- Python
- MySQL
- Tkinter
- Tabulate

## Setup Instructions

### 1. Install dependencies
pip install -r requirements.txt

### 2. Setup MySQL Database
- Open MySQL Workbench
- Run `schema.sql`
- Then run `sample_data.sql`

### 3. Set Environment Variable
setx DB_PASSWORD "your_password"

### 4. Run the Project
python main.py



##  Note

1. S-CODE = awr420

2. Digicode = 
		Second last digit from the generated code.
		[If system generated = 78526341 then Digicode  = 4]

Database password is not included for security reasons.
