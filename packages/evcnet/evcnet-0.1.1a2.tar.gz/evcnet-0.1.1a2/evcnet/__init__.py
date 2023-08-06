import requests


class Evcnet(object):

    def __init__(self, url):
        self.__url = url
        self.__session = requests.session()
        self.__session.headers.update(
            {
                "user-agent": "python-evcnet/0.0.1 (+https://github.com/hkraal/python-evcnet)"
            }
        )

    def authenticate(self, username, password):
        # Login to get a cookie.
        r = self.__session.post(
            url=self.__url,
            data={
                "emailField": username,
                "passwordField": password,
                "Login": "Sign on",
            },
            allow_redirects=False,
        )
        if r.status_code != 302:
            raise RuntimeError(
                "Unexpected status code ({}) during login: {}".format(
                    r.status_code, r
                )
            )
        return True

    def total_usage(self):
        # Retrieve metric.
        data_request = self.__session.get(
            url=f"{self.__url}/api/ajax",
            params={
                "requests": '{"0":{"handler":"\\\\LMS\\\\EV\\\\AsyncServices\\\\DashboardAsyncService","method":"totalUsage","params":{"mode":"customer","maxCache":3600}},"1":{"handler":"\\\\LMS\\\\EV\\\\AsyncServices\\\\DashboardAsyncService","method":"totalUsage","params":{"mode":"rechargeSpot","maxCache":3600}}}'
            },
            allow_redirects=False,
        )
        if data_request.status_code != 200:
            raise RuntimeError(
                "Unexpected status code ({}) during data retrieval: {}".format(
                    data_request.status_code, data_request
                )
            )

        api_data = data_request.json()

        result = {
            "totalUsage": api_data[0],
            "totalProvided": api_data[1],
        }

        return result
