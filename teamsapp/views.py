from django.shortcuts import render

# Create your views here.
def team_list(request):
    return render(request, 'teamsapp/team_list.html', {})