# Create your views here.
from django.shortcuts import render_to_response
from auto1.models import ServerGroup, Server

def default ( request ):
    return render_to_response (
        "auto1/default.html",
        {}
    )

def auto1_project_list ( request ):
    return render_to_response (
        "auto1/project_list.html",
        {}
    )
def auto1_project_create ( request ):
    """
    if "POST" == request.method:
        form = TaskCreationForm ( request.POST )
        if form.is_valid ():
            form.save ()

    else:
        form = TaskCreationForm ()
    """

    return render_to_response (
        "auto1/task_project_create.html",
        {
#"form" : form,
        }
    )

def auto1_server_list ( request ):
    return render_to_response (
        "auto1/server_list.html",
        {
            "groups" : ServerGroup.objects.all (),
        }
    )

def auto1_server_create ( request ):
    return render_to_response (
        "auto1/server_create.html",
        {}
    )

