# Exchange Web Server
This project contains the basic files to send and save an email/attachment through the module ```exchangelib```.

## Installation
Note that the module requires ```Python 3.6``` or higher.

To install the module, run a pip command like the following:


```
pip install exchange-web-server
```

## Setting .env Variables
To work properly, this module needs your companies:
- tenant_id
- client_id
- client_secret


## Usage create_account
Simply import the modules via the following import statements:
```
from exchange-web-server import create_account
account = create_account('user@provider.com')
```
The ```create_account``` function requires your Outlook-Exchange email-address.



## Usage send
Simply import the modules via the following import statements:

```
from exchange-web-server import send_email
```

The ```send_email``` function requires your account, subject, body, recipients and optional attachments.

To send an email, the following code provides the core functionality:
```
send_email(account, 'TestSubject', 'TestBody', ['recepient@provider.com'], ['path/to/your/attachments'])
```



## Usage save
Simply import the modules via the following import statements:

```
from exchange-web-server import save_attachment
```


The ```save_attachment``` function requires your Outlook Exchange Folder, which needs to be located in your inbox. Also it needs a path where to save and an exchangelib account.

To save an attachment, the following code provides the core functionality:
```
save_attachment(account, 'TestSubject', 'TestBody', ['recepient@provider.com'])
```

## License
This project is licensed by a MIT License.
