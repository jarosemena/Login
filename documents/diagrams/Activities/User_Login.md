```mermaid
graph TD
    A[Start] --> B[Access Login Page]
    B --> C[Enter Email and Password]
    C --> D[Submit Login]
    D --> E[Validate Credentials]
    E -->|Valid| F[Generate JWT Token]
    E -->|Invalid| G[Show Error Message]
    F --> H[Redirect to Dashboard]
    G --> B
    H --> I[End]
    ```