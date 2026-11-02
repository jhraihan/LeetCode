SELECT
    Person.firstName,
    Person.lastName,
    Address.city,
    Address.state
FROM
    Person
LEFT JOIN
    Address ON Person.personId = Address.personId;


-- Employees Earning More Than Their Managers

SELECT
    e1.name AS Employee
FROM
    Employee e1
JOIN
    Employee e2 ON e1.managerId = e2.id
WHERE
    e1.salary > e2.salary