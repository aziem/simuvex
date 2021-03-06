import simuvex

######################################
# write
######################################

class fwrite(simuvex.SimProcedure):
    #pylint:disable=arguments-differ

    def run(self, src, size, nmemb, file_ptr):
        # TODO handle errors
        data = self.state.memory.load(src, size, "Iend_BE")
        written = self.state.posix.write(file_ptr, data, size*nmemb)

        return written
