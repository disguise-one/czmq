################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
import utils
from . import destructors
libczmq_destructors = destructors.lib

class ZdirPatch(object):
    """
    work with directory patches
    """

    def __init__(self, path, file, op, alias):
        """
        Create new patch
        """
        p = utils.lib.zdir_patch_new(utils.to_bytes(path), file._p, op, utils.to_bytes(alias))
        if p == utils.ffi.NULL:
            raise MemoryError("Could not allocate person")

        # ffi.gc returns a copy of the cdata object which will have the
        # destructor called when the Python object is GC'd:
        # https://cffi.readthedocs.org/en/latest/using.html#ffi-interface
        self._p = utils.ffi.gc(p, libczmq_destructors.zdir_patch_destroy_py)

    def dup(self):
        """
        Create copy of a patch. If the patch is null, or memory was exhausted,
        returns null.
        """
        return utils.lib.zdir_patch_dup(self._p)

    def path(self):
        """
        Return patch file directory path
        """
        return utils.lib.zdir_patch_path(self._p)

    def file(self):
        """
        Return patch file item
        """
        return utils.lib.zdir_patch_file(self._p)

    def op(self):
        """
        Return operation
        """
        return utils.lib.zdir_patch_op(self._p)

    def vpath(self):
        """
        Return patch virtual file path
        """
        return utils.lib.zdir_patch_vpath(self._p)

    def digest_set(self):
        """
        Calculate hash digest for file (create only)
        """
        return utils.lib.zdir_patch_digest_set(self._p)

    def digest(self):
        """
        Return hash digest for patch file
        """
        return utils.lib.zdir_patch_digest(self._p)

    def test(verbose):
        """
        Self test of this class.
        """
        return utils.lib.zdir_patch_test(verbose)

################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################