# https://leetcode.com/problems/nth-highest-salary/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE temp INT;
 SET temp = N-1;
  RETURN (
      select distinct Salary
from Employee
order by Salary desc
limit 1 offset temp
      
  );
END