import os
import os.path

import h5py

__all__ = ['save_location_is_valid']

def save_location_is_valid(path, filename, groupname):
    """Returns whether the save info (path, file, group) are valid. Note: the group has to not exist.

    Parameters
    ----------
    path : str
        Path
    filename : str
        File name
    groupname : str
        Group name

    Returns
    -------
    bool, str
        Valid bool, str description
    """    
    if path is None:
        return False, 'Path is empty'
    elif filename is None:
        return False, 'Filename is empty'
    elif groupname is None:
        return False, 'Group name is empty'
    elif '\\' in path:
        return False, 'Orient slashes as /'
    elif '\\' in filename:
        return False, 'Orient slashes as /'
    elif '\\' in groupname:
        return False, 'Orient slashes as /'
    else:
        does_path_exist = os.path.exists(path)
        print('Path exists: {}'.format(does_path_exist))
        pfname = path.rstrip('/') + '/' + filename.lstrip('/')
        does_file_exist = os.path.exists(pfname)
        # print('Filename exists: {}'.format(pfname))
        if not does_path_exist:
            return False, 'Path does not exist'
        elif does_path_exist &  (not does_file_exist):  # Path good, file would be new
            return True, 'File does not exist'
        elif does_path_exist & does_file_exist: # Would be adding to an existing file
            print('File does exist') 
            temp = []
            with h5py.File(pfname,'r') as fid:
                fid.visit(lambda x: temp.append(x))
            print(temp)
            does_grp_exist = groupname.lstrip('/').rstrip('/') in temp
            print('Group exists: {}'.format(does_grp_exist))
            if does_grp_exist:
                return False, 'Group exists already. Try again.'
            else:
                return True, 'Group does not exist and will be created.'