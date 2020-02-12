import os

def main():
    print("*****************************************")
    print("***** POC Pre-commit/PMD java hooks *****")
    print("*****************************************")
    
    pmd_bin_path = "/apps/infra/precommit/pmd-bin-6.22.0-SNAPSHOT/bin"
    
    pmd_result = os.system("cd /apps/infra/precommit/poc-pipeline202002 && %d pmd -d java-web-project/src/ -R .pmd_rulset.xml" % pmd_bin_path)
    

    retv = 0
    if(pmd_result != 0):
        print("Execution returned code %d" % pmd_result)
        retv = 1 # Error code 1
    return retv


if __name__ == '__main__':
    exit(main())


