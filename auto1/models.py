from django.db import models

class ServerGroup ( models.Model ):
    name = models.CharField ( max_length = 200 )

    def __unicode__ ( self ):
        return self.name

class Server ( models.Model ):
    group = models.ForeignKey ( ServerGroup )
    name = models.CharField ( max_length = 200, null = True, blank = True )
    address = models.CharField ( max_length = 200 )


    def __unicode__ ( self ):
        return self.name


class Project ( models.Model ):
    server = models.ManyToManyField ( Server )
    name = models.CharField ( max_length = 200, default = "" )
    repository = models.CharField ( max_length = 255, default = "" )

class Branch ( models.Model ):
    project = models.ForeignKey ( Project )
    

class Task ( models.Model ):
    name = models.CharField ( max_length = 200 )
    
