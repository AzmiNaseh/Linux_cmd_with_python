from subprocess import PIPE,Popen



def get_grep_output(command):

    sub_call = Popen(command,stdin=PIPE,stdout=PIPE,stderr=PIPE,shell=True)
    stdout,sterr = sub_call.communicate()
    #print(stdout,sterr)
    if stdout:
        return stdout.decode("utf-8")
    else:
        return ""



if __name__ == "__main__"

    list_files_and_folder_command = ("ls -lrt")
    print(get_grep_output(list_files_and_folder_command))
