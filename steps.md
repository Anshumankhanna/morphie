## How to begin using Mistral AI (courtesy of Anshuman Khanna, because he is a genius and did what wasn't being done after seeing 100's of youtube videos)

- Install python.
- Instal VS Code.
- Yes I wrote these steps to mock.
- Open a folder in VS code (not desktop, make a folder for yourself)
- Now open your terminal
- Follow [this](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) to create a virtual environment.
- After your virtual environment is activated, open the folder **.venv** and open the folder **Lib/site-packages** in it.
- Now install mistral ai using the command `pip install mistralai python-dotenv`.
- Insert another mocking comment here.
- Check if **mistralai** is installed by finding the folder of **mistralai** in **Lib/site-packages**.
- Now go to [here](https://docs.mistral.ai/getting-started/quickstart/#getting-started-with-mistral-ai-api) and copy the first code snippet you see, because that's what the chatgpt generation does (actually use my code).
- Make a file in your original folder (don't make the file inside .venv) names **app.py**.
- In this file copy the code you pasted.
- Now we will set environment variables, create a **.env** file in the same folder and paste the provided API key there using a variable name.
- Now open terminal again (make sure it is running in your current directory, if you don't know what this means, google it, also make sure .venv is activated).
- Run this command: `py app.py`.
- If you have followed the steps nicely, you would have an output.