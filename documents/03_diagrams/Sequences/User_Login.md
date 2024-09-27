```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant Database

    User->>Frontend: Accesses the login page
    Frontend->>User: Displays login form
    User->>Frontend: Enters email and password
    Frontend->>Backend: Sends credentials
    Backend->>Database: Verifies credentials
    Database-->>Backend: Returns result
    alt Valid credentials
        Backend->>Frontend: Sends JWT token
        Frontend->>User: Redirects to main page
    else Invalid credentials
        Backend->>Frontend: Sends error for invalid credentials
        Frontend->>User: Displays error message
    end
    ```