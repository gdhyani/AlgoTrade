from py5paisa import FivePaisaClient;

# login credentials
cred={
    "APP_NAME":"5P51285403",
    "APP_SOURCE":"18349",
    "USER_ID":"IHfq2r6NWRV",
    "PASSWORD":"AdGAP0p3vBg",
    "USER_KEY":"BW1Hx8St1JeVg0W0yQXxIdJDdkW7Qyhx",
    "ENCRYPTION_KEY":"RgNQaCDUN33pITzrnPFWVBnsvOAFZxPy"
    }

client = FivePaisaClient(cred=cred)
# Access Token for Login

accessToken = input("Enter Access TOken: ");

client.get_access_token(accessToken);
#Loggin Successful
