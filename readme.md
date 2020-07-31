Full Throttle Assignment

Tech Stack :- Python, Django(Django_Rest_Framework)

SetUp :-
1. Clone the repository.
2. Install requirements - "pip install -r requirements.txt"
3. Create PostgreSQL database "FullThrottle"".
4. run "python manage.py make migrations".
5. run "python manage.py migrate".
6. run "python manage.py runserver". 

Details :-
1. The database contains two tables "Members" and "Activity_Periods"
2. Two APIs :-.
   i) localhost/members - to fetch details of all the members. 
   ii) localhost/activity_periods - to fetch all the stored activity_periods (ReadOnly API).
3. API "localhost/members/<int>" fetches details of members with "id" = <int>.
4. API "localhost/members/?real_name=ABC" fetches details of members with "real_name" = "ABC".
5. API "localhost/activity_periods/?real_name=ABC" fetches all the activities of member with "real_name" = "ABC".

Add Data:
1. Script - "scripts/add_data" to add data from CSV file.
 
