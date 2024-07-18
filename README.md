Crypto Api

analyze real-time performance statistics of cryptocurrencies

this project is a python api which calculates some statistics on the user requested cryptocurrency.  
it accepts input in json format with a field for the name of a cryptocurrency.  
it makes external api calls to fetch real-time price data, as well as a range of historical prices.  
the python backend then computes some statistics.  
the api then returns these statistics in a json format.  
currently, usage is to make POST requests on https://testaccount0.pythonanywhere.com/api/stats. 
you can view the api output using postman or an api testing package of your choice.  
aditionally, there is a webpage created for interacting with the api in a more user friendly format. Webpage is written using plain html/css/javascript.  


Installation:  
  
The api is accessible at https://testaccount0.pythonanywhere.com/api/stats.

There is also a demo webpage through which you can interact with the API, available at: https://testaccount0.pythonanywhere.com/demo


API documentation:

Endpoint '/api/stats'  
This endpoint accepts HTTP POST requests and returns statistics for the specified cryptocurrency.  
The request must be a JSON object with the following parameter:  
'name' (string): the name of cryptocurrency   
example:  
{  
  "name": "ethereum"  
}  
Response format:  
the API response is a JSON object containing the calculated statistics  
example response:  
{
    "ath": 4085.78,
    "ath_date": "14-03-2024",
    "low_after_ath": 2826.93,
    "low_after_ath_date": "05-05-2024",
    "name": "ethereum",
    "percent_decline_from_ath": 14.617527130682518,
    "percent_gain_to_reach_ath": 17.12005595464006,
    "price": 3488.54,
    "tracked_from": "18-07-2023"
}
  
How to use:  
to use the API, send a POST request to the '/api/stats' endpoint with a JSON object containing the 'name' parameter  
example using cURL:  
curl -X POST -H "Content-Type: application/json" -d '{"name": "bitcoin"}' https://testaccount0.pythonanywhere.com/api/stats 
review the response from the API to get statistics for that cryptocurrency.

alternatively: use the webpage titled main.html to interact with the API.

TODO: add database to cache results of api requests  
implement automated testing
