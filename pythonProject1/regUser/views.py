from django.shortcuts import render

app_name = 'regUser'
def  regUserView(request):
    return render(request, 'regUser.html')


def questionnaireView(request):
    foto = request.GET.get('foto')
    firstname = request.GET.get('firstname')
    lastname = request.GET.get('lastname')
    birth = request.GET.get('birth')
    skill_1 = request.GET.get('skill_1')
    skill_2 = request.GET.get('skill_2')
    skill_3 = request.GET.get('skill_3')
    skill_4 = request.GET.get('skill_4')
    skill_5 = request.GET.get('skill_5')
    about = request.GET.get('about')
    context = {
        'foto_html': foto,
        'firstname_html': firstname,
        'lastname_html': lastname,
        'birth_html': birth,
        'skill_1_html': skill_1,
        'skill_2_html': skill_2,
        'skill_3_html': skill_3,
        'skill_4_html': skill_4,
        'skill_5_html': skill_5,
        'about_html': about,
    }
    return render(request, template_name='questionnaire.html',context=context)
def loginUserView(request):

    return render(request, 'loginUser/loginUser.html')