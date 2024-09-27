```mermaid
graph TD
    A[Start] --> B[Access Registration Page]
    B --> C[Fill Registration Form]
    C --> D[Submit Form]
    D --> E[Validate Data]
    E -->|Valid| F[Create User Account]
    E -->|Invalid| G[Show Error Message]
    F --> H[Send Confirmation Email]
    H --> I[Redirect to Login Page]
    G --> B
    I --> J[End]
    ```