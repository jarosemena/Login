```mermaid 
%%{init: {'theme': 'default'}}%%
graph TD
    A[User] -->|Submits registration form| B[Registration System]
    B -->|Validates input| C{Input Valid?}
    C -->|Yes| D[Create User Account]
    C -->|No| E[Show Error Message]
    D -->|Sends confirmation email| F[Email Service]
    F -->|Email Sent| G[Show Success Message]
    ```