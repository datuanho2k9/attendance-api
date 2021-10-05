# Attendance-API
Simple API to mark students Attendance.\
You need Python, with Flask installed to use this. 
## How to run 
1. `git clone https://github.com/datuanho2k9/attendance-api.git` to clone the repo 2
2. `cd attendance-api` 
3. `mkdir Database/Classes` to create the database for JSON files 
4. `python3 main.py` to run the file 
## How to use 
### /attend, `POST` 
Mark a student attendance, expected headers with `Content-Type: application/json` with the following data: 
```json 
{ 
    "class-id": "string", 
    "student-id": "string" 
} 
``` 
All expected responses: 
```json 
{
    "status": 200,
    "message": "Attended {student-id} in {class-id}" ,
    "data": null
}
``` 
```json
{
    "status": 300,
    "message": "Student {student-id} is already attended in {class-id}",
    "data": null,
}
```
```json
{
    "status": 200,
    "message": "Student {student-id} is added as attended in {class-id}",
    "data": null
}
```
If the `POST` body is not in JSON, or no `Content-Type:application/json` on headers will result in JSON decode error, or `status:500`.
### /attendance/**class-id**, `GET` 
Get students has attended in class **class-id**.\
All expected responses:
```json
{
    "status": 400, 
    "message": "Class doesn't exist", 
    "data": null
}
```
```json
{
    "status":200,
    "message": "Success fetching data for class {class-id}",
    "data": ["student-id"]
}
```
