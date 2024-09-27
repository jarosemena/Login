### Definition 
The  AuthToken  entity represents a token generated for user authentication. This token is used to verify the user's identity during API requests. 
 
### Attributes 
 
- **id**:  
  - Type:  int  
  - Description: Unique identifier for the authentication token. 
 
- **user_id**:  
  - Type:  int  
  - Description: Reference to the associated user. 
 
- **token**:  
  - Type:  string  
  - Description: The JWT token generated for the user. 
 
- **created_at**:  
  - Type:  datetime  
  - Description: The date and time when the token was created. 
 
- **expiration_date**:  
  - Type:  datetime  
  - Description: The date and time when the token expires. 
 
### Example of AuthToken Entity in JSON Format
{
  "id": 1,
  "user_id": 1,
  "token": "jwt_token_string",
  "created_at": "2023-10-01T12:00:00Z",
  "expiration_date": "2023-10-01T13:00:00Z"
}