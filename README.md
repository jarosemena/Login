# Login
General Login to use like a microservice for all environments

---

# Login Application Project

## 1. Project Description

This project is a login application that allows user creation, password recovery, and authentication through third-party services such as Google, Facebook, and Outlook. The application is divided into two parts: a backend developed in Flask and a frontend in React using Material-UI.

## 2. Project Structure
/Login
│  
├── /backend 
│   ├── /app 
│   │   ├── /models            # Data models 
│   │   ├── /services          # Business logic 
│   │   ├── /controllers       # Controllers to handle requests 
│   │   ├── /repositories      # Data access 
│   │   ├── /routes            # API routes 
│   │   ├── /utils             # Utility functions 
│   │   └── /tests             # Unit tests 
│   │ 
│   ├── /migrations            # Database migrations 
│   ├── /requirements.txt      # Python dependencies 
│   └── app.py                 # Main application file 
│   
└── /frontend 
    ├── /src 
    │   ├── /components        # React components 
    │   ├── /pages             # Application pages 
    │   ├── /services          # API service calls 
    │   ├── /utils             # Utility functions 
    │   └── index.js           # Main React file 
    │   
    ├── package.json           # React dependencies 
    └── .env                   # Environment variables


## 3. Features

- **New User Registration**: Allows users to register via a form or authenticate using third-party services (Google, Facebook, Outlook).
- **Login**: Registered users can log in.
- **Password Recovery**: Users can recover their passwords via a code sent to their email.
- **JWT Authentication**: A JWT token is generated for user sessions.
- **Security**: Implements security measures to prevent common attacks such as SQL injections and brute force attacks.

## 4. Technologies Used

- **Backend**:
  - Flask
  - Flask-SQLAlchemy
  - Flask-Migrate
  - Flask-JWT-Extended
  - Flask-Mail
  - MySQL
  - Flask-WTF
  - Flask-Limiter
  - bcrypt
  - pytest

- **Frontend**:
  - React
  - Redux
  - Material-UI
  - Jest
  - React Testing Library

## 5. Installation

### Backend

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/my-project.git
   cd my-project/backend

2. Create and activate a virtual environment:
   ```bash
      python -m venv venv
      venv\Scripts\activate  # On Windows
      # source venv/bin/activate  # On macOS/Linux

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt

4. Set up the MySQL database and update app.py with your credentials.

5. Run the application:
   ```bash
   python app.py

### Frontend

1. Navigate to the frontend folder:
   ```bash
   cd ../frontend

2. Install the dependencies:  
   ```bash
   npm install

3. Run the application:
   ```bash
   npm start

## 6. Testing

### To run backend tests, make sure the virtual environment is activated and run:
pytest

### To run frontend tests, navigate to the frontend folder and run:
npm test

## 7. Contributions
Contributions are welcome. If you wish to contribute, please open an issue or submit a pull request.

## 8. License
This project is licensed under the MIT License. See the LICENSE file for more details.