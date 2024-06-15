
SELECT 'CREATE DATABASE family_medical_info'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'family_medical_info')\gexec


\c family_medical_info

CREATE SCHEMA IF NOT EXISTS family;





