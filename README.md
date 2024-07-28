## Group3-Python-Azure
   - coding structure
      - app.py
      - README.md
      - requirements.txt
      - .gitignore
      - data\USA_Housing.csv
      - .github\workflows (main_group3-python.yml)

### Github Repository Group3-Python-Azure
   - https://github.com/WilliamShi5358/Group3-Python-Azure.git

### Create Azure web services
   - Web app name : Group3-Python
   - Public access address: https://group3-python.azurewebsites.net/
     - Login on Azure portal by gmail or school email address
     - Before creating an Web AppCreate, have to create a Resource Group and a subscription
        - Resource Group holding related web apps
           -  The name of group: Group3-Python-Azure
        - Subscription defining the region and pricing plan
           - Region: central Canada 
           - Price plan: Basic B1
     - Select Web App to create a web app in the menu of Creat a resource menu 
        - current Web App: Group3-Python
     - Important Tip for settings:
        - Deployment Center:
           - settings: github repository is Group3-Python-Azure.git
           - verified by github username and password       
        - configuration:
           - Major version: Python 3
           - Startup Command:python -m streamlit run app.py --server.port 8000 --server.address 0.0.0.0 
        - requirements.txt
           - create a requirements.txt in gitHub repository to import Python libraries 
             - streamlit
             - pandas
             - numpy
### Online Development Github
   - Group3-python-Azure online github repository is associated with Azure web services
   - Sync by Actions on github
   - Check requirments.txt if all libraries have been listed 

### Local Development Visual Studio Code
   - git clone https://github.com/WilliamShi5358/Group3-Python-Azure.git
   - run python on local host: streamlit run app.py
   - before push updates to online github, process 'git pull origin main'
   - and then 
     - git add <specific files> 
     - git commit -m ''
     - git push origin main

### Python app development
   - data loadup
   - show data
   - filter data
   - visualazation data

### Presentation Slides to show the comprehension of the project

### Short Vedio clips to show the output of the project