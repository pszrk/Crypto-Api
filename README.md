View a summary of some statistics on a cryptocurrency of your choice

This project is a python RESTful api which calculates some statistics on a cryptocurrency which the user specifies.  
It accepts input in json format with a field for the name of a cryptocurrency.  
The Python backend makes external api calls to get real-time and historical prices.
The Python backend then computes some statistics, 
then returns these statistics via the API in a json format.  
The API accepts POST requests on the endpoint /api/stats.
You can view the api output using postman or an api testing package of your choice.  
Aditionally, there is a webpage created for interacting with the api.

<b>Technologies:</b>   
Python - backend development  
Flask - Web framework for building the API endpoints  
HTML/JavaScript/CSS: frontend webpage to interact with the API


<b>Usage:</b>  
The api endpoint is accessible at https://testaccount0.pythonanywhere.com/api/stats.

There is a demo webpage through which you can interact with the API, at: https://testaccount0.pythonanywhere.com/demo
  
  
<b>API documentation:</b>  
Endpoint /api/stats  
This endpoint accepts HTTP POST requests and returns statistics for the specified cryptocurrency.  
The request must be a JSON object with the following parameter:  
'name' (string): the name of cryptocurrency   
example:  
```
{  
  "name": "ethereum"  
}  
```
Response format:  
the API response is a JSON object containing some information about that cryptocurrency  
example response:  
```
{
    "amount_gain_to_reach_ath": 8376,
    "ath": 73738,
    "ath_date": "17-03-2024",
    "low_after_ath": 53898,
    "low_after_ath_date": "07-07-2024",
    "name": "bitcoin",
    "percent_decline_from_ath": 11.359136401855217,
    "price": 65362,
    "tracked_from": "26-07-2023"
}
```

Usage example using cURL:  
```
curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"bitcoin\"}" https://testaccount0.pythonanywhere.com/api/stats
```
alternatively: use the webpage titled main.html to interact with the API.

TODO:   
add database to cache results of api requests  
implement automated testing
