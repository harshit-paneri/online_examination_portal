from django.http import HttpResponse
# import git
import os
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def webhook(request):
    if request.method == "POST":
        # repo = git.Repo(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        # origin = repo.remotes.origin
        os.system("./main_script.sh")
        # os.system("source ~/.virtualenvs/online-exam/bin/activate")
        # os.system("git stash -u")
        # origin.pull(os.getenv("MAIN_BRANCH", "main"))
        # os.system("git stash pop")
        # os.system("pip install -r requirements.txt")
        return HttpResponse("Updated Succesfully", status=200)
    else:
        return HttpResponse("Wrong event type", status=400)
