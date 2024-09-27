```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant Database

    User->>Frontend: Accesses the registration page
    Frontend->>User: Displays registration form
    User->>Frontend: Fills out form and submits
    Frontend->>Backend: Sends registration data
    Backend->>Database: Checks if the email already exists
    Database-->>Backend: Returns result
    alt Email does not exist
        Backend->>Database: Creates new user
        Database-->>Backend: Confirms creation
        Backend->>Frontend: Sends registration confirmation
        Frontend->>User: Displays success message
    else Email already exists
        Backend->>Frontend: Sends error for existing email
        Frontend->>User: Displays error message
    end
    ```