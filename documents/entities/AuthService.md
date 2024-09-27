## AuthService Entity 
 
### Definition 
The  AuthService  entity represents third-party authentication services that can be used for user login, such as Google, Facebook, or Outlook. 
 
### Attributes 
 
- **id**:  
  - Type:  int  
  - Description: Unique identifier for the authentication service. 
 
- **name**:  
  - Type:  string  
  - Description: The name of the authentication service (e.g., "Google", "Facebook"). 
 
- **user_id**:  
  - Type:  int  
  - Description: Reference to the associated user (if applicable). 
 
### Example of AuthService Entity in JSON Format
{
  "id": 1,
  "name": "Google",
  "user_id": 1
}