# Droneface Executor

Client server to obtain **Drone as a Service** and **Drone as a platform**

![droneface](doc/droneface.jpeg)

## Table of contents
* [Table of contents](#table-of-contents)
* [Start server](#start-server)
  * [Connect with Ngrok](#connect-with-ngrok)
* [Development environment](#development-environment)

## Start server

Init server by running the following command at the root of the project

```bash
python app.py
```

Or by flask package

```bash
python -m flask run
```


### Connect with Ngrok

Linux

```bash
./ngrok http 5000
```

Windows

```bash
ngrok.exe http 5000
```

## Development environment

For powershell to allow hot reload
```powershell
$env:FLASK_ENV = "development"
# $env:FLASK_ENV = "production"
```
