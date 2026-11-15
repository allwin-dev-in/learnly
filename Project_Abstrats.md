# Learnly | Learning Management System

## Project Overview



<!-- 
## TECHNICAL REQUIREMENTS
- Python
- Django
- Django REST Framework
- MySQL- Database
- JWT Authentication using Simple JWT
- Token Authentication
- Django ORM
- Model Serializers
- APIView or Generic Views
- Custom User Model
- Custom AUthentication -->

---

## Application Structure

    App Name        Responsibility
    --------------------------------
    Accounts        User Registration,Authentication
    Courses         Courses Management
    Student         Student Management

## Database Models

- Custom User Model - extend from Abstract User.

Additional fields:

    Fields          Data Type           Constraints
    ----------------------------------------------------
    Phone           CharField(12)       Unique,Required
    Role            CharField(Choices-  Required
                              Student,
                              Admin
                             )  

- Courses Model 
```
    Fields          Data Type           Constraints
    ---------------------------------------------------
    Id              AutoField           Primary Key
    Title           CharField           Course Title
    Description     TextField           Course Description
    Duration        CharField           Course Duration
    Language        CharField           Course Language
    Price           Decimal             Course Price
    Cover_Picture   ImageField          Cover Image
    Created_by      AutoField           FK(User)
    Created_at      AutoField           Auto_add_now=True
    Updated_at      AutoField           Auto_now=True
```
- Student Model
```
    Fields          Data Type           Constraints
    ---------------------------------------------------


```