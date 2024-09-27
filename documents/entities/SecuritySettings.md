## SecuritySettings Entity 
 
### Definition 
The  SecuritySettings  entity manages security-related settings for each user, such as login attempts and account status. 
 
### Attributes 
 
- **id**:  
  - Type:  int  
  - Description: Unique identifier for the security settings. 
 
- **user_id**:  
  - Type:  int  
  - Description: Reference to the associated user. 
 
- **failed_attempts**:  
  - Type:  int  
  - Description: Number of failed login attempts. 
 
- **is_locked**:  
  - Type:  boolean  
  - Description: Indicates whether the user account is locked. 
 
- **lock_date**:  
  - Type:  datetime  
  - Description: The date and time when the account was locked. 
 
### Example of SecuritySettings Entity in JSON Format
{
  "id": 1,
  "user_id": 1,
  "failed_attempts": 3,
  "is_locked": true,
  "lock_date": "2023-10-01T12:00:00Z"
}