import requests
from bson import ObjectId
import webbrowser
from ratelimiter import RateLimiter


class Intramove:
    """The Intramove class is a client for interacting with an API that allows you to purchase and use various packages of news analysis services."""

    available_packages = ["headlines-100","articles-100"]
    current_service_ip = "https://api.intramove.ai:443"

    @classmethod
    def get_available_packages(cls):
        """The get_available_packages method is a class method that returns a list of available packages that can be purchased."""
        return cls.available_packages

    def __init__(self):
        self.packages = {
            "headlines-100": "prod_N2ndwwdkNjVThi",
            "articles-100": "prod_N3UFpCDcp0Hisv"
        }  # "prod_N2ndwwdkNjVThi"}
        self.headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
        }
        self.api_key = None
        self.client_ids = []

    def _call_endpoint(self, endpoint, payload):
        try:
            response = requests.get(
                f"{Intramove.current_service_ip}/{endpoint}",
                headers=self.headers,
                params=payload,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"An HTTP error occurred: {err}")
        except requests.exceptions.RequestException as err:
            print(f"An error occurred while making the request: {err}")

        response = response.json()

        if not response:
            raise Exception("Client not registered.")

        return response

    def buy_package(self, product: str, quantity: int = 1):
        """The buy_package method allows you to purchase a package of news headlines by specifying the product name and quantity,
        and it opens a URL in your web browser to complete the purchase."""

        assert (
            product in self.packages.keys()
        ), f"Product has to be in {self.packages.keys()}."
        assert quantity > 0, "Quantity has to be greater than 0."

        payload = {"product_id": self.packages[product], "quantity": quantity}
        response = requests.post(
            f"{Intramove.current_service_ip}/checkout",
            headers=self.headers,
            params=payload,
        )
        url = response.json()["session_id"]["url"]
        session_details = response.json()
        try:
            webbrowser.open(url)
        except:
            print(
                "Couldn't open browser. Please copy the link and run it in the browser."
            )
            return url, session_details
        return url, session_details

    @RateLimiter(max_calls=1, period=0.5)
    def get_id(self, email: str, name: str):
        """The get_id method allows you to retrieve a client ID for a given email and name."""

        if not isinstance(email, str) or not email:
            raise ValueError("email must be a non-empty string")
        if not isinstance(name, str) or not name:
            raise ValueError("name must be a non-empty string")

        payload = {"email": email, "name": name}
        response = self._call_endpoint("client_id", payload)
        return response

    @RateLimiter(max_calls=1, period=0.5)
    def get_api_key(self, client_id: str):
        """The get_api_key method allows you to retrieve an API key for a given client ID."""
        if not isinstance(client_id, str) or not client_id:
            raise ValueError("client_id must be a non-empty string")

        try:
            ObjectId(client_id)
        except:
            raise Exception(
                "Client ID doesn't have the right format, you must use the ID returned."
            )

        payload = {"client_id": client_id}

        self.api_key = self._call_endpoint("client_api_key", payload)
        return self.api_key

    @RateLimiter(max_calls=1, period=0.5)
    def credits_available(self, api_key: str, product_name:str):
        """The credits_available method allows you to retrieve information about the number of credits available for a given API key."""
        if not isinstance(api_key, str) or not api_key:
            raise ValueError("api_key must be a non-empty string")

        if not isinstance(product_name, str) or not product_name:
            raise ValueError("product_name must be a non-empty string")

        if product_name not in Intramove.available_packages:
            raise ValueError("product_name must be one of the avalable packages.")

        payload = {"api_key": api_key, "product_name":product_name}
        return self._call_endpoint("credits_available", payload)

    @RateLimiter(max_calls=1, period=0.5)
    def credits_consumed(self, api_key: str, product_name:str):
        """The credits_consumed method allows you to retrieve information about the number of credits consumed for a given API key."""
        if not isinstance(api_key, str) or not api_key:
            raise ValueError("api_key must be a non-empty string")

        if not isinstance(product_name, str) or not product_name:
            raise ValueError("product_name must be a non-empty string")

        if product_name not in Intramove.available_packages:
            raise ValueError("product_name must be one of the avalable packages.")

        payload = {"api_key": api_key, "product_name":product_name}
        return self._call_endpoint("credits_consumed", payload)

    @RateLimiter(max_calls=1, period=0.5)
    def status(self, api_key: str, product_name:str):
        """The status method allows you to retrieve the status of a given API key."""
        if not isinstance(api_key, str) or not api_key:
            raise ValueError("api_key must be a non-empty string")
        
        if not isinstance(product_name, str) or not product_name:
            raise ValueError("product_name must be a non-empty string")

        if product_name not in Intramove.available_packages:
            raise ValueError("product_name must be one of the avalable packages.")

        payload = {"api_key": api_key, "product_name":product_name}
        return self._call_endpoint("status", payload)

    @RateLimiter(max_calls=1, period=0.0001)
    def analyze_headline(
        self, headline: str, date: str, api_key: str, callback_url: str = ""
    ):
        """
        Analyze a given headline for financial sentiment.

        Parameters:
        - headline (str): the headline to analyze
        - date (str): the date of the headline
        - api_key (str): the API key to use for authentication
        - callback_url (str, optional): the URL to send the results to. If not provided, the results will be returned directly.

        Returns:
        - A dictionary containing the results of the analysis.
        """
        if not isinstance(headline, str) or not headline:
            raise ValueError("headline must be a non-empty string")

        if not isinstance(date, str):
            raise ValueError("date must be a string")

        if not isinstance(api_key, str) or not api_key:
            raise ValueError("api_key must be a non-empty string")

        if not isinstance(callback_url, str):
            raise ValueError("callback_url must be a string")

        headline_payload = {
            "headline": headline,
            "date": date,
            "callback_url": callback_url,
        }

        headline_headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "api-key": api_key,
        }

        response = requests.post(
            f"{Intramove.current_service_ip}/analyze/headline",
            headers=headline_headers,
            params=headline_payload,
        )
        return response.json()

    @RateLimiter(max_calls=1, period=0.0001)
    def analyze_article(
        self, article: str, date: str, api_key: str, callback_url: str = ""
    ):
        """
        Analyze a given article for financial sentiment.

        Parameters:
        - article (str): the article to analyze
        - date (str): the date of the headline
        - api_key (str): the API key to use for authentication
        - callback_url (str, optional): the URL to send the results to. If not provided, the results will be returned directly.

        Returns:
        - A dictionary containing the results of the analysis.
        """
        if not isinstance(article, str) or not article:
            raise ValueError("article must be a non-empty string")

        if not isinstance(date, str):
            raise ValueError("date must be a string")

        if not isinstance(api_key, str) or not api_key:
            raise ValueError("api_key must be a non-empty string")

        if not isinstance(callback_url, str):
            raise ValueError("callback_url must be a string")

        article_payload = {
            "article": article,
            "date": date,
            "callback_url": callback_url,
        }

        article_headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "api-key": api_key,
        }

        response = requests.post(
            f"{Intramove.current_service_ip}/analyze/article",
            headers=article_headers,
            params=article_payload,
        )
        return response.json()