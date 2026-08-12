### Use this file to run all stage1 executables for a particular instrument

import os
import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('stage1_file', help="""Enter the name of the stage1 file to be run. e.g., stage1_g395h_nrs1""")
parser.add_argument('-detector', help="""Enter the name of the detector, if more than one detector exists in the cwd, e.g., 'nrs1'""")
args = parser.parse_args()

### Assuming we are in the parent directory where all uncal.fits files are in sub-directories
all_uncal_files = sorted(glob.glob("*%s*/*uncal*"%args.detector))

### Double checking whether we've already run any stage1 extractions, so we don't need to run them again
completed_files = len(sorted(glob.glob("**/*gain*")))

cwd = os.getcwd()

### Now loop over the uncal.fits files that have not yet been processed through stage1
for i in all_uncal_files[completed_files:]:

    print(i)

    ### work out correct file path on the fly
    direc = cwd + "/" + i.split("/")[0] + "/"
    file = i.split("/")[1]
    root = file.split("_uncal.fits")[0]

    ### change into the correct subdirectory
    os.chdir(direc)

    ### run correct stage1 file -- note this stage1 file should have been copied into the parent directory and you need to change the below line to point to the correct stage1 executable
    os.system(". ../%s %s"%(args.stage1_file,root)) # replace [stage1_file] with actual file name, e.g. stage1_g395h_nrs1 or stage1_MIRI
