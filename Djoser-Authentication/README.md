### First, make sure that [python3.10](https://www.python.org/) and [node.js 16](https://nodejs.org/en/) are installed on your system.

### Back-End server:

And then, open the command prompt in the location where the Djoser-Authentication folder is located and navigate to the following folder with the following command : 

```
> cd Djoser-Authentication\backend 
```

Then create a virtual environment with the following command:

```
> python -m venv .venv
```
And then activate virtual environment with the following command:

```
> .venv\Scripts\activate
```
After the activation of the virtual environment, it is the turn of the required modules with the following command:
```
> pyrhon -m pip install -r requirements.txt
```
Then run the django server with the following command:
```
> python manage.py runserver
```
> **Note**
> Do not close the terminal after this step and let the server run

### Front-End server:
Now it's time to run the front server

Open a new command prompt in the location where the Djoser-Authentication folder is located and navigate to the following folder with the following command:

```
> cd Djoser-Authentication\frontend 
```

Then install the node modules with the following command:

```
> npm install
```

Afrter this run the vue.js server with the following command:

```
npm run serve
```
### And finally navigate to the this url : [http://localhost:8080/](http://localhost:8080/)
