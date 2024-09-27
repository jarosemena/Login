```mermaid
sequenceDiagram
    participant Admin
    participant Frontend
    participant Backend
    participant Database

    Admin->>Frontend: Accesses the roles management page
    Frontend->>Admin: Displays roles list and management options
    Admin->>Frontend: Chooses to create a new role
    Frontend->>Admin: Displays form for new role
    Admin->>Frontend: Fills out the form and submits
    Frontend->>Backend: Sends new role data
    Backend->>Database: Validates and creates new role
    Database-->>Backend: Confirms creation
    Backend->>Frontend: Sends success message
    Frontend->>Admin: Displays success notification

    Admin->>Frontend: Chooses to edit an existing role
    Frontend->>Admin: Displays form for editing role
    Admin->>Frontend: Modifies the role and submits
    Frontend->>Backend: Sends updated role data
    Backend->>Database: Validates and updates role
    Database-->>Backend: Confirms update
    Backend->>Frontend: Sends success message
    Frontend->>Admin: Displays success notification

    Admin->>Frontend: Chooses to delete a role
    Frontend->>Admin: Confirms deletion
    Admin->>Frontend: Confirms deletion
    Frontend->>Backend: Sends delete request for the role
    Backend->>Database: Deletes the role
    Database-->>Backend: Confirms deletion
    Backend->>Frontend: Sends success message
    Frontend->>Admin: Displays success notification
    ```