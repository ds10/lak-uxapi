##  V0.1

class configreader:

    uddurl = ""
    uddusername = ""
    uddpassword=""
    xapiurl= ""
    xapiusername= ""
    xapipassword= ""
    batchfrom= ""
    batchto= ""
    batchsize= ""
    batcherr= ""
    chunksfrom= ""
    chunksto= ""
    moodlename= ""
    moodleurl= ""
    pluginurl= ""
    AES1= ""
    AES2= ""
    datafrom= ""
    logslocation= ""
    uxapilocation = ""
    aggurl = ""
    homepage=""


    def readConfig(self,fileLocation):

        f = open(fileLocation, 'r')
        for row in f:
            row = row[:-1]
            if 'uddurl' in row:
                self.uddurl = row.split('=')[1]
            if 'uddusername' in row:
                self.uddusername = row.split('=')[1]
            if 'uddpassword' in row:
                self.uddpassword = row.split('=')[1]
            if 'xapiurl' in row:
                self.xapiurl = row.split('=')[1]
            if 'xapiusername' in row:
                self.xapiusername = row.split('=')[1]
            if 'xapipassword' in row:
                self.xapipassword = row.split('=')[1]
            if 'batchfrom' in row:
                self.batchfrom = row.split('=')[1]
            if 'batchto' in row:
                self.batchto = row.split('=')[1]
            if 'batchsize' in row:
               self. batchsize = row.split('=')[1]
            if 'batcherr' in row:
                self.batcherr = row.split('=')[1]
            if 'chunksfrom' in row:
                self.chunksfrom = row.split('=')[1]
            if 'chunksto' in row:
                self.chunksto = row.split('=')[1]
            if 'moodlename' in row:
                self.moodlename = row.split('=')[1]
            if 'moodleurl' in row:
                self.moodleurl = row.split('=')[1]
            if 'pluginurl' in row:
                self.pluginurl = row.split('=')[1]
            if 'AES1' in row:
                self.AES1 = row.split('=')[1]
            if 'AES2' in row:
                self.AES2 = row.split('=')[1]
            if 'datafrom' in row:
                 self.datafrom = row.split('=')[1]
            if 'logslocation' in row:
                self.logslocation = row.split('=')[1]
            if 'uxapilocation' in row:
                self.uxapilocation = row.split('=')[1]
            if 'aggurl' in row:
                self.aggurl = row.split('=')[1]
            if 'homepage' in row:
                self.homepage = row.split('=')[1]