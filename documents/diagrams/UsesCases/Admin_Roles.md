```mermaid 
%%{init: {'theme': 'default'}}%%
graph TD
    A[Admin User] -->|Accesses administration view| B[Administration System]
    B -->|Selects Manage Roles| C[Display List of Roles]
    C --> D{Options}
    D -->|Create New Role| E[Create Role Form]
    E -->|Submits Role Details| F[Validate Input]
    F -->|Valid| G[Create New Role]
    G -->|Adds to List| C
    D -->|Update Existing Role| H[Select Role]
    H -->|Modify Role Details| I[Update Role Form]
    I -->|Submits Changes| F
    F -->|Valid| J[Update Role]
    J -->|Reflects Changes| C
    D -->|Delete Role| K[Select Role]
    K -->|Confirm Deletion| L[Delete Role]
    L -->|Removes from List| C
    D -->|Assign Roles to Users| M[Select Role]
    M -->|Display Users| N[Assign Users]
    N -->|Submits Assignments| O[Update User Roles]
    ```