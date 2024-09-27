```mermaid 
%%{init: {'theme': 'default'}}%%
graph TD
    A[User] -->|Requests password recovery| B[Recovery System]
    B -->|Sends recovery email| C[Email Service]
    C -->|Email Sent| D[Show Recovery Success Message]
    A -->|Enters recovery code| E[Recovery Code Validation]
    E -->|Validates code| F{Code Valid?}
    F -->|Yes| G[Allows User to Set New Password]
    F -->|No| H[Show Invalid Code Message]
    ```