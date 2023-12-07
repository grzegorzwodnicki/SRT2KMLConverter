import shutil
import version
import glob
import zipfile
import uuid
from constants import *
import platform
import os
import sys

DIST_PATH = 'dist-win32' if sys.platform == 'win32' else '/tmp/dist-darwin'
original_folder = os.path.dirname(os.path.realpath(__file__))


def isArchitecture64Bit():
    return platform.architecture()[0]=='64bit'

def createInstaller(project_name, python_ver="37"):

    executable = ""
    if 'darwin' in sys.platform:
        executable = "python3 pyinstaller-dev/pyinstaller.py" #"pyinstaller"
        # executable = "pyinstaller" #"pyinstaller"
    else: #windows
        if isArchitecture64Bit():
            python_ver += '-64'
        executable = "pyinstaller.exe"
    # ' --paths "C:\\Windows\\WinXsX\\x86_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.18362.1_none_3da3af2845f54b85" ' \
    launch_string = executable + ' {}.spec --log-level DEBUG -y'.format(getExecutableName(
        project_name))
    # launch_string = executable + ' {}.spec --log-level DEBUG --windowed -y'.format(getExecutableName(project_name))
    # if isArchitecture64Bit():
    #     launch_string += ' --uac-admin '
    print(os.getcwd(), os.path.exists(getExecutableName(project_name)+'.spec'))
    launch_string += ' --distpath {}'.format(DIST_PATH)
    # launch_string += " --key=fWexFwr9PwelDsgn"
    print(launch_string)
    os.system(launch_string)

def cleanup(project_name):
    if sys.platform == 'win32':
        os.chdir('dist-win32/{}'.format(project_name))
        if isArchitecture64Bit():
            manifest_path = "../../manifests/{}.exe.manifest".format(project_name)
            print(manifest_path, 'exists:', os.path.exists(manifest_path))
            if os.path.exists(manifest_path):
                shutil.copy(manifest_path, '.')
        else:
            if os.path.exists('dependencies/vips-dev-8.10'):
                shutil.rmtree('dependencies/vips-dev-8.10')
        for file in glob.glob('api-ms-win-*.dll'):
            os.remove(file)
        for file in [
            # 'PySide2/Qt/plugins/platforms/qwebgl.dll',
            # 'PySide2/Qt/plugins/platforms/qoffscreen.dll',
            # 'PySide2/Qt/plugins/platforms/qminimal.dll'
                ]:
            if os.path.exists(file):
                os.remove(file)
        for path in [#'PySide2/Qt/bin',
                     'PySide2/Qt/translations',
                     'PySide2/QtBluetooth.pyd',
                     # 'Qt5Qml.dll',
                     'Qt5Quick.dll',
                     # 'Qt5WebSockets.dll',
                     'Qt5Designer.dll',
                     # 'Qt5WebEngineCore.dll'
                     ]:
            if os.path.exists(path):
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.unlink(path)
    elif sys.platform == 'darwin':
        os.chdir('/tmp/dist-darwin/{}'.format(project_name))
        # for file in [
        #     'QtWebEngineCore'
        # ]:
        #     if os.path.exists(file):
        #         os.remove(file)
        if 'Video Slicer' in project_name:
            os.makedirs('tcl', exist_ok=True)
            os.makedirs('tk', exist_ok=True)
            print("tcl and tk subdirs created")
            print(os.getcwd())
    os.chdir('../..')

def zip(project_name):
    print("Zipping...")
    zfname = '{}-{}-{}'.format(getExecutableName(project_name), sys.platform, version.getPrefix())
    zfpath = '../../Output/'+zfname + '.zip'
    print(zfpath)
    os.chdir('dist-{}/{}'.format(sys.platform, project_name))
    with zipfile.ZipFile(zfpath, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith('.log'):
                    continue
                else:
                    zf.write(os.path.join(root, file), os.path.join(root, file))

def unlinkLicenseAndLogs(project_name):
    if sys.platform == 'win32':
        if not os.path.exists('dist-win32/{}'.format(project_name)):
            return
        os.chdir('dist-win32/{}'.format(project_name))
    else:
        os.chdir('/tmp/dist-darwin/{}'.format(project_name))
    for file in ['license', 'exif.log', 'errors.log', project_name+'.exe.manifest']:
        if os.path.exists(file):
            print("deleted", file)
            os.unlink(file)
    os.chdir(original_folder)

def createInnoSetup(project_name, project_version, copyright_holder,
                    innosetup_app_id=None):
    unlinkLicenseAndLogs(project_name)
    if not innosetup_app_id:
        innosetup_app_id = str(uuid.uuid3(uuid.NAMESPACE_OID, project_name)).upper()
    if project_name == LOC8_G2:
        iss_name = "loc8_g2_stub.iss"
    else:
        iss_name = "usr.iss"
    with open(iss_name, 'r', encoding='utf-8') as temp:
        iss_template = temp.read()
        iss = iss_template.format(app_id=innosetup_app_id,
                                  project_name=project_name,
                                  project_executable_name=getExecutableName(project_name),
                                  project_version=project_version,
                                  copyright_holder=copyright_holder)
    if isArchitecture64Bit():
        iss = iss.replace('ArchitecturesInstallIn64BitMode=', 'ArchitecturesInstallIn64BitMode=x64')
    if 'Image Slicer' in project_name:
        iss = iss.replace("{commonpf}", "{localappdata}")
    with open(getExecutableName(project_name)+'.iss', 'w', encoding='utf-8') as f:
        f.write(iss)
    executable = '"C:\\Program Files (x86)\\Inno Setup 6\\iscc.exe" {}.iss'.format(getExecutableName(project_name))
    os.system(executable)
    installer_path = "Output//"+getDatedName(project_name, project_version)+".exe"
    if os.path.exists(installer_path):
        os.unlink(installer_path)
    os.rename("Output//{}-{}.exe".format(getExecutableName(project_name), project_version),
              "Output//"+getDatedName(project_name, project_version)+".exe")

def getDatedName(project_name, project_version):
    architecture = 'x64' if isArchitecture64Bit() else 'x86'
    return '{}-{}-{}-{}-{}'.format(getExecutableName(project_name), project_version, sys.platform, architecture,
                                   version.getPrefix())

def getExecutableName(project_name):
    return project_name.replace(' ', '_').replace("/",'2')

def generatePlist(project_name, project_version):
    exec_name = getExecutableName(project_name)
    plist_path = "{}/Bundle/{}.app/Contents/info.plist".format(DIST_PATH, project_name)
    plist_stub_path = "dist-darwin/BundleStub-{}.app/Contents/info.plist.stub".format(exec_name)
    if os.path.exists(plist_path):
        os.unlink(plist_path)
    with open(plist_stub_path, 'r', encoding='utf-8') as f:
        plist_contents = f.read().format(PROJECT_NAME=project_name,
                                         PROJECT_VERSION=project_version)
    with open(plist_path, 'w', encoding='utf-8') as f:
        f.write(plist_contents)

def createBundle(project_name, project_version):
    os.chdir(original_folder)
    print("original_folder=", original_folder)
    print(os.getcwd())
    unlinkLicenseAndLogs(project_name)
    exec_name = getExecutableName(project_name)
    bundle_path = "{}/Bundle/{}.app".format(DIST_PATH, project_name)
    print('exec_name =', exec_name)
    print(bundle_path)
    if os.path.exists(bundle_path):
        shutil.rmtree(bundle_path)
    os.makedirs(bundle_path, exist_ok=True)
    os.makedirs(bundle_path+"/Contents/Resources", exist_ok=True)
    icon_name = 'loc8-icon.icns' if 'USR' not in project_name and 'Beta' not in project_name else 'usr-icon.icns'
    if 'beta' in project_version:
        app_icon_stub = "dist-darwin/BundleStub-{}.app/Contents/Resources/{}".format(exec_name, 'usr-icon.icns')
    else:
        app_icon_stub = "dist-darwin/BundleStub-{}.app/Contents/Resources/{}".format(exec_name, icon_name)
    print(app_icon_stub)
    print(os.getcwd())
    print(os.path.exists(app_icon_stub))
    shutil.copy(app_icon_stub, bundle_path+"/Contents/Resources/{}".format(icon_name))
    generatePlist(project_name, project_version)
    compiled_path = '{}/{}'.format(DIST_PATH, project_name)
    print(compiled_path)
    shutil.copytree(compiled_path,
                bundle_path+"/Contents/MacOS")

def createDmg(project_name, project_version):
    exec_name = getExecutableName(project_name)
    # if 'beta' in project_version:
    #     exec_name += '_beta'
    executable = "appdmg {}_dmg.json /tmp/dist-darwin/{}.dmg".format(exec_name, exec_name)
    # os.system("hdiutil detach /dev/disk2")
    os.system("rm /tmp/dist-darwin/{}.dmg".format(exec_name))
    print(executable)
    os.system(executable)
    shutil.move("/tmp/dist-darwin/{}.dmg".format(exec_name),
                os.path.join(original_folder, "Output/{}.dmg".format(getDatedName(project_name, project_version))))