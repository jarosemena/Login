```mermaid
graph TD
    A[Start] --> B[Access Dashboard]
    B --> C[Click Logout]
    C --> D[Invalidate JWT Token]
    D --> E[Redirect to Login Page]
    E --> F[End]
    ```