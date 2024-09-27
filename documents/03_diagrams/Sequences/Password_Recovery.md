```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant Database
    participant Email

    User->>Frontend: Accesses the password recovery page
    Frontend->>User: Displays recovery form
    User->>Frontend: Enters email
    Frontend->>Backend: Sends recovery request
    Backend->>Database: Checks if the email exists
    Database-->>Backend: Returns result
    alt Email exists
        Backend->>Database: Generates recovery code
        Database-->>Backend: Confirms generation
        Backend->>Email: Sends recovery code
        Email-->>Backend: Confirms sending
        Backend->>Frontend: Sends success message
        Frontend->>User: Displays success message
    else Email does not exist
        Backend->>Frontend: Sends error for email not found
        Frontend->>User: Displays error message
    end
    ```