# [Sprint 4 - Software Development Tools (Streamlit)](https://software-development-tools-project-rbzd.onrender.com)

## Skills Learned in Sprint 
- Develop and deploy a web application to a cloud service so that it is accessible to the public

## Libraries Used
 - `pandas` `streamlit` `plotly.express` `altair`

## Problem Statement & Task
Using a car advertisement dataset (vehicles_us.csv), this TripleTen project aims to provide additional practice on common software engineering tasks to develop and deploy a web application to a cloud service.  

If you want to view my project, please access it using this link: [https://software-development-tools-project-rbzd.onrender.com](https://software-development-tools-project-rbzd.onrender.com)

For this project, I've created a Streamlit application hosted on Render that allows users in interact with the car advertisement dataset to uncover insights about what car attributes can increase its value on the secondary market. For additional context, the car advertisement dataset contains information on used car sales such as price, model year, model, car condition, number of cylinders, fuel type, miles on the odometer, transmission type, car type, paint color, four wheel drive, date posted, and days listed. Using data visualization, this project aims to uncover insights about which attributes have a directional impact on price and allows for users to interact with the plots to uncover their own findings. 

## How Was This Web Application Developed

To get the web application deployed on a cloud service that is accessible locally, there are a few steps that had to be completed - 

### Develop and Test Locally
I used VsCode to write my code and develop my project repository locally. In terms of methods and libraries used in local testing, I used pandas, streamlit, and plotly.express. I first read in the csv and convert it to a dataframe. I then did some lite exploratory data analysis and cleaned and transformed the dataset. Using plotly.express I created a few charts to visualize some trends within the car advertisement dataset. Streamlit is used here as a framework to display all of the visualizations when deployed as a web application or when testing locally. 

Once the project compiled and ran locally, I created an account on Render and linked my GitHub repositiory. [Render](https://render.com/) is a cloud solution that can apps and websites with free TLS certificates, global CDN, private networks and auto deploys from Git. Given that the local build ran without error and the folder structure was correct, there are only a few additional changes that must be made to deploy your application to Render. You must 
1. First, we need to create the requirements.txt file. Create this new file in your project folder’s root level. Then, add your project’s required packages. It should look something like this (although you can include other packages):
2. Second, we need to add the configuration file to your git repository. Create the .streamlit directory, then add the config.toml file there (this can all be done with the right-click menu in the left-hand tab of VS Code).This configuration file will tell Render where to look in order to listen to your Streamlit app when hosting it on its servers.
3. Create a new web service linked to your GitHub repository:
4. Configure the new Render web service. To your Build Command, add ```pip install streamlit & pip install -r requirements.txt```
5. To your Start Command, add: streamlit run app.py. It should look like this: ```streamlit run app.py```
6. Deploy to Render, wait for the build to succeed.
    - You should see a link to your site, and if these steps are performed correctly, your Streamlit application should be up and running. 

### How To Run This Project Locally

If you're interested in running this project locally on your own machine, please follow along with the steps provided below - 
1. Clone this repository and store it locally
2. As you add new Streamlit components to develop your application, you can run the ```streamlit run app.py``` command from the terminal to see what the result will look like. Do this on your local machine (preferably from a system terminal) to test that everything works before committing and pushing your changes to your own GitHub repo, if you choose to. 
3. After running ```streamlit run app.py```, you should be able to access your local test deployment using the port [http://0.0.0.0:10000](http://0.0.0.0:10000).
     - If successful, if should see your streamlit displaying your app. However, if unsuccessful, you'll see a message that states a potential cause for an unsuccessful build. Fix the error, save, and run the command again. 
  
## Results & Findings
Thank you for taking the time to view my project. I hope you found my web application engaging and my instructions and project overview to be clear and helpful!

## Examples of Visualizations Used in Project
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2004%20-%20Software%20Development%20Tools%20(Streamlit)/Assets/image.png)
