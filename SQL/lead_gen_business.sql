-- 1. What query would you run to get the total revenue for March of 2012?
SELECT SUM(billing.amount) AS revenue FROM billing
WHERE billing.charged_datetime BETWEEN '2012-03-01' AND '2012-03-31';

-- 2. What query would you run to get total revenue collected from the client with an id of 2?
SELECT SUM(billing.amount) AS revenue FROM billing
WHERE billing.client_id = 2;

-- 3. What query would you run to get all the sites that client=10 owns?
SELECT sites.domain_name FROM sites
WHERE sites.client_id = 10;

-- 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client=20?
SELECT sites.site_id, COUNT(sites.site_id) AS number_of_sites, DATE_FORMAT(sites.created_datetime, '%M') AS month_created, DATE_FORMAT(sites.created_datetime, '%Y') AS year_created
FROM sites
WHERE sites.client_id = 1
GROUP BY year_created, month_created;

SELECT sites.site_id, COUNT(sites.site_id) AS number_of_sites, DATE_FORMAT(sites.created_datetime, '%M') AS month_created, DATE_FORMAT(sites.created_datetime, '%Y') AS year_created
FROM sites
WHERE sites.client_id = 20
GROUP BY year_created, month_created;

-- 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
SELECT sites.domain_name, COUNT(leads.leads_id) AS leads_generated, sites.created_datetime AS created
FROM leads
JOIN sites ON leads.site_id = sites.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-02-15'
GROUP BY sites.domain_name;

-- 6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, COUNT(leads.leads_id) AS number_of_leads
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY client_name;

-- 7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, COUNT(leads.leads_id) AS number_of_leads, DATE_FORMAT(leads.registered_datetime, '%M') AS month_generated
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-06-30'
GROUP BY leads.registered_datetime;

-- 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011? Order this query by client id.  Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.
SELECT clients.client_id, CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, COUNT(leads.leads_id) AS number_of_leads, sites.domain_name
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY sites.domain_name
ORDER BY clients.client_id;

SELECT clients.client_id, CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, COUNT(leads.leads_id) AS number_of_leads, sites.domain_name
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
GROUP BY sites.domain_name
ORDER BY clients.client_id;

-- 9. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client id.
SELECT SUM(billing.amount) AS revenue, billing.client_id, CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, DATE_FORMAT(billing.charged_datetime, '%M %Y') AS months
FROM billing
JOIN clients ON billing.client_id = clients.client_id
GROUP BY billing.charged_datetime
ORDER BY billing.client_id;

-- 10. Write a single query that retrieves all the sites that each client owns. Group the results so that each row shows a new client. It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, GROUP_CONCAT(sites.domain_name SEPARATOR ' / ') AS sites
FROM clients
JOIN sites ON clients.client_id = sites.client_id
GROUP BY clients.client_id;