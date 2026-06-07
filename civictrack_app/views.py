from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from .forms import RegisterForm, IssueForm, IssueUpdateForm
from .models import Issue


def home(request):

    total = Issue.objects.count()

    pending = Issue.objects.filter(
        status='Pending'
    ).count()

    in_progress = Issue.objects.filter(
        status='In Progress'
    ).count()

    resolved = Issue.objects.filter(
        status='Resolved'
    ).count()

    return render(
        request,
        'home.html',
        {
            'total': total,
            'pending': pending,
            'in_progress': in_progress,
            'resolved': resolved,
        }
    )


def about(request):
    return render(request, 'about.html')


def guidelines(request):
    return render(request, 'guidelines.html')


def contact(request):
    return render(request, 'contact.html')


def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Registration successful. Please login.'
            )

            return redirect('login')

    else:

        form = RegisterForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            messages.success(
                request,
                'Login successful.'
            )

            return redirect('dashboard')
        else:

            messages.error(
                request,
                'Invalid username or password.'
            )

    return render(
        request,
        'login.html'
    )


def user_logout(request):

    logout(request)

    messages.success(
        request,
        'Logged out successfully.'
    )

    return redirect('home')


@login_required
def submit_issue(request):

    if request.method == 'POST':

        form = IssueForm(request.POST, request.FILES)

        if form.is_valid():

            issue = form.save(commit=False)
            issue.user = request.user
            issue.save()

            return redirect('my_issues')

    else:
        form = IssueForm()

    return render(
        request,
        'submit_issue.html',
        {'form': form}
    )


@login_required
def my_issues(request):

    issues = Issue.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'my_issues.html',
        {
            'issues': issues
        }
    )


@login_required
def issue_list(request):

    issues = Issue.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'my_issues.html',
        {
            'issues': issues
        }
    )

@login_required
def issue_detail(request, issue_id):

    issue = get_object_or_404(
        Issue,
        id=issue_id,
        user=request.user
    )

    return render(
        request,
        'issue_detail.html',
        {
            'issue': issue
        }
    )

@login_required
def profile(request):

    return render(
        request,
        'profile.html'
    )


@staff_member_required
def authority_dashboard(request):

    status_filter = request.GET.get(
        'status'
    )

    issues = Issue.objects.all().order_by(
        '-created_at'
    )

    if status_filter:

        issues = issues.filter(
            status=status_filter
        )

    return render(
        request,
        'authority_dashboard.html',
        {
            'issues': issues,
            'status_filter': status_filter
        }
    )


@staff_member_required
def update_issue(request, issue_id):

    issue = get_object_or_404(
        Issue,
        id=issue_id
    )

    if request.method == 'POST':

        form = IssueUpdateForm(
            request.POST,
            request.FILES,
            instance=issue
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Issue updated successfully.'
            )

            return redirect(
                'authority_dashboard'
            )

    else:

        form = IssueUpdateForm(
            instance=issue
        )

    return render(
        request,
        'update_issue.html',
        {
            'form': form,
            'issue': issue
        }
    )

@login_required
def dashboard(request):

    total = Issue.objects.filter(
        user=request.user
    ).count()

    pending = Issue.objects.filter(
        user=request.user,
        status='Pending'
    ).count()

    in_progress = Issue.objects.filter(
        user=request.user,
        status='In Progress'
    ).count()

    resolved = Issue.objects.filter(
        user=request.user,
        status='Resolved'
    ).count()

    return render(
        request,
        'home.html',
        {
            'total': total,
            'pending': pending,
            'in_progress': in_progress,
            'resolved': resolved,
        }
    )