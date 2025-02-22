# PyWeber CLI Documentation

The `pyweber-cli` is a command-line interface (CLI) tool designed to help you create and manage PyWeber projects. It provides commands to create new projects and run existing ones. Below is a detailed explanation of the CLI, its commands, and how to use them.

---

## Installation

To use the `pyweber-cli`, ensure you have Python installed and install the required dependencies. You can install the CLI tool using pip:

```bash
pip install pyweber
```
## Commands
### `create-new`

- **Description**: Creates a new PyWeber project with a basic structure.

- **Parameters**:
    - `project_name (str)`: The name of the project to create.

- **Behavior**:
    - Creates a new directory with the specified project_name.
    - Sets up the following structure:
        - `src/style/`: Directory for CSS files.
        - `templates/`: Directory for HTML templates.

    - Generates the following files:
        - `main.py`: The main Python file with a basic PyWeber application structure.
        - `templates/index.html`: A basic HTML template.
        - `src/style/style.css`: A basic CSS file.

- **Error Handling**:
    - If the directory already exists, the CLI will log an error and exit.
    - If any error occurs during project creation, it will log the error and exit.

#### Example
```bash
pyweber-cli create-new my_project
```

### `run`
- **Description**: Runs an existing PyWeber project.

- **Parameters**:
    - file (str, optional): The Python file to run. Defaults to main.py.

- **Behavior**:
    - Attempts to run the specified Python file using the python command.
    - Logs the start of the process and any errors that occur during execution.

- **Error Handling:**
    - If the file cannot be executed, it logs the error and exits.

#### Example
```bash
cd my_project
pyweber run
```