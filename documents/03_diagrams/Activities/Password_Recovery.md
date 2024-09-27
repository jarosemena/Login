```mermaid
graph TD
    A[Start] --> B[Access Password Reset Page]
    B --> C[Enter Email]
    C --> D[Submit Request]
    D --> E[Generate Reset Code]
    E --> F[Send Reset Code to Email]
    F --> G[Access Reset Code Page]
    G --> H[Enter Reset Code and New Password]
    H --> I[Submit New Password]
    I --> J[Validate Reset Code]
    J -->|Valid| K[Update Password]
    J -->|Invalid| L[Show Error Message]
    K --> M[Send Confirmation Email]
    M --> N[Redirect to Login Page]
    L --> G
    N --> O[End]
    ```