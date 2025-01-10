-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Getting the description of the same date 28/07/2021
SELECT description FROM crime_scene_reports WHERE day = 28 AND month = 7 AND year = 2021;

-- Finding the transcript that matches the output of the previos query
SELECT transcript FROM interviews WHERE day = 28 AND month = 7 AND year = 2021 AND transcript LIKE '%bakery%';

-- Joining people and bakery_security_logs to get name, activity and license plate where they match by the license plate
SELECT bakery_security_logs.license_plate, bakery_security_logs.activity, people.name FROM people JOIN bakery_security_logs
ON bakery_security_logs.license_plate = people.license_plate WHERE bakery_security_logs.minute >= 15 AND bakery_security_logs.minute <= 25
AND bakery_security_logs.hour = 10
AND bakery_security_logs.day = 28
AND bakery_security_logs.month = 7
AND bakery_security_logs.year = 2021;

-- Joining people with bank_accounts and atm_transactions by ids and account numbers. As per what the second transcript says.
SELECT people.name, atm_transactions.transaction_type FROM people JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number WHERE atm_transactions.year = 2021
AND atm_transactions.month = 7
AND atm_transactions.day = 28
AND atm_location="Leggett Street"
AND atm_transactions.transaction_type = "withdraw";

-- Getting calls informations on the same date and with duration less than 60 seconds.
SELECT caller, receiver FROM phone_calls WHERE day = 28 AND month = 7 AND year = 2021 AND duration < 60;

-- The next two quries are to add the names of receivers and callers in the same table by using ALTER
ALTER TABLE phone_calls ADD caller_name text;
ALTER TABLE phone_calls ADD receiver_name text;

-- Extracting the previous query but with the new columns we added to check
SELECT caller, caller_name, receiver_name, receiver FROM phone_calls WHERE day = 28 AND month = 7 AND year = 2021 AND duration < 60;

-- Updating and adding new values to the new columns we added from people table
UPDATE phone_calls SET caller_name = people.name FROM people WHERE phone_calls.caller = people.phone_number;
UPDATE phone_calls SET receiver_name = people.name FROM people WHERE phone_calls.receiver = people.phone_number;

-- Extracting the previous query but with the new columns we updated to check their names
SELECT caller, caller_name, receiver_name, receiver FROM phone_calls WHERE day = 28 AND month = 7 AND year = 2021 AND duration < 60;

-- finding flight information
SELECT id, origin_airport_id, destination_airport_id, hour, minute FROM flights WHERE day = 29 AND month = 7 AND year = 2021
ORDER BY hour ASC LIMIT 1;

-- Finding the city name of the original and destination airports
SELECT city FROM airports JOIN flights ON flights.origin_airport_id = airports.id WHERE flights.origin_airport_id = 8;
SELECT city FROM airports JOIN flights ON flights.origin_airport_id = airports.id WHERE flights.origin_airport_id = 4;
-- Now we know that id 8 means fiftyville and 4 means new york city


SELECT flights.destination_airport_id, name, phone_number, license_plate from people JOIN passengers
ON people.passport_number = passengers.passport_number JOIN flights ON flights.id = passengers.flight_id
WHERE flights.id = 36 ORDER BY flights.hour;

-- Finding the name
SELECT name FROM people JOIN passengers ON people.passport_number = passengers.passport_number
JOIN flights ON flights.id = passengers.flight_id WHERE (flights.id = 36 AND flights.day = 29 AND flights.month = 7 AND flights.year = 2021)
AND name IN (SELECT phone_calls.caller_name FROM phone_calls WHERE day = 28 AND month = 7 AND year = 2021 AND duration < 60)
AND name IN (SELECT people.name FROM people JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number WHERE atm_transactions.year = 2021
AND atm_transactions.month = 7
AND atm_transactions.day = 28
AND atm_location="Leggett Street"
AND atm_transactions.transaction_type = "withdraw")
AND name IN (SELECT people.name FROM people JOIN bakery_security_logs
ON bakery_security_logs.license_plate = people.license_plate WHERE bakery_security_logs.minute >= 15 AND bakery_security_logs.minute <= 25
AND bakery_security_logs.hour = 10 AND bakery_security_logs.day = 28 AND bakery_security_logs.month = 7 AND bakery_security_logs.year = 2021);