import requests

class ESP32FlightContoller:
    
    # Initialize parameters
    def __init__(self, ipAddress, port):
        self.ip = ipAddress
        self.port = port
        self.url = f'http://{ipAddress}:{port}'
        self.connections = []    

    def add_connection(self, device):
        self.connections.append(device)
    
    def get_connections(self):
        count = 0
        for device in self.connections:
            count = 1 + count
            print(device)
        return self.connections, "Number of connections: ", count
    
    def get_AP_connections(self):
        try:
            response = requests.get(self.url, timeout=2)
            response.raise_for_status()
            print(response.text)
            return response.text
        except requests.RequestException as e:
            message = " Unable to pair with FC"
            print(f"Unable to pair with FC: {e}")
            return message
        