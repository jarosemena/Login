## ActivityLog Entity 
 
### Definition 
The  ActivityLog  entity records actions taken by users within the application for auditing and monitoring purposes. 
 
### Attributes 
 
- **id**:  
  - Type:  int  
  - Description: Unique identifier for the activity log entry. 
 
- **user_id**:  
  - Type:  int  
  - Description: Reference to the associated user. 
 
- **action**:  
  - Type:  string  
  - Description: Description of the action taken (e.g., "login", "password reset"). 
 
- **timestamp**:  
  - Type:  datetime  
  - Description: The date and time when the action occurred. 
 
### Example of ActivityLog Entity in JSON Format
{
  "id": 1,
  "user_id": 1,
  "action": "login",
  "timestamp": "2023-10-15T15:30:00Z"
}