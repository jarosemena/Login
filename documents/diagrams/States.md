```mermaid
stateDiagram-v2
    [*] --> Registered
    Registered --> LoggedIn : Login
    LoggedIn --> LoggedOut : Logout
    LoggedOut --> LoggedIn : Login
    LoggedIn --> PasswordReset : Request Password Reset
    PasswordReset --> LoggedOut : Reset Password
    PasswordReset --> LoggedIn : Cancel Reset
    LoggedOut --> Registered : Register

    ```