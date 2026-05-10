create database job_market_analysis;

use job_market_analysis;

select count(*) from jobs;

select Location,count(*) as `total jobs`
from jobs
group by Location
order by `total jobs` desc ;

SELECT `Job Title`, AVG(`Salary Estimate`) AS `avg salary`
FROM jobs
GROUP BY `Job Title`
ORDER BY `avg salary` DESC;

select Industry, count(*) as `total jobs`
from jobs
group by Industry
order by `total jobs` desc;

SELECT `Company Name`, AVG(`Salary Estimate`) AS avg_salary
FROM jobs
GROUP BY `Company Name`
ORDER BY avg_salary DESC;

