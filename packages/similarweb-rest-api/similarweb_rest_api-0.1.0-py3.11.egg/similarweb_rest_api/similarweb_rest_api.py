import json
import os
import re
import typing
import requests
import pandas as pd
import xml.etree.ElementTree as ET
import openpyxl
import csv
import jinja2
import jsonlines
import yaml


class SimilarwebResponse:
    def __init__(self, data):
        self.data = data
        self.functions = {
            "to_json": self.to_json,
            "to_dataframe": self.to_dataframe,
            "to_sql": self.to_sql,
            "to_xml": self.to_xml,
            "to_excel": self.to_excel,
            "to_csv": self.to_csv,
            "to_html": self.to_html,
            "to_json_lines": self.to_json_lines,
            "to_yaml": self.to_yaml
        }

    def _extract_results(self):
        """
        Extracts the results from the JSON response.

        The results are extracted from the JSON response by finding the key that
        holds the results. The key is found by searching for the key that holds a
        list.

        Args:
            None

        Returns:
            A list of results.
        """
        # Parse the JSON string into a Python dictionary
        data = data = self.data.json()

        # Find the key that holds the results
        result_key = None
        for key, value in data.items():
            if isinstance(value, list):
                result_key = key
                break

        # Extract the results from the dictionary
        if result_key:
            return data[result_key]
        else:
            return None

    def description(self, func_name: str) -> str:
        """
        Returns the docstring of the specified function.

        Parameters
        ----------
        func_name : str
            The name of the function.

        Returns
        -------
        str
            The docstring of the specified function.
        """
        # Get the function object
        func = getattr(self, func_name)

        # Return the docstring
        return func.__doc__

    def to_json(self):
        """
        This function returns a JSON representation of the data
        contained in the object.
        """
        return json.dumps(self.data.json())

    def to_dataframe(self, **kwargs):
        """
        to_dataframe(self, **kwargs)
        Convert the results to a DataFrame.

        Parameters
        ----------
        kwargs : dict
            Keyword arguments to pass to the DataFrame constructor.

        Returns
        -------
        df : DataFrame
            A DataFrame containing the results.
        """
        # Extract the results
        results = self._extract_results()

        # Convert the results to a DataFrame
        df = pd.DataFrame(results, **kwargs)

        return df

    def to_sql(self, table_name):
        """
        to_sql(self, table_name)

        Generates an SQL statement to insert the results of the query into the
        specified table.

        Parameters
        ----------
        table_name : str
            The name of the table to insert the results into.

        Returns
        -------
        str
            The SQL statement to insert the results into the specified table.

        Examples
        --------
        >>> from sql_query import SQLQuery
        >>> query = SQLQuery("SELECT * FROM table")
        >>> query.to_sql("new_table")
        'INSERT INTO new_table (column1, column2, column3) VALUES (value1, value2, value3), (value4, value5, value6), (value7, value8, value9);'
        """
        # Extract the results
        results = self._extract_results()

        # Generate the SQL statement
        sql = f"INSERT INTO {table_name} ({', '.join(results[0].keys())}) VALUES "
        for result in results:
            sql += f"({', '.join(str(val) for val in result.values())}), "
        sql = sql[:-2]  # Remove the last comma and space
        sql += ";"

        return sql

    def to_xml(self, root_tag):
        """
        to_xml(self, root_tag)

        Convert the results to XML.

        Parameters
        ----------
        root_tag : str
            The name of the root element.

        Returns
        -------
        str
            The XML document as a string.
        """
        # Extract the results
        results = self._extract_results()

        # Create the root element
        root = ET.Element(root_tag)

        # Create a child element for each result
        for result in results:
            item = ET.SubElement(root, "item")
            for key, value in result.items():
                child = ET.SubElement(item, key)
                child.text = str(value)

        # Return the XML document as a string
        return ET.tostring(root, encoding="unicode")

    def to_excel(self, filepath, sheet_name="Sheet1", **kwargs):
        """
        Write the results of a query to an Excel file.

        Parameters
        ----------
        filepath : str
            The path to the Excel file to write to.
        sheet_name : str, optional
            The name of the sheet to write to.
        **kwargs : dict
            Additional keyword arguments to pass to the underlying
            `openpyxl.Workbook.save` method.
        """
        # Extract the results
        results = self._extract_results()

        # Create a new workbook
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = sheet_name

        # Write the headers
        headers = list(results[0].keys())
        sheet.append(headers)

        # Write the rows
        for result in results:
            row = list(result.values())
            sheet.append(row)

        # Save the workbook to the specified filepath
        workbook.save(filepath)

    def to_csv(self, filepath, **kwargs):
        """
        Write the results to a CSV file.

        Parameters
        ----------
        filepath : str
            The path to the CSV file.
        kwargs : dict
            Keyword arguments to pass to the CSV writer.
        """
        # Extract the results
        results = self._extract_results()

        # Write the headers
        headers = list(results[0].keys())

        # Write the rows
        rows = [list(result.values()) for result in results]

        # Write the CSV file
        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f, **kwargs)
            writer.writerow(headers)
            writer.writerows(rows)

    def to_html(self, template_path, **context):
        """
        Render the results of the test suite to HTML.

        Parameters
        ----------
        template_path : str
            The path to the template to use for rendering the results.
        **context
            Any additional context to pass to the template.

        Returns
        -------
        str
            The rendered HTML.
        """
        # Extract the results
        results = self._extract_results()

        # Load the template
        with open(template_path, "r") as f:
            template = jinja2.Template(f.read())

        # Render the template with the results and any additional context
        html = template.render(results=results, **context)

        return html

    def to_json_lines(self, filepath):
        """
        Write the results to a file in JSON Lines format.

        Parameters
        ----------
        filepath : str
            The path to the file to write the results to.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If the filepath is not a string.
        """
        # Extract the results
        results = self._extract_results()

        # Write the results to a file in JSON Lines format
        with jsonlines.open(filepath, "w") as writer:
            for result in results:
                writer.write(result)

    def to_yaml(self):
        """
        Convert the results to YAML.

        Parameters
        ----------
        results : dict
            The results to convert to YAML.

        Returns
        -------
        yaml : str
            The results in YAML format.
        """
        # Extract the results
        results = self._extract_results()

        # Convert the results to YAML
        yaml = yaml.dump(results, default_flow_style=False)

        return yaml


class SimilarwebApi:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.data = None
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, 'similarweb_endpoints.json')
        with open(file_path, 'r') as f:
            self.json_list = json.load(f)


    def find_json(self, json_list, name):
        """
        Finds a JSON object in a list of JSON objects by name.

        Parameters
        ----------
        json_list : list
            A list of JSON objects.
        name : str
            The name of the JSON object to find.

        Returns
        -------
        dict
            The JSON object with the given name.

        Raises
        ------
        ValueError
            If no JSON object with the given name is found.
        """
        for obj in json_list:
            if obj['name'] == name:
                return obj
            return None

    def list_endpoints(self):
        print('These are all endpoints that are included in the module:')
        for endpoint in self.json_list:
            print(f"- {endpoint['name']}")

    def description(self, func_name: str) -> str:
        """
        Returns the description of the specified function.

        Parameters
        ----------
        func_name : str
            The name of the function to get the description of.

        Returns
        -------
        str
            The description of the specified function.
        """
        # Get the function object
        func = getattr(self, func_name)

        # Return the docstring of the function
        return func.__doc__

    def description_endpoint(self, endpoint: str) -> str:
        """
        Returns the description of the specified endpoint.

        Parameters
        ----------
        endpoint : str
            The name of the endpoint to get the description for.

        Returns
        -------
        str
            The description of the specified endpoint.
        """
        # Find the JSON object for the function
        json_obj = self.find_json(json_list=self.json_list, name=endpoint)
        if not json_obj:
            return None

        # Return the description of the function
        return json_obj['description']

    def list_parameter(self, endpoint: str) -> str:
        json_obj = self.find_json(json_list=self.json_list, name=endpoint)
        if not json_obj:
            return None

        # Find the key that holds the results
        result_key = []
        for key, value in json_obj.items():
            if isinstance(value, list):
                result_key.append(key)

        # Extract the results from the dictionary
        if result_key:
            for key in result_key:
                print('_______________________')
                print(f"{key.upper()} :\n")
                for param in json_obj[key]:
                    print('|')
                    for key in param.keys():
                        print(f"|__ {key.upper()}: {param[key]}")
                print('\n')
        else:
            return None

    def get(self, name, **kwargs):
        """
        Send an HTTP GET request to a Similarweb API and return the response as a JSON string.

        This method is used to send a request to a specific API endpoint provided by Similarweb, based on the
        `name` argument. Any additional keyword arguments passed to the method will be included as parameters
        in the request.

        The method will first look for a JSON object in the `similarweb_endpoints.json` file that has a
        matching `name` field. If no such object is found, the method will return None.

        If a JSON object is found, the method will check that all required path parameters are provided
        in `kwargs`. It will also check that the values of all path and query parameters match the required
        data type and format, if specified.

        The method will then replace any path parameters in the API URL with the corresponding values from
        `kwargs` and add any query parameters to the URL. It will then send an HTTP GET request to the API
        using the constructed URL and return the response as a JSON string.

        Args:
            name: The name of the API method to request. This should match the `name` field of a JSON object
                in the `similarweb_endpoints.json` file.
            **kwargs: Optional keyword arguments to pass to the API as path or query parameters.

        Returns:
            The response from the API as a JSON string. If no matching JSON object is found or if the request
            fails for any reason, the return value will be None.

        Raises:
            ValueError: If a required path or query parameter is missing or if a provided parameter value is
                invalid.
        """
        # self.json_dict = self.find_json(self.json_list, name)
        # Find the JSON object with the matching name
        json_obj = self.find_json(json_list=self.json_list, name=name)
        if not json_obj:
            return None

        # Check that all required path parameters are provided
        required_params = [param['name'] for param in json_obj['path parameter'] if param['required']]
        missing_params = [param for param in required_params if param not in kwargs]
        if missing_params:
            raise ValueError(f"Missing required path parameters: {', '.join(missing_params)}")

        # Check that the value matches the datatype and format, if specified
        format_pattern = r'\d{4}-\d{2}'
        for param in json_obj['path parameter']:
            param_name = param['name']
            if param_name in kwargs:
                value = kwargs[param_name]
                datatype = param.get('datatype')
                if datatype:
                    if datatype == "string":
                        datatype = str
                    elif datatype == "boolean":
                        datatype = bool
                    elif datatype == "integer":
                        datatype = int
                    if not isinstance(value, datatype):
                        raise ValueError(f"Value for path parameter '{param_name}' must be of type {datatype.__name__}")
                format = param.get('format')
                if format and not isinstance(value, str):
                    raise ValueError(f"Value for path parameter '{param_name}' must be a string")
                if format and not re.match(format_pattern, value):
                    raise ValueError(
                        f"Value for query parameter '{param_name}' does not match the required format {format}")

        # Check that all required query parameters are provided
        required_params = [param['name'] for param in json_obj['query parameter'] if param['required']]
        missing_params = [param for param in required_params if param not in kwargs]
        if missing_params:
            raise ValueError(f"Missing required query parameters: {', '.join(missing_params)}")

        # Check that the value matches the datatype and format, if specified
        for param in json_obj['query parameter']:
            param_name = param['name']
            if param_name in kwargs:
                value = kwargs[param_name]
                datatype = param.get('datatype')
                if datatype:
                    if datatype == "string":
                        datatype = str
                    elif datatype == "boolean":
                        datatype = bool
                    elif datatype == "integer":
                        datatype = int
                    if not isinstance(value, datatype):
                        raise ValueError(f"Value for path parameter '{param_name}' must be of type {datatype.__name__}")
                format = param.get('format')
                if format and not isinstance(value, str):
                    raise ValueError(f"Value for query parameter '{param_name}' must be a string")
                if format and not re.match(format_pattern, value):
                    raise ValueError(
                        f"Value for query parameter '{param_name}' does not match the required format {format}")

        # Replace path parameters in the URL
        url = json_obj['url']
        for param in json_obj['path parameter']:
            param_name = param['name']
            wrapped_param_name = f"{{{param_name}}}"
            if param_name in kwargs:
                value = kwargs[param_name]
                if wrapped_param_name in url:
                    url = url.replace(f"{{{param_name}}}", value)
                else:
                    url = url.replace(f"{param_name}", value)
            else:
                raise ValueError(f"Missing required path parameter '{param_name}'")

        # Add query parameters to the URL
        query_params = []
        for param in json_obj['query parameter']:
            param_name = param['name']
            if param_name in kwargs:
                value = kwargs[param_name]
                query_params.append(f"{param_name}={value}")
        if query_params:
            url += "?" + "&".join(query_params)
        if json_obj['method'] == 'GET':
            response = requests.get(url)
            return SimilarwebResponse(response)
        else:
            raise ValueError(f"Missing correct method for request")