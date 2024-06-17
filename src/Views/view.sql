
CREATE VIEW FamilyMembers AS
SELECT health_insurance_card_no, first_name, last_name
FROM family_member_details
WHERE health_insurance_card_no = (
    SELECT expiry_date_of_card
    FROM family_health_insurance_card_details
    WHERE first_name = 'George'
);

SELECT * FROM FamilyMembers;
