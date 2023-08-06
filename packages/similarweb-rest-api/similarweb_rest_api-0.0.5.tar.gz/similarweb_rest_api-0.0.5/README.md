# similarweb REST API

### Introduction
The similarweb REST API is a library that simplifies the access to the REST API of Similarweb.

### Installation
To install the library, run the following command:

Copy code
`pip install similarweb-rest-api`
### Usage
To use the library, import the SimilarwebApi class and create an instance of it. Then, use the get method to make a request to the API.

```python
from similarweb_rest_api import SimilarwebApi

api = SimilarwebApi()
response = api.get('website/traffic', domain='example.com', start_date='2020-01-01', end_date='2020-01-31')
```
The get method returns a SimilarwebResponse object, which contains the API response in various formats. To access the response in a specific format, use one of the following methods:

**to_json:** returns the response as a JSON string
**to_dataframe:** returns the response as a Pandas DataFrame
**to_sql:** returns an SQL statement to insert the response into a table
**to_xml:** returns the response as an XML document
**to_excel:** writes the response to an Excel file
**to_csv:** writes the response to a CSV file
**to_html:** returns the response as an HTML table
**to_jsonl:** writes the response to a JSON Lines file
**to_yaml:** returns the response as a YAML document

For example, to convert the response to a DataFrame and display the first 5 rows:

```python
df = response.to_dataframe()
df.head()
```
### Parameters
The following parameters can be passed to the get function:

**name:** The name of the API endpoint. 
**domain:** The domain to get data for. 
**api_key:** Your API key. 
**start_date:** The start date for the data range (in the format YYYY-MM). 
**end_date:** The end date for the data range (in the format YYYY-MM). 
### License
This library is free to use for non-commercial purposes. For commercial use, please contact the author for permission.

### Contact
If you have any questions or suggestions, please contact the author Damien Frigewski at [dfrigewski@gmail.com](mailto:dfrigewski@gmail.com "dfrigewski@gmail.com").