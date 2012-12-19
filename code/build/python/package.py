### Imports

import glob, shutil, os, sys, argparse


### Constants

# List of available platforms
platformlist    = ['vs2008', 'tutovs2008', 'vs2010', 'tutovs2010', 'mingw', 'tutomingw', 'mac', 'tutomac', 'linux32', 'tutolinux32', 'linux64', 'tutolinux64', 'android', 'android-native', 'doxygen', 'src', 'extern']

# Base source path
basesrc         = '../..'

# Work directory
workdir         = 'workdir'


### Processes command line

# Gets parameters from command line arguments
if __name__ == '__main__':
    parser      = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', default = 'latest')
    parser.add_argument('-p', '--platform', default = 'doxygen', choices = platformlist)
    args        = parser.parse_args()
    version     = args.version
    platform    = args.platform

    # Logs
    print('Version: ' + version)
    print('Platform: ' + platform)


### Variables

# List of file info
basefileinfolist = [
    {'src': '../AUTHORS',                                               'dst': None},
    {'src': '../CHANGELOG',                                             'dst': None},
    {'src': '../COPYRIGHT',                                             'dst': None},
    {'src': '../LICENSE',                                               'dst': None},
    {'src': '../README',                                                'dst': None}
]

docfileinfolist = basefileinfolist

codefileinfolist = basefileinfolist + [
    {'src': 'build/premake4.lua',                                       'dst': None},
]

externfileinfolist = basefileinfolist

devfileinfolist = basefileinfolist + [
    {'src': 'bin/*Template.ini',                                        'dst': '.'}
]

vsfileinfolist = devfileinfolist + [
    {'src': 'lib/dynamic/orx*.dll',                                     'dst': 'lib'},
    {'src': 'lib/dynamic/orx*.lib',                                     'dst': 'lib'},
    {'src': 'lib/dynamic/orx*.pdb',                                     'dst': 'lib'}
]

tutorialvsfileinfolist = [
    {'src': 'lib/dynamic/orx*.lib',                                     'dst': 'lib'},
    {'src': 'lib/dynamic/orx*.pdb',                                     'dst': 'lib'},
    {'src': '../tutorial/build/windows/' + platform[4:] + '/*proj*',    'dst': 'build/windows/' + platform[4:]},
    {'src': '../tutorial/build/windows/' + platform[4:] + '/*.sln',     'dst': 'build/windows/' + platform[4:]}
]

mingwfileinfolist = devfileinfolist + [
    {'src': 'lib/dynamic/orx*.dll',                                     'dst': 'lib'},
    {'src': 'lib/dynamic/liborx*.a',                                    'dst': 'lib'}
]

tutorialmingwfileinfolist = [
    {'src': 'lib/dynamic/liborx*.a',                                    'dst': 'lib'},
    {'src': '../tutorial/build/windows/codeblocks/*.cbp',               'dst': 'build/windows/codeblocks'},
    {'src': '../tutorial/build/windows/codeblocks/*.workspace',         'dst': 'build/windows/codeblocks'},
    {'src': '../tutorial/build/windows/codelite/*.project',             'dst': 'build/windows/codelite'},
    {'src': '../tutorial/build/windows/codelite/*.workspace',           'dst': 'build/windows/codelite'},
    {'src': '../tutorial/build/windows/gmake/*.make',                   'dst': 'build/windows/gmake'},
    {'src': '../tutorial/build/windows/gmake/Makefile',                 'dst': 'build/windows/gmake'}
]

macfileinfolist = devfileinfolist + [
    {'src': 'lib/dynamic/liborx*.dylib',                                'dst': 'lib'}
]

tutorialmacfileinfolist = [
    {'src': 'lib/dynamic/liborx*.dylib',                                'dst': 'lib'},
    {'src': '../tutorial/build/mac/codeblocks/*.cbp',                   'dst': 'build/mac/codeblocks'},
    {'src': '../tutorial/build/mac/codeblocks/*.workspace',             'dst': 'build/mac/codeblocks'},
    {'src': '../tutorial/build/mac/codelite/*.project',                 'dst': 'build/mac/codelite'},
    {'src': '../tutorial/build/mac/codelite/*.workspace',               'dst': 'build/mac/codelite'},
    {'src': '../tutorial/build/mac/gmake/*.make',                       'dst': 'build/mac/gmake'},
    {'src': '../tutorial/build/mac/gmake/Makefile',                     'dst': 'build/mac/gmake'},
    {'src': '../tutorial/build/mac/xcode/Tutorial.xcodeproj/*.pbxproj', 'dst': 'build/mac/xcode/Tutorial.xcodeproj'}
]

linuxfileinfolist = devfileinfolist + [
    {'src': 'lib/dynamic/liborx*.so',                                   'dst': 'lib'}
]

tutoriallinuxfileinfolist = [
    {'src': 'lib/dynamic/liborx*.so',                                   'dst': 'lib'},
    {'src': '../tutorial/build/linux/codeblocks/*.cbp',                 'dst': 'build/linux/codeblocks'},
    {'src': '../tutorial/build/linux/codeblocks/*.workspace',           'dst': 'build/linux/codeblocks'},
    {'src': '../tutorial/build/linux/codelite/*.project',               'dst': 'build/linux/codelite'},
    {'src': '../tutorial/build/linux/codelite/*.workspace',             'dst': 'build/linux/codelite'},
    {'src': '../tutorial/build/linux/gmake/*.make',                     'dst': 'build/linux/gmake'},
    {'src': '../tutorial/build/linux/gmake/Makefile',                   'dst': 'build/linux/gmake'}
]

androidfileinfolist = devfileinfolist + [
    {'src': 'build/android/obj/local/armeabi/liborx*.a',                'dst': 'lib/static/android/armeabi'},
    {'src': 'build/android/obj/local/armeabi-v7a/liborx*.a',            'dst': 'lib/static/android/armeabi-v7a'}
]

androidnativefileinfolist = devfileinfolist + [
    {'src': 'build/android-native/obj/local/armeabi/liborx*.a',         'dst': 'lib/static/android-native/armeabi'},
    {'src': 'build/android-native/obj/local/armeabi-v7a/liborx*.a',     'dst': 'lib/static/android-native/armeabi-v7a'}
]

# List of folder info
docfolderinfolist = [
    {'src': '../doc/html',                                              'dst': None}
]

devfolderinfolist = [
    {'src': 'include',                                                  'dst': None},
    {'src': '../tools/orxCrypt/bin',                                    'dst': 'tools/orxCrypt/bin'},
    {'src': '../tools/orxFontGen/bin',                                  'dst': 'tools/orxFontGen/bin'},
]

tutorialfolderinfolist = [
    {'src': 'include',                                                  'dst': None},
    {'src': '../tutorial/bin',                                          'dst': 'bin'},
    {'src': '../tutorial/data',                                         'dst': 'data'},
    {'src': '../tutorial/src',                                          'dst': 'src'}
]

externfolderinfolist = [
    {'src': '../extern/Box2D_2.1.3',                                    'dst': None},
    {'src': '../extern/dlmalloc',                                       'dst': None},
    {'src': '../extern/freetype-2.4.1',                                 'dst': None},
    {'src': '../extern/glfw-2.7',                                       'dst': None},
    {'src': '../extern/libsndfile-1.0.22',                              'dst': None},
    {'src': '../extern/openal-soft',                                    'dst': None},
    {'src': '../extern/premake',                                        'dst': None},
    {'src': '../extern/SOIL',                                           'dst': None},
    {'src': '../extern/stb_vorbis',                                     'dst': None}
]

androidfolderinfolist = docfolderinfolist + [
    {'src': 'build/android',                                            'dst': None},
    {'src': 'lib/static/android',                                       'dst': None},
    {'src': '../extern/android',                                        'dst': None},
    {'src': '../extern/Box2D_2.1.3/lib/android',                        'dst': None},
    {'src': '../extern/SOIL/lib/android',                               'dst': None},
    {'src': 'demo/android',                                             'dst': None},
    {'src': 'plugins/Display/android',                                  'dst': None},
    {'src': 'plugins/Joystick/android',                                 'dst': None},
    {'src': 'plugins/Keyboard/android',                                 'dst': None},
    {'src': 'plugins/Mouse/android',                                    'dst': None},
    {'src': 'plugins/Physics/Box2D',                                    'dst': None},
    {'src': 'plugins/Render/Home',                                      'dst': None},
    {'src': 'plugins/Sound/android',                                    'dst': None},
    {'src': 'include',                                                  'dst': None},
    {'src': 'src',                                                      'dst': None}
]

androidnativefolderinfolist = docfolderinfolist + [
    {'src': 'build/android-native',                                     'dst': None},
    {'src': 'lib/static/android-native',                                'dst': None},
    {'src': '../extern/nv_and_util',                                    'dst': None},
    {'src': '../extern/Box2D_2.1.3/lib/android-native',                 'dst': None},
    {'src': '../extern/SOIL/lib/android-native',                        'dst': None},
    {'src': 'demo/android-native',                                      'dst': None},
    {'src': 'plugins/Display/android-native',                           'dst': None},
    {'src': 'plugins/Joystick/android-native',                          'dst': None},
    {'src': 'plugins/Keyboard/android-native',                          'dst': None},
    {'src': 'plugins/Mouse/android-native',                             'dst': None},
    {'src': 'plugins/Physics/Box2D',                                    'dst': None},
    {'src': 'plugins/Render/Home',                                      'dst': None},
    {'src': 'plugins/Sound/android-native',                             'dst': None},
    {'src': 'include',                                                  'dst': None},
    {'src': 'src',                                                      'dst': None}
]

codefolderinfolist = [
    {'src': '../tools',                                                 'dst': None},
    {'src': 'bin',                                                      'dst': None},
    {'src': 'build/linux',                                              'dst': None},
    {'src': 'build/mac/xcode/orx-embedded.xcodeproj',                   'dst': None},
    {'src': 'build/mac/codeblocks',                                     'dst': None},
    {'src': 'build/mac/codelite',                                       'dst': None},
    {'src': 'build/mac/gmake',                                          'dst': None},
    {'src': 'build/windows/vs2008',                                     'dst': None},
    {'src': 'build/windows/vs2010',                                     'dst': None},
    {'src': 'build/windows/codeblocks',                                 'dst': None},
    {'src': 'build/windows/codelite',                                   'dst': None},
    {'src': 'build/windows/gmake',                                      'dst': None},
    {'src': 'include',                                                  'dst': None},
    {'src': 'plugins/Demo',                                             'dst': None},
    {'src': 'plugins/Display/GLFW',                                     'dst': None},
    {'src': 'plugins/Joystick/GLFW',                                    'dst': None},
    {'src': 'plugins/Keyboard/GLFW',                                    'dst': None},
    {'src': 'plugins/Mouse/GLFW',                                       'dst': None},
    {'src': 'plugins/Physics/Box2D',                                    'dst': None},
    {'src': 'plugins/Render/Home',                                      'dst': None},
    {'src': 'plugins/Sound/OpenAL',                                     'dst': None},
    {'src': 'src',                                                      'dst': None}
]


### Platform info

platforminfolist = {

    'vs2008': {
        'foldername':       'dev-vs2008',
        'filename':         'dev-vs2008',
        'format':           'zip',
        'fileinfolist':     vsfileinfolist,
        'folderinfolist':   devfolderinfolist
    },

    'tutovs2008': {
        'foldername':       'tutorial-vs2008',
        'filename':         'tutorial-vs2008',
        'format':           'zip',
        'fileinfolist':     tutorialvsfileinfolist,
        'folderinfolist':   tutorialfolderinfolist
    },

    'vs2010': {
        'foldername':       'dev-vs2010',
        'filename':         'dev-vs2010',
        'format':           'zip',
        'fileinfolist':     vsfileinfolist,
        'folderinfolist':   devfolderinfolist
    },

    'tutovs2010': {
        'foldername':       'tutorial-vs2010',
        'filename':         'tutorial-vs2010',
        'format':           'zip',
        'fileinfolist':     tutorialvsfileinfolist,
        'folderinfolist':   tutorialfolderinfolist
    },

    'mingw': {
        'foldername':       'dev-mingw',
        'filename':         'dev-mingw',
        'format':           'zip',
        'fileinfolist':     mingwfileinfolist,
        'folderinfolist':   devfolderinfolist
    },

    'tutomingw': {
        'foldername':       'tutorial-mingw',
        'filename':         'tutorial-mingw',
        'format':           'zip',
        'fileinfolist':     tutorialmingwfileinfolist,
        'folderinfolist':   tutorialfolderinfolist
    },

    'mac': {
        'foldername':       'dev-mac',
        'filename':         'dev-mac',
        'format':           'zip',
        'fileinfolist':     macfileinfolist,
        'folderinfolist':   devfolderinfolist
    },

    'tutomac': {
        'foldername':       'tutorial-mac',
        'filename':         'tutorial-mac',
        'format':           'zip',
        'fileinfolist':     tutorialmacfileinfolist,
        'folderinfolist':   tutorialfolderinfolist
    },

    'linux32': {
        'foldername':       'dev-linux32',
        'filename':         'dev-linux32',
        'format':           'bztar',
        'fileinfolist':     linuxfileinfolist,
        'folderinfolist':   devfolderinfolist
    },

    'tutolinux32': {
        'foldername':       'tutorial-linux32',
        'filename':         'tutorial-linux32',
        'format':           'bztar',
        'fileinfolist':     tutoriallinuxfileinfolist,
        'folderinfolist':   tutorialfolderinfolist
    },

    'linux64': {
        'foldername':       'dev-linux64',
        'filename':         'dev-linux64',
        'format':           'bztar',
        'fileinfolist':     linuxfileinfolist,
        'folderinfolist':   devfolderinfolist
    },

    'tutolinux64': {
        'foldername':       'tutorial-linux64',
        'filename':         'tutorial-linux64',
        'format':           'bztar',
        'fileinfolist':     tutoriallinuxfileinfolist,
        'folderinfolist':   tutorialfolderinfolist
    },

    'android': {
        'foldername':       'dev-android',
        'filename':         'full-android',
        'format':           'zip',
        'fileinfolist':     androidfileinfolist,
        'folderinfolist':   androidfolderinfolist
    },

    'android-native': {
        'foldername':       'dev-android-native',
        'filename':         'full-android-native',
        'format':           'zip',
        'fileinfolist':     androidnativefileinfolist,
        'folderinfolist':   androidnativefolderinfolist
    },

    'doxygen': {
        'foldername':       'doc',
        'filename':         'doc',
        'format':           'zip',
        'fileinfolist':     docfileinfolist,
        'folderinfolist':   docfolderinfolist
    },

    'src': {
        'foldername':       'code',
        'filename':         'src',
        'format':           'zip',
        'fileinfolist':     codefileinfolist,
        'folderinfolist':   codefolderinfolist
    },

    'extern': {
        'foldername':       'extern',
        'filename':         'extern',
        'format':           'zip',
        'fileinfolist':     externfileinfolist,
        'folderinfolist':   externfolderinfolist
    },
}


### Prepares

# Deletes packing folder if present
if os.path.exists(workdir):
    shutil.rmtree(workdir)

# Gets base destination path
basedst = os.path.join(workdir, os.path.join('orx-' + version, platforminfolist[platform]['foldername']))


### Copies folders

# Should copy folders?
if platforminfolist[platform]['folderinfolist']:

    # Creates destination path if needed
    if not os.path.exists(basedst):
        os.makedirs(basedst)

    # For all folder info for this platform
    for folderinfo in platforminfolist[platform]['folderinfolist']:

        # Gets source
        source = os.path.join(basesrc, folderinfo['src'])

        # Exists?
        if os.path.exists(source):

            # Gets destination
            if folderinfo['dst']:
                destination = os.path.join(basedst, folderinfo['dst'])
            else:
                destination = os.path.join(basedst, folderinfo['src'])

            # Does the destination folder exist?
            if os.path.exists(destination):

                # Deletes it
                shutil.rmtree(destination)

            # Logs
            print('Copying folder: ' + folderinfo['src'])

            # Copies folder
            shutil.copytree(source, destination)
        else:

            # Logs
            print('Skipping folder: ' + folderinfo['src'])


### Copies files

# Should copy files?
if platforminfolist[platform]['fileinfolist']:

    # Creates destination path if needed
    if not os.path.exists(basedst):
        os.makedirs(basedst)

    # For all file info for this platform
    for fileinfo in platforminfolist[platform]['fileinfolist']:

        # For all files
        for file in glob.iglob(os.path.join(basesrc, fileinfo['src'])):

            # Gets destination
            if fileinfo['dst']:
                destination = os.path.join(basedst, fileinfo['dst'])
            else:
                destination = os.path.join(basedst, os.path.dirname(os.path.relpath(file, basesrc)))

            # Logs
            print('Copying file: ' + os.path.basename(file))

            # Creates path if needed
            if not os.path.exists(destination):
                os.makedirs(destination)

            # Copies file
            shutil.copy2(file, destination)


### Exports archive

# Creates archive from folder
archive = shutil.make_archive(os.path.join('packages', 'orx-' + platforminfolist[platform]['filename'] + '-' + version), platforminfolist[platform]['format'], workdir, '.')

# Logs
print('Created archive: ' + os.path.basename(archive))