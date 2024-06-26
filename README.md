# Mission Statement

```psql
To provide secure, accessible, and accurate family medical information to enhance patient care and health outcomes.
```

# Mission Objectives

```psql

Establish and maintain detailed family medical records, capturing all medical visits, diagnoses, and treatments.

Ensure every family member has an up-to-date health insurance record, including coverage details and expiry dates.

Implement regular and thorough yearly check-ups for all family members, to monitor and promote long-term health.

Develop a robust network of healthcare professionals, 

specializing in various medical fields across affiliated hospitals.

Maintain accurate records of children's vaccinations and health check-ups.

Ensure comprehensive and accurate documentation of family member details, facilitating personalized healthcare and seamless family support.

```

# Instructions to run program

####  Create Database and schema
- Open terminal.
- Change current working directory into ```src``` folder.
  example :- 
```  ~/Desktop/Family_medical_info_db/src```
- Run following commands.

    ``` psql
    cd src
    cd Create
    psql -U postgres
    \i create_db.sql
    \q
    ```

#### Setup virtual environment

```psql
cd ..
cd ..
python3 -m venv .venv --prompt family
source .venv/bin/activate 
```
#### Install psycopg library

```psql
pip install psycopg
pip show psycopg
```

#### Set up connection pooling with psycopg
```psql
pip install psycopg[binary,pool]
```
#### Install prettytable and colorama
```psql
pip install prettytable

pip install colorama
```

#### Insert health insurance card details

- copy below commands and run one by one in terminal with your data

```psql
python3 -m src.main --health_insurance_card_no HIC123 --expiry_date_of_card 2026/07/12

python3 -m src.main --health_insurance_card_no HIC623 --expiry_date_of_card 2030/12/17

python3 -m src.main --health_insurance_card_no HIC523 --expiry_date_of_card 2035/07/22

python3 -m src.main --health_insurance_card_no HIC723 --expiry_date_of_card 2038/08/13
```

``` The expiry date of the health insurance card should not be from last year; it should be for a future year```

#### insert family member details

- copy below command and run one by one in terminal with your data

```psql
python3 -m src.Insert.insert_family_member --health_insurance_card_no HIC123 --first_name George --last_name Doe --age 66 --relation Father --gender M --marital_status Married --profession Engineer --contact_no 1234567890

python3 -m src.Insert.insert_family_member --health_insurance_card_no HIC623 --first_name Shiny --last_name George --age 55 --relation Mother --gender F --marital_status Married --profession "Home maker" --contact_no 13467890

python3 -m src.Insert.insert_family_member --health_insurance_card_no HIC523 --first_name Anila --last_name Jacob --age 25 --relation Sister --gender F --marital_status Married --profession "Civil Engineer" --contact_no 7234567890

python3 -m src.Insert.insert_family_member --health_insurance_card_no HIC723 --first_name John --last_name Doe --age 35 --relation Brother --gender M --marital_status Married --profession "Buisness" --contact_no 72784567890
```
``` The health insurance card number and first name must be provided```

#### Available options to select for marital status are:- Single, Married, Divorced, Widowed, Separated, Committed and Other


#### If you want to skip any field, for example, if the last name is empty, then you can skip --last_name.
```psql
python3 -m src.Insert.insert_family_member --health_insurance_card_no HIC222 --first_name Rose --age 23 --relation Father --gender F --marital_status Single --profession Student --contact_no 123456789
```

#### Insert Hospital Details

- copy below command and run one by one in terminal with your data

```psql
python3 -m src.Insert.insert_hospital_details --hospital_name "Appollo Hospital" --location Hamburg --address "Schmalenbecker 28" --contact_number "+1234567890" --website "http://hospitalappolo.com" --registration_fees 100.00

python3 -m src.Insert.insert_hospital_details --hospital_name "We Care Hospital" --location Berlin --address "Paulstraße 55" --contact_number "+1834597890" --website "http://wecarehospital.com" --registration_fees 150.00

python3 -m src.Insert.insert_hospital_details --hospital_name "Take Care Hospital" --location Munich --address "rollstraße 85" --contact_number "+187797890" --website "http://takecarehospital.com" --registration_fees 100.00

```

```The hospital name must be provided.```
```Multiple hospital can have same name.But hospial name and address should be unique```

#### Insert Doctor Details

- copy below command and run one by one in terminal with your data

```psql

python3 -m src.Insert.insert_doctor_details --hospital_id 1 --department Physician --doctor_name "Dr.Paul Issac" --gender M --availability_days "Monday Tuesday Friday" --consultation_hours '[{"Monday": "09:00 to 18:00"}, {"Tuesday": "10:00 to 17:00"}, {"Friday": "09:00 to 15:00"}]' --contact_no "+1112223344"

python3 -m src.Insert.insert_doctor_details --hospital_id 2 --department Cardiology --doctor_name "Dr.Johnson" --gender M --availability_days "Monday Friday" --consultation_hours '[{"Monday": "09:00 to 18:00"}, {"Friday": "10:00 to 17:00"}]' --contact_no "+1912223344"

python3 -m src.Insert.insert_doctor_details --hospital_id 1 --department Physiotherapy --doctor_name "Dr.Clara" --gender F --availability_days "Monday Tuesday Friday" --consultation_hours '[{"Monday": "08:00 to 18:00"}, {"Tuesday": "10:00 to 17:00"}, {"Friday": "10:00 to 15:00"}]' --contact_no "+10912223344"

python3 -m src.Insert.insert_doctor_details --hospital_id 3 --department Neurology --doctor_name "Dr.Sara Issac" --gender F --availability_days "Monday Tuesday Friday" --consultation_hours '[{"Monday": "09:00 to 18:00"}, {"Tuesday": "10:00 to 17:00"}, {"Friday": "09:00 to 15:00"}]' --contact_no "+1678223344"


```

```The hospital id, department, doctor name  must be provided```

``` You cannot add doctor details whose hospital id is not present in the hospital details```

#### Insert family yearly check up details

- copy below commands and run one by one in terminal with your data

```psql
python3 -m src.Insert.insert_yearly_check --health_insurance_card_no HIC123 --yearly_check_up_done "yes" --date_of_check_up "2024-02-03" 

python3 -m src.Insert.insert_yearly_check --health_insurance_card_no HIC623 --yearly_check_up_done "no" 

python3 -m src.Insert.insert_yearly_check --health_insurance_card_no HIC523 --yearly_check_up_done "yes" --date_of_check_up "2024-05-23" 

python3 -m src.Insert.insert_yearly_check --health_insurance_card_no HIC723 --yearly_check_up_done "no" 

```

```The health insurance card number must be provided```

#### Insert Children Check Up Details

- copy below command and run in terminal with your data

```psql
python3 -m src.Insert.insert_children_check     --health_insurance_card_no HIC723     --parents_name "Anila Jacob"     --number_of_children 2     --children_name_and_age '[{"name": "Sam", "age": 5}, {"name": "Bob", "age": 8}]'     --vaccination_details '[{"name":"Sam","completed":"yes"},{"name":"Bob","completed":"no"}]'     --date_of_vaccination '[{"name":"Sam","date": "2024-03-15"}]'     --vaccination_name "Varicella"
```
``` --health_insurance_card_no is (Parent's card number) must be provided ```
```Date of vaccination cannot be future date```


#### Insert family medical details

- copy below command and run in terminal with your data

```psql
python3 -m src.Insert.insert_family_medical --health_insurance_card_no HIC123 --doctor_id 1 --hospital_id 1 --department Physician --date_of_visit "2024-06-10 15:30" --symptoms "Cough Running nose" --diagnosis "Viral  Infection" --medication "Antibiotics Cough syrup"

python3 -m src.Insert.insert_family_medical --health_insurance_card_no HIC623 --doctor_id 3 --hospital_id 1 --department Physiotherapy --date_of_visit "2024-02-22 10:30" --symptoms "Leg pain" --diagnosis "Leg Sprain" --medication "Exercises Pain oinment"

python3 -m src.Insert.insert_family_medical --health_insurance_card_no HIC123 --doctor_id 2 --hospital_id 2 --department Cardiology --date_of_visit "2024-03-15 10:30" --symptoms "Chest pain" --diagnosis "Chest Infection" --medication "ECG scanning"

python3 -m src.Insert.insert_family_medical --health_insurance_card_no HIC523 --doctor_id 4 --hospital_id 3 --department Neurology --date_of_visit "2024-04-18 10:30" --symptoms "Headache" --diagnosis "Migraine" --medication "Sumatriptin"
```


```The health insurance card number, doctor id, hospital id, department and date of visit must be provided```
```date_of_visit cannot be future date```

``` You cannot enter the data of a person whose health insurance card number does not exist in the family member details table. First, you need to add the member to the family member details table with the corresponding health insurance card number.```

#### Update availability_days and consultation_hours of doctor_details table
```psql
cd src
cd Update
psql -U postgres
\i update.sql
\q
cd ..
cd ..
```

#### Reset doctor_id and hospital_id to 1 in the doctor_details and hospital_details tables.

```psql
cd src
cd Reset
psql -U postgres
\i reset_table_id.sql
\q
cd ..
cd ..
```

#### Delete All Values Inserted Into Data Base Table
```psql
cd src
cd Truncate
psql -U postgres
\i truncate.sql
\q
cd ..
cd ..
```

#### Delete All Created Table, Schema and DataBase
```psql
cd src
cd Delete
\i delete.sql
\q
cd ..
cd ..
```


