
# KTU Mon

## Introduction

KTU Mon is an application that was developed as a desperate attempt at trying to get myself up to date with the recent notifications published by KTU.  

Once upon a time I missed registering for few backlog exams because I put way too much trust in the elected UUC's of my college. I had hoped they would continue providing updates through their Instagram page, only to realize one day that they've deleted the whole damn account and I had missed my backlog exams.  
Those UUC's were useless to say the least (ആരംഭ ശൂരത്വം മാത്രം).  

Although I have dropped out from this University and no longer need the app, I have decided to add useless enhacements and publish this application as a package so that other students out there studying in KTU might find it useful.  

Since this is Open Source code, you can try to understand the engineering behind this over-engineered webscraper and please feel free to post bugs, issue fixes, contribute improvements etc.  

Thanks,  
Anantha

## Installation & Usage

> The recommended way to install is through pipX  

1. Get pipX from pip

    ```
    python -m pip install --user pipx
    ```

2. Make sure that pipX is on PATH by going to it's installed folder ```C:\Users\{USER_NAME}\AppData\Roaming\Python\Python3x\Scripts``` and executing

    ```
    pipx ensurepath
    ```

3. Restart the terminal and run pipX by typing ```pipx```

4. If that didn't work, then manually add the ```pipx.exe``` file in the location ```C:\Users\{USER_NAME}\AppData\Roaming\Python\Python3x\Scripts``` to PATH

5. After that you can install KTU Mon by typing the following into the terminal

    ```
    pipx install ktumon
    ```

6. After installing, you can run it by typing ```ktumon``` in the terminal.  
    > It is recommended that you do not run it immediately. Instead set it up to make it run during startup and restart the system.

7. But inorder for the application to run at startup you'll need to add the executable ```ktumon.exe``` from the location ```C:\Users\{USER_NAME}\AppData\Roaming\Python\Python3x\Scripts``` to the Startup folder.

8. Press Windows logo key + R to open the Run prompt and type ```shell:startup``` this will open up the Startup folder. Paste in the shortcut of the ```ktumon.exe``` executable in there.

9. Now restart the system.  
The first run would take some time to set up the local database and fetch the latest data from KTU, so please be patient. You'll be getting a desktop notification once the application has finished setting up.

## Technical Stuff

The application runs as a system tray icon making use of Pystray. We use a local sqlite database for our database related stuff.

We spawn new threads to run the timer that checks for notifications at set intervals.

The application's Web GUI runs on Uvicorn ASGI Web Server with FastAPI as Web Framework using the Jinja2 Templating Engine and the frontend is completely made using Bootstrap CSS Framework.

The Pystray Process is used to spawn a new Process for running Uvicorn on demand. The spawned Uvicorn Process automatically opens up the default browser to show the Web GUI.

We use a WebSocket connection with the frontend to the backend to determine whether or not to terminate the spawned Uvicorn Process.

The spawned Uvicorn Process is terminated as soon as the User closes the Web GUI tab or the whole Browser itself.

## Development & Contribution

In order to develop and contribute, fork this project and clone it to your local machine.  
We use Visual Studio Code for development and recommend you to use it as well.

You should have Python 3.11 or above.  
We recommennd working with a virtual environment to isolate the packages.

You can install ```virtualenv``` for that purpose

```
pipx install virtualenv
```

Then within the cloned repository run the following command to create a virtual environment

```
virtualenv venv
```

After which change the interpreter within Visual Studio Code to point to the Python Interpreter contained within the created virtual environment.

Now create a new terminal in Visual Studio Code and you'll see that the virtual environement is activated.  

>You can see ```(venv)``` in the shell prompt of the terminal.

After which type in the following command to install an editable module of the project you are working on

```
pip install -e .[dev]
```

After making any changes to the code you can always run it whenever by executing ```ktumon```  

Whenever you are modifying the code, most of the time you won't have to rebuild and reinstall the editable module and that is the advantage of this approach.

Now you're all set!

The following command is used to build the distribution packages

```
python -m build
```