import os
import argparse
import sys, getopt

def main(): 

    pmd_bin_path = "/apps/infra/precommit/pmd-bin-6.22.0-SNAPSHOT/bin"
    workdir = "/apps/infra/precommit/poc-pipeline202002"

    print("")
    print("*****************************************")
    print("***** POC Pre-commit/PMD java hooks *****")
    print("*****************************************")
    print("")
    print("Starting PMD validations...")
    print("")



    #print(str(sys.argv))
    #args = sys.argv[:1]
    #print(str(args))

    for i in range(1, len(sys.argv)):
        print("** Validating file \"{}\" marked to commit.".format(sys.argv[i]))
        command = "cd {} && {}/run.sh pmd -cache .pmd_cache -d {} -R .pmd_rulset.xml".format(workdir, pmd_bin_path, sys.argv[i])
        pmd_stream = os.system(command)
    
    #pmd_output = pmd_stream.read()

    retv = 0
    if(pmd_stream != 0):
        print("")
        print("Execution returned code {}".format(pmd_stream))
        #print(pmd_output)
        retv = 1 # Error code 1
    print("")
    print("*****************************************")
    print("")
    return retv


if __name__ == '__main__':
    exit(main())


