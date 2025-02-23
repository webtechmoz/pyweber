from gitpush import subprocess, push
import shutil

def upload_module():
    print('\n============ GIT PUSH ============')

    shutil.rmtree(path='dist', ignore_errors=True)
    shutil.rmtree(path='build', ignore_errors=True)

    subprocess.run(['python', '-m', 'build'], shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(['twine', 'upload', 'dist/*'], shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    push()

if __name__ == '__main__':
    upload_module()