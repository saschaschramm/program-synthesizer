A class Client that stores the following parameters: client ID, scope and redirect URI
The client implements a method that takes an url as an input and returns an authorization URL. The URL must contain the following parameters: client_id, scope and redirect_uri
After checking __name__ == '__main__' the client is initialized with the arguments client ID "Gq42cPKuPFue0AyvagkUzELV", scope "openid profile", redirect URI "https://example.com/"
The authorization URL must contain the url-encoded parameters client_id, scope and redirect_uri
The authorization URL must contain an urlsafe parameter state in order to mitigate Cross-Site Request Forgery. The probability of an attacker guessing the generated state must be less than or equal to 2^(-128)
The authorization URL must contain an urlsafe parameter state in order to mitigate Cross-Site Request Forgery. The probability of an attacker guessing the generated state must be less than or equal to 2^(-256)
The authorization URL must contain the parameter response_type=code
After checking __name__ == '__main__' the client generates an authorization URL with the endpoint "http://127.0.0.1:5000/oauth/authorize"
After checking __name__ == '__main__' the client sends a request with the authorization URL and prints the response