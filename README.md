# secret-santa
This repository has been created to do the secret santa lottery online (especially for companies working remotely).

## Installation
```console
pip install numpy
```

## Usage

### Allows low secure app
If your sender mail is a gmail you can not allow lqw secure app. You must use *“Third-party apps with account access,”*.

> Important: "Manage third-party access" is only available if you grant access to third-party apps.
> 1. Go to the Security section of your Google Account.
> 2. Under “Third-party apps with account access,” select Manage third-party access.
> 3. Select the app or service you want to review.

Source:
- https://support.google.com/accounts/answer/6010255?hl=en
- https://support.google.com/accounts/answer/3466521 

### Executing
for Linux:
```console
python3 /path_python_script send_email.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.