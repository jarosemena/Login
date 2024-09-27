## PasswordResetCode Entity 
 
### Definition 
The  PasswordResetCode  entity represents a code sent to users for the purpose of resetting their passwords. 
 
### Attributes 
 
- **id**:  
  - Type:  int  
  - Description: Unique identifier for the password reset code. 
 
- **user_id**:  
  - Type:  int  
  - Description: Reference to the associated user. 
 
- **code**:  
  - Type:  string  
  - Description: The code sent to the user for password reset. 
 
- **created_at**:  
  - Type:  datetime  
  - Description: The date and time when the code was created. 
 
- **used**:  
  - Type:  boolean  
  - Description: Indicates whether the code has been used. 
 
### Example of PasswordResetCode Entity in JSON Format
{
  "id": 1,
  "user_id": 1,
  "code": "reset_code_string",
  "created_at": "2023-10-01T12:00:00Z",
  "used": false
}