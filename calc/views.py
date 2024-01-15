from django.shortcuts import render, redirect
from .models import Publication, Experience, Education,Blog,Project,Message


# Create your views here.

def index(request):

	pubs = Publication.objects.all()
	exps = Experience.objects.all()
	edus = Education.objects.all()

	return render(request,'index.html',{'pubs':pubs,'exps':exps, 'edus':edus})
	
def blog_single(request):
	blogs = Blog.objects.all()

	return render(request,'blog_single.html',{'blogs':blogs})

def project_details(request):
	projects = Project.objects.all()

	return render(request,'project_details.html',{'projects':projects})


def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')  # Use get method to avoid potential KeyError
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message_text = request.POST.get('message', '')  # Rename 'message' to avoid conflict with model field name

        # Create a new Message instance and save it to the database
        new_message = Message(name=name, email=email, subject=subject, message=message_text)
        new_message.save()
        # Check for validation errors
        print('Successfully received Message')
        return redirect('/')

    return render(request, 'index.html')

