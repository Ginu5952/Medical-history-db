
DROP VIEW IF EXISTS FamilyMembers;



DROP TABLE family_health_insurance_card_details CASCADE;
DROP TABLE hospital_details CASCADE;
DROP TABLE doctor_details CASCADE;
DROP TABLE family_member_details CASCADE;
DROP TABLE children_check_up_details CASCADE;
DROP TABLE family_yearly_check_up_details CASCADE;
DROP TABLE family_medical_details CASCADE;



DROP SCHEMA family CASCADE;

\c postgres

DROP DATABASE family_medical_info;

