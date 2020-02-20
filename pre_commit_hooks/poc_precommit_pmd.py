import os
import argparse
import sys, getopt

def main(): 

    pmd_bin_path = "/apps/infra/precommit/pmd-bin-6.22.0-SNAPSHOT/bin"
    workdir = "/apps/infra/actions-runner/_work/fifa-training-sandbox2/fifa-training-sandbox2"

    print("")
    print("***************************************************")
    print("********** POC Pre-commit/PMD java hooks **********")
    print("***************************************************")
    print("")
    print("Starting PMD validations...")
    print("")



    #print(str(sys.argv))
    #args = sys.argv[:1]
    #print(str(args))

    retv = 0
    pmd_steam = 0
    for i in range(1, len(sys.argv)):
        filename = sys.argv[i]
        if filename.endswith(".java") or filename.endswith(".jar"):
            print("** Validating java hooks in file \"{}\" marked to commit.".format(filename))
            command = "cd {} && {}/run.sh pmd -cache .pmd_cache -d {} -R .pmd_rulset.xml".format(workdir, pmd_bin_path, filename)
            print("** Executing command `{}`".format(command))
            pmd_stream = os.system(command)
            print("Execution returned code {}".format(pmd_stream))
            if(retv == 0 and pmd_stream != 0): retv = pmd_stream
        else:
            print("** Skipping file \"{}\" marked to commit.".format(filename))

    
    #pmd_output = pmd_stream.read()

    if(pmd_stream != 0):
        print("")
        #print(pmd_output)
        retv = 1 # Error code 1
    print("")
    print("***************************************************")
    print("Finishing PMD execution. For more information about")
    print("PMD Hooks visit https://pmd.github.io/latest/pmd_rules_java.html")
    print("***************************************************")
    print("")
    return retv


if __name__ == '__main__':
    exit(main())


