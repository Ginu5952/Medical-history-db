
UPDATE doctor_details
SET  availability_days = ARRAY['Monday', 'Wednesday', 'Friday']
WHERE hospital_id = 1 AND department = 'Physician';


UPDATE doctor_details
SET consultation_hours  = '[{"Monday": "09:00 to 18:00"}, {"Wednesday": "10:00 to 17:00"}, {"Friday": "09:00 to 15:00"}]'
WHERE hospital_id = 1 AND department = 'Physician';

SELECT * FROM doctor_details;