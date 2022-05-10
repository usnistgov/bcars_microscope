import os.path


from timeit import default_timer as timer
from time import sleep

import numpy as np
import h5py

def save_location_is_valid(path, filename, groupname, dsetname):
    """Check to see if the dataset is available
    """
    assert '\\' not in path, 'Orient slashes as /'
    assert '\\' not in filename, 'Orient slashes as /'
    assert '\\' not in groupname, 'Orient slashes as /'
    assert '\\' not in dsetname, 'Orient slashes as /'

    does_path_exist = os.path.exists(path)
    print('Path exists: {}'.format(does_path_exist))
    pfname = path.rstrip('/') + '/' + filename.lstrip('/')
    does_file_exist = os.path.exists(pfname)
    # print('Filename exists: {}'.format(pfname))
    if does_path_exist &  (not does_file_exist):  # Path good, file would be new
        print('File does not exist')
        return True
    elif does_path_exist & does_file_exist: # Would be adding to an existing file
        print('File does exist')
        temp = []
        with h5py.File(pfname,'r') as fid:
            fid.visit(lambda x: temp.append(x))
        print(temp)
        does_grp_exist = groupname.lstrip('/').rstrip('/') in temp
        print('Group exists: {}'.format(does_grp_exist))
        # print('Group exists (2): {}'.format())
        does_dset_exist = (groupname.lstrip('/').rstrip('/') + '/' + dsetname.lstrip('/')) in temp
        print(groupname.lstrip('/').rstrip('/') + '/' + dsetname.lstrip('/'))
        print('Dset exists: {}'.format(does_dset_exist))
        del temp
        if does_dset_exist:
            return False
        else:
            return True
        

if __name__ == '__main__':
    # Steps from LabView
    #
    # Just within stack axis for loop
    # Open File H5F
    # Open Group H5G
    # Create Simple
        # H5T Create Type
        # H5S Create Simple
        # H5P Set chunk size
        # H5D create 2?
        # H5T Close type
        # H5S Close space
        # H5P Close properties
    # H5D Get space
    # H5A Write Memo attributes
    # H5A Write array of cluster attributes to attributes
    # H5A Raster.Stack.Position
    # H5A TimeStage.Position
    # Within image for-loop
        # H5S Select simple 
        # H5D Write data (slice)
    # H5F Close File

    sample_path = './'
    sample_filename = 'demo_hdf.h5'
    pfname = sample_path + sample_filename
    sample_groupname = '/grp0/grp0_0'
    sample_dsetname = 'sample_dset_0'

    # This is different than my LabView
    m = 50  # Slow Y-moving
    n = 100 # Fast X-moving
    p = 901 # Spectrum

    data = np.random.randint(0, 2**16, dtype=np.uint16, size=(n,m,p))  # Note not m,n,p b/c iter size with array
    meta = {'Raster.Fast.Axis':'X', 'Raster.Fast.Steps':n, 'Raster.Fast.Start':0, 'Raster.Fast.Stop':n-1}
    meta.update({'Raster.Slow.Axis':'Y', 'Raster.Slow.Steps':m, 'Raster.Slow.Start':0, 'Raster.Slow.Stop':m-1})
    meta.update({'Raster.Fixed.Axis':'Z', 'Raster.Fixed.Steps':1, 'Raster.Fixed.Start':0, 'Raster.Fixed.Stop':0})

    print('Save location is unique: {}'.format(save_location_is_valid(sample_path, sample_filename, sample_groupname, sample_dsetname)))
    ## WINNER BY FAR COMPARED TO OTHER ORIENTATION OF THE DATA
    # SLOW, FAST, SPECTRUM
    # Data is M,N,P
    # Written as counter,N,P
    with h5py.File(sample_filename,'w') as fid:
        grp = fid.create_group(sample_groupname)
        dset = grp.create_dataset(sample_dsetname, shape=(n,m,p), dtype=np.uint16)
        
        tmr = timer()
        for num, d in enumerate(data):
            # print(d.shape)
            dset[num,:,:] = 1*d
        tmr -= timer()
        print('Counter,N,P Timer: {:.3f} sec'.format(-tmr))

        dset.attrs.update(meta)
        dset.attrs.update({'test':123})
        for k in dset.attrs:
            print(k, dset.attrs[k])


