import simuvex

######################################
# read
######################################

class read(simuvex.SimProcedure):
    #pylint:disable=arguments-differ

    def run(self, fd, dst, length):
        self.state.posix.read(fd, length, dst_addr=dst)
        return length
