from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from investor.models import Investor, InvestorContact, IdeaLikes
from entreprenuer.models import Entreprenuer, EntreprenuerContact, EntreprenuerIdeas
from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objs as go


def logout(request):
    return redirect('/home/')


def homefunction(request):
    return render(request, "ahome.html")


def servicesfunction(request):
    return render(request, "aservices.html")


def aboutfunction(request):
    return render(request, "aabout.html")


def invdetfunction(request):
    invdet = Investor.objects.all()
    count = Investor.objects.all().count()
    return render(request, "ainvestor.html", {'invdet': invdet, 'count': count})


def invqrfunction(request):
    invqr = InvestorContact.objects.all()
    count = InvestorContact.objects.all().count()
    return render(request, "ainvqueries.html", {'invqr': invqr, 'count': count})


def enpdetfunction(request):
    enpdet = Entreprenuer.objects.all()
    count = Entreprenuer.objects.all().count()
    return render(request, "aentreprenuer.html", {'enpdet': enpdet, 'count': count})


def enpqrfunction(request):
    enpqr = EntreprenuerContact.objects.all()
    count = EntreprenuerContact.objects.all().count()
    return render(request, "aenpqueries.html", {'enpqr': enpqr, 'count': count})


def ereplyfunction(request, subject):
    return render(request, 'aereply.html', {'subject': subject})


def edeletefunction(request, subject):
    EntreprenuerContact.objects.filter(subject=subject).delete()
    return redirect('/crosscutadmin/enpqr')


def ireplyfunction(request, subject):
    return render(request, 'aireply.html', {'subject': subject})


def ideletefunction(request, subject):
    InvestorContact.objects.filter(subject=subject).delete()
    return redirect('/crosscutadmin/invqr')



def indeletefunction(request, email):
    Investor.objects.filter(email=email).delete()
    return redirect('/crosscutadmin/invdet')



def epdeletefunction(request, email):
    Entreprenuer.objects.filter(email=email).delete()
    return redirect('/crosscutadmin/enpdet')


def ereplymailfunction(request, subject):
    if request.method == 'POST':
        body = request.POST['body']
        mail = EntreprenuerContact.objects.values_list('email', flat=True).get(subject=subject)
        fname = EntreprenuerContact.objects.values_list('firstname', flat=True).get(subject=subject)
        EntreprenuerContact.objects.filter(subject=subject).delete()
        subject = 'Regarding your submitted issue to our Crosscut'
        mess = 'Hello ' + fname + '\n' + body
        email = EmailMessage(subject, mess, to=[mail])
        email.send()
    return redirect('/crosscutadmin/enpqr')


def ireplymailfunction(request, subject):
    if request.method == 'POST':
        body = request.POST['body']
        mail = InvestorContact.objects.values_list('email', flat=True).get(subject=subject)
        fname = InvestorContact.objects.values_list('firstname', flat=True).get(subject=subject)
        InvestorContact.objects.filter(subject=subject).delete()
        subject = 'Regarding your submitted issue to our Crosscut'
        mess = 'Hello ' + fname + '\n' + body
        email = EmailMessage(subject, mess, to=[mail])
        email.send()
    return redirect('/crosscutadmin/invqr')


def dashboard(request):
    e = Entreprenuer.objects.all().count()
    i = Investor.objects.all().count()
    eq = EntreprenuerContact.objects.all().count()
    iq = InvestorContact.objects.all().count()
    si = EntreprenuerIdeas.objects.all().count()
    idea = IdeaLikes.objects.values_list('ideaname', flat=True).distinct().order_by()
    ideal = idea[::1]
    likes = []
    for k in ideal:
        likes.append(IdeaLikes.objects.filter(ideaname=k).count())
    m = ['Investors', 'Entreprenuers']
    trace = go.Figure(
        data=[
            go.Scatter(
                name="Original",
                x=m,
                y=[i, e],
            ),
        ],
        layout=go.Layout(
            title="Crosscut Users",
            yaxis_title="No. Of Registrations",
            xaxis_title="Different Types of Users"
        )
    )
    trace2 = go.Figure(
        data=[
            go.Pie(
                name="Original",
                labels=m,
                values=[i, e],
                hole=.3,
            ),
        ],
        layout=go.Layout(
            title="Crosscut Users",
        )
    )
    trace3 = go.Figure(
        data=[
            go.Bar(
                name="Original",
                x=ideal,
                y=likes,
            ),
        ],
        layout=go.Layout(
            title="StartUp Success Rate",
            yaxis_title="No. Of Likes",
            xaxis_title="Different Start Ups"
        )
    )
    trace4 = go.Figure(
        data=[
            go.Scatter(
                name="Original",
                x=ideal,
                y=likes,
            ),
        ],
        layout=go.Layout(
            title="StartUp Success Rate",
            yaxis_title="No. Of Likes",
            xaxis_title="Different Start Ups"
        )
    )

    plot_div = plot(trace, output_type='div')
    plot_pie = plot(trace2, output_type='div')
    plot_like = plot(trace3, output_type='div')
    plot_like2 = plot(trace4, output_type='div')
    return render(request, "agraph.html",
                  context={'plot_div': plot_div, 'plot_pie': plot_pie,'plot_like': plot_like,'plot_like2': plot_like2, 'e': e, 'i': i, 'si': si, 'eq': eq, 'iq': iq})
