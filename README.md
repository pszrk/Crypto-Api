# Crypto-Cooldown
analyze real-time performance statistics of cryptocurrencies


this project is a python api which calculates some statistics on the user requested cryptocurrency.  
it accepts input in json format with a field for the name of a cryptocurrency.  
it makes external api calls to fetch real-time price data, as well as a range of historical prices.  
the python backend then computes some statistics.  
the api then returns these statistics in a json format.  
currently, usage is to clone the repository, run api_server.py, and make json queries on localhost:5000. you can then view the api output using postman or an api testing package of your choice.  
aditionally, there is a webpage created for interacting with the api in a more user friendly format. Webpage is written using plain html/css/javascript.  


Installation:  
  
Clone repository  
Install dependencies (pip install -r requirements.txt)  
Start the api server (python api_server.py)  
The api will be accessible at http://localhost:5000  
If you want to interact with the API through the webpage instead, open main.html after starting the API server.  

API documentation:

Endpoint '/api/stats'  
This endpoint accepts HTTP POST requests and returns statistics for the specified cryptocurrency.  
The request must be a JSON object with the following parameter:  
'name' (string): the name of cryptocurrency   
example:  
{  
  "name": "bitcoin"  
}  
Response format:  
the API response is a JSON object containing the calculated statistics  
example response:  
{  
'name': 'bitcoin',   
'current': 27926.159635951317,   
'peak_date': '09-11-2021',   
'peak_price': 67617.0155448617,   
'peak_21': True,   
'ath': 67617.0,   
'ath_diff': 58.69949918518817,   
'ath_date': '11-11-2021',   
'all_stats': 'current price of bitcoin is $27926.16. bitcoin reached its peak price in the crypto inflationary period of 2021. bitcoin is 58.7% below its all time high of 67617.00 from 11-11-2021'  
}  
  
How to use:  
to use the API, send a POST request to the '/api/stats' endpoint with a JSON object containing the 'name' parameter  
example using cURL:  
curl -X POST -H "Content-Type: application/json" -d '{"name": "bitcoin"}' http://localhost:5000/api/stats  
review the response from the API to get statistics for that cryptocurrency.
