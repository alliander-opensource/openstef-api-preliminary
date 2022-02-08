import requests


class PetClient:
    """Pet client.

    Communicates with the external Swagger pet store to retrieve pets.
    """

    def __init__(self):
        """Creates a pet client instance.

        Sets up a requests session for increased performance and cookie handling.
        """
        self.sess = requests.session()
        self.json_headers = {"content-type": "application/json"}

    def get_pets(self):
        """Retrieves pets from the Swagger pet store.

        Note:
            The response does not contain Pet object instances yet.

        Returns:
            Dictionary of pets as defined by the Swagger pet store.
        """
        res = self.sess.get(
            "https://petstore.swagger.io/v2/pet/findByStatus?status=available",
            headers=self.json_headers,
        )
        return res.json()
