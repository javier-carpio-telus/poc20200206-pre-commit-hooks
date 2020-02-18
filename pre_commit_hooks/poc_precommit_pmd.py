import os
import argparse

def main(argv=None):

    print(argv)
    pmd_bin_path = "/apps/infra/precommit/pmd-bin-6.22.0-SNAPSHOT/bin"
    workdir = "/apps/infra/precommit/poc-pipeline202002"
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    print()
    print("*****************************************")
    print("***** POC Pre-commit/PMD java hooks *****")
    print("*****************************************")
    print("")
    print("Starting PMD validations...")
    print("")




    for filename in args.filenames:
        print("Filename {}, args: {}".format(filename, args))

    command = "cd {} && {}/run.sh pmd -cache .pmd_cache -d **/src/ -R .pmd_rulset.xml".format(workdir, pmd_bin_path)
    
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


