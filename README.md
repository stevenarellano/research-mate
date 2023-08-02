# resmate

resmate is a command-line tool for asking arXiv research papers questions. It is built using Python, the Click library, and arXiv's API.

## Installation

1. Clone or download the resmate repository.
2. Navigate to the repository directory:

```
cd /path/to/resmate
```

3. Make the `resmate` script executable:

```
chmod +x resmate
```

4. Add the resmate directory to your PATH environment variable by adding the following line to your shell's configuration file (e.g., ~/.bashrc, ~/.zshrc, etc.):

```
export PATH="$PATH:/path/to/resmate"
```

5. Save and close the file, and then source the configuration file to apply the changes to your current shell session (any other configuration file for your shell e.g. ~/.zshrc):

```
source ~/.bashrc
source ~/.zshrc
source ~/.bash_profile
```

## Usage

Once you have installed resmate, you can use it to query arxiv research papers. Run the following:

-   `resmate`

For more information on available commands and options, you can run `resmate --help`.

## Misc Setup

.env with the following variables set

1. OPENAI_API_KEY

## Uninstall

1. Open your shell's configuration file (e.g., ~/.bashrc, ~/.zshrc, etc.) in a text editor.
2. Remove the line that you added to add the resmate directory to your PATH environment variable. It should look something like this:

```
export PATH="$PATH:/path/to/resmate"
```

3. Open a terminal session and run the following command to apply the changes to your current session:

```
source ~/.bashrc
```

4. Delete the resmate directory and all its contents from your system. You can do this by running the following command in the directory where the resmate directory is located:

```
rm -rf resmate

```
