Here are detailed steps for opening JupyterLab in a cloned GitHub directory. There are some slight differences with MacOS and Windows.

#### Part 0: Make a Conda environment for the course (only the first time)
- Open a command terminal:
    - In Windows: 'Anaconda Prompt' program (**not** the regular Windows command prompt)
    - In MacOS: 'Terminal' application
- Make a new environment by typing or copying this command:
    - `conda create -n 688y jupyterlab` [Enter]
    - This will make a new environment named `688y` with the latest stable version of `jupyterlab` installed on it
    - You can find complete [documentation for managing conda environments here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

#### Part 1: Open a command terminal in your cloned directory
MacOS:
- Right-click on the repository you want to access in the left sidebar in GitHub Desktop
- Click [Open in Terminal]

Windows:
- Right-click on the repository you want to access in the left sidebar in GitHub Desktop
- Click [Copy Repo Path]
- Open the 'Anaconda Prompt' program
- Type `cd`, add a space, then paste your copied path ([ctrl] + [v]) and press [Enter]

#### Part 2: Activate your Conda environment
- Type `conda activate 688y` and press [Enter]

#### Part 3: Run JupyterLab
- Type `jupyter lab` (note that this command is two separate words) and press [Enter]
- Jupyter Lab will automatically open in your default web browser.
- To open it in another browser, you can copy and paste the http address listed in the terminal that looks something like this: `http://localhost:8888/lab?token=1d4864ff4b76b82225b0d8393bc735de7af3462f9dc747f2` 

Leave the command terminal open in the background while you do your work. You can minimize it to keep it out of the way.

If you need to restart JupyterLab, the easiest way is to close the browser window and terminal, then start a new one. You can avoid fully closing the terminal by pressing [control] + [c], which will stop the JupyterLab server and shut down all Python kernels.
