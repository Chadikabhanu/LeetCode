/* Write your PL/SQL query statement below */
SELECT p.firstName,p.lastname,a.city,a.state
FROM Person p
left join Address a
on p.personid = a.personid;