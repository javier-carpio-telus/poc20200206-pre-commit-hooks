import os

def main():
    print()
    print("*****************************************")
    print("***** POC Pre-commit/PMD java hooks *****")
    print("*****************************************")
    print()
    print("Starting PMD validations...")
    print()
    pmd_bin_path = "/apps/infra/precommit/pmd-bin-6.22.0-SNAPSHOT/bin"
    command = "cd /apps/infra/precommit/poc-pipeline202002 && {}/run.sh pmd -cache -d java-web-project/src/ -R .pmd_rulset.xml".format(pmd_bin_path)
    
    pmd_stream = os.system(command)
    #pmd_output = pmd_stream.read()

    retv = 0
    if(pmd_stream != 0):
        print()
        print("Execution returned code {}".format(pmd_stream))
        #print(pmd_output)
        retv = 1 # Error code 1
    print()
    print("*****************************************")
    print()
    return retv


if __name__ == '__main__':
    exit(main())


