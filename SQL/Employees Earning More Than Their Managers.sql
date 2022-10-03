# https://leetcode.com/problems/employees-earning-more-than-their-managers/

# Write your MySQL query statement below
select a.name Employee from Employee a 
left join Employee b
on a.ManagerId = b.Id
where a.Salary > b.Salary