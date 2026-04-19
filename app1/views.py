from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from app1.models import Department,Students,Teachers
from app1.forms import StudentForm,TeacherForm,DepartmentForm


def home(request):
    return render(request, 'home.html')

def reg(request):
    message = ""
    if request.method == 'POST':
        user_name = request.POST.get('username')
        email = request.POST.get('useremail')
        p1 = request.POST.get('password1')
        p2 = request.POST.get('confirm')
        if p1 != p2:
            message = "Passwords do not match"
        elif User.objects.filter(email=email).exists():
            message = "Email already exists"
        elif User.objects.filter(username=user_name).exists():
            message = "Username already exists"
        else:
            user = User.objects.create_user(
                username=user_name,
                email=email,
                password=p1
            )
            user.save()
            return redirect('LOG1')
    return render(request, 'register.html', {'message': message})





def login1(request):
    message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        if not username or not password:
            message = "Please fill all fields"
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('HOME')
            else:
                message = "Invalid username or password"
    return render(request, 'login.html', {'message': message})






class department_create(View):
    def get(self, request):
        form = DepartmentForm()
        data = Department.objects.all()
        return render(request, 'dep.html', {
            'form': form,
            'data': data
        })
    def post(self, request):
        form = DepartmentForm(request.POST)
        data = Department.objects.all()
        if form.is_valid():
            form.save()
            return redirect('Dep')
        return render(request, 'dep.html', {
            'form': form,
            'data': data
        })
class department_update(View):
    def get(self, request, id):
        edit_data = get_object_or_404(Department, id=id)
        form = DepartmentForm(instance=edit_data)
        data = Department.objects.all()
        return render(request, 'dep.html', {
            'form': form,
            'data': data,
            'edit': True
        })
    def post(self, request, id):
        edit_data = get_object_or_404(Department, id=id)
        form = DepartmentForm(request.POST, instance=edit_data)
        if form.is_valid():
            form.save()
            return redirect('Dep')
        return redirect('Dep')
class department_delete(View):
    def get(self, request, id):
        return render(request, 'delform.html', {'id': id})
    def post(self, request, id):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            data = get_object_or_404(Department, id=id)
            data.delete()
            return redirect('Dep')
        else:
            return render(request, 'delform.html', {
                'id': id,
                'message': 'Invalid username or password'
            })






class teacher(View):
    def get(self, request):
        form = TeacherForm()
        data = Teachers.objects.all()
        return render(request, 'teach.html', {
            'form': form,
            'data': data
        })
    def post(self, request):
        form = TeacherForm(request.POST)
        data = Teachers.objects.all()
        if form.is_valid():
            form.save()
            return redirect('TEACH')
        return render(request, 'teach.html', {
            'form': form,
            'data': data
        })
class teacher_update(View):
    def get(self, request, id):
        edit_data = get_object_or_404(Teachers, id=id)
        form = TeacherForm(instance=edit_data)
        data = Teachers.objects.all()
        return render(request, 'teach.html', {
            'form': form,
            'data': data,
            'edit': True
        })
    def post(self, request, id):
        edit_data = get_object_or_404(Teachers, id=id)
        form = TeacherForm(request.POST, instance=edit_data)
        if form.is_valid():
            form.save()
            return redirect('TEACH')
        return redirect('TEACH')
class teacher_delete(View):
    def get(self, request, id):
        return render(request, 'delform.html', {'id': id})
    def post(self, request, id):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            data = get_object_or_404(Teachers, id=id)
            data.delete()
            return redirect('TEACH')
        else:
            return render(request, 'delform.html', {
                'id': id,
                'message': 'Invalid username or password'
            })




# CREATE + LIST
class student_create(View):
    def get(self, request):
        form = StudentForm()
        data = Students.objects.all()
        return render(request, 'std.html', {
            'form': form,
            'data': data
        })
    def post(self, request):
        form = StudentForm(request.POST)
        data = Students.objects.all()
        if form.is_valid():
            form.save()
            return redirect('STU')
        return render(request, 'std.html', {
            'form': form,
            'data': data
        })
# UPDATE
class student_update(View):
    def get(self, request, id):
        edit_data = get_object_or_404(Students, id=id)
        form = StudentForm(instance=edit_data)
        data = Students.objects.all()
        return render(request, 'std.html', {
            'form': form,
            'data': data,
            'edit': True
        })
    def post(self, request, id):
        edit_data = get_object_or_404(Students, id=id)
        form = StudentForm(request.POST, instance=edit_data)
        if form.is_valid():
            form.save()
            return redirect('STU')
        return render(request, 'std.html', {
            'form': form,
            'data': Students.objects.all(),
            'edit': True
        })

class student_delete(View):
    def get(self, request, id):
        return render(request, 'delform.html', {'id': id})
    def post(self, request, id):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            data = get_object_or_404(Students, id=id)
            data.delete()
            return redirect('STU')
        else:
            return render(request, 'delform.html', {
                'id': id,
                'message': 'Invalid username or password'
            })
            


  

