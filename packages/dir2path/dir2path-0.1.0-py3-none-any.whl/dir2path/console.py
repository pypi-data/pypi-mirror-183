import os


supported_shells = {
    "bash": "~/.bashrc",
    "zsh": "~/.zshrc",
}

def run():
    dirp = os.getcwd()
    shell_name = os.environ['SHELL'].split("/")[-1]
    if shell_name in supported_shells:
        shell_config = open(os.path.expanduser(supported_shells[shell_name]), 'a')
        path_append_script = f"export PATH=\"$PATH:{dirp}\"\n"
        shell_config.write(path_append_script)
        shell_config.close()
        print(f"{dirp} appended to $PATH, please reload your shell")
        quit()
    else:
        print(f"Unsupported shell: {system_shell_var}")
        quit(1)
