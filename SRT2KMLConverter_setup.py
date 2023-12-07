from SRT2KMLConverter import V
from setup_usr_program import *

INNOSETUP_APP_ID = "AE61073F-3D89-432C-9D9B-EE7C2C13C756"

if __name__=='__main__':
    print(V.PROJECT_VERSION)
    createInstaller(V.PROJECT_NAME, python_ver='39')
    # cleanup(PROJECT_NAME)
    # if sys.platform == 'darwin':
    #     createBundle(PROJECT_NAME, PROJECT_VERSION)
    #     createDmg(PROJECT_NAME, PROJECT_VERSION)
    #if sys.platform == 'win32':
    #    createInnoSetup(V.PROJECT_NAME, V.PROJECT_VERSION, V.COPYRIGHT_HOLDER, INNOSETUP_APP_ID)