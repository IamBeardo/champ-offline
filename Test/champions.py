import csv

class champ(object):
    """Object of a MCOC champion"""

    @classmethod
    def fromHookCSV(cls, row):
        pass
        print (row)
        print ("")

        return cls(row["Id"],int(row["Stars"]),int(row["Rank"]),int(row["Level"]),int(row["Awakened"]),[row["Role"]])
        #OrderedDict([('Id', 'scarletwitch'), ('Stars', '4'), ('Rank', '3'), ('Level', '30'), ('Awakened', '0'), ('Pi', '0'), ('Role', '')])

    def __init__(self, Name="None", Stars=1, Rank=1,Level=1, Sig=0, Tags=None):
        self.Name   = Name
        self.Stars  = Stars
        self.Rank   = Rank
        self.Level  = Level
        self.Sig    = Sig
        self.Awakened= Sig!=0
        self.Prestige = None  # needs lookup

        if Tags is None:
            self.Tags = []
        else:
            self.Tags = Tags

    def __str__(self):
        pass
        return " [{}] {} {} ".format('*'* self.Stars,self.Name,self.Rank)


class champList(object):
    """list of champs"""

    
    def __init__(self):
        self.champs = dict()


    def loadHookCsv(self,f):
        csvreader = csv.DictReader(f)
        
        for row in csvreader:
            newchamp=champ.fromHookCSV(row)
            self.champs["{} {}".format(newchamp.Stars,newchamp.Name)]=newchamp
      
        return self

