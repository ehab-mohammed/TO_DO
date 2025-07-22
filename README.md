this project automates the process of testing a To-Do web application using Selenium and Behave (BDD) in Python.

It covers the following scenarios:

User login

Add a new task

Mark a task as completed

Delete a task

Python	Programming language
Behave	BDD Framework (Given-When-Then syntax)
Selenium	Web UI Automation
ChromeDriver	To control the Chrome browser
Git	Version control system

-project structure
TO_DO/
├── features/              
│   ├── todo.feature
│   ├── ...
│   └── steps/
│       └── step_definitions.py
├── manualtesting/         
│   ├── D01-Test_Strategy.pdf
│   ├── D02-SIGN IN.pdf
│   ├── D02-SIGN UP.pdf
│   ├── D04-TO DO.pdf
│   └── D05-BUG REPORTS.pdf
├── README.md              
├── requirements.txt      
└── .gitignore            


 Assumptions Made
A valid test account is already created:
Email: starlink@example.com
Password: ana01220@STAR
internet connection is stable to run test

-steps to run in the terminal
1-pip install -r requirements.txt
2-venv\Scripts\activate  # Windows
3-type behave
