
## UserRole Entity 
 
### Definition 
The  UserRole  entity serves as a join table to establish a many-to-many relationship between users and roles. 
 
### Attributes 
 
- **id**:  
  - Type:  int  
  - Description: Unique identifier for the user-role association. 
 
- **user_id**:  
  - Type:  int  
  - Description: Reference to the associated user. 
 
- **role_id**:  
  - Type:  int  
  - Description: Reference to the associated role. 
 
### Example of UserRole Entity in JSON Format
{
  "id": 1,
  "user_id": 1,
  "role_id": 1
}