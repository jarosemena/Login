### Definition 
The  User  entity represents an individual who can access the application. Each user has unique credentials and may belong to one or more roles. 
 
### Attributes 
 
- **id**:  
  - Type:  int  
  - Description: Unique identifier for the user. 
 
- **first_name**:  
  - Type:  string  
  - Description: The first name of the user. 
 
- **last_name**:  
  - Type:  string  
  - Description: The last name of the user. 
 
- **email**:  
  - Type:  string  
  - Description: The email address of the user (must be unique). 
 
- **password_hash**:  
  - Type:  string  
  - Description: The hashed password for the user's account. 
 
- **created_at**:  
  - Type:  datetime  
  - Description: The date and time when the user account was created. 
 
- **last_login**:  
  - Type:  datetime  
  - Description: The date and time when the user last logged in. 
 
- **authentication_method**:  
  - Type:  string  
  - Description: The method of authentication (e.g., local, Google, Facebook). 
 
### Example of User Entity in JSON Format
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "password_hash": "hashed_password",
  "created_at": "2023-10-01T12:00:00Z",
  "last_login": "2023-10-15T15:30:00Z",
  "authentication_method": "local"
}