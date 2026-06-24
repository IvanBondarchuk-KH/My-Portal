from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Note
from .forms import RegisterForm
from .forms import ProfileForm
from .forms import NoteForm


def register_view(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(
                form.cleaned_data['password']
            )

            user.save()

            login(request, user)

            return redirect('dashboard')

    else:
        form = RegisterForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )


def login_view(request):

    error = ""

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('dashboard')

        error = "Невірний логін або пароль"

    return render(
        request,
        'login.html',
        {'error': error}
    )


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard_view(request):

    notes = Note.objects.filter(
        user=request.user
    )

    total = notes.count()

    done = notes.filter(
        done=True
    ).count()

    active = notes.filter(
        done=False
    ).count()

    return render(
        request,
        'dashboard.html',
        {
            'total': total,
            'done': done,
            'active': active
        }
    )


@login_required
def profile_view(request):

    profile = request.user.profile

    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            instance=profile
        )

        if form.is_valid():

            profile = form.save()

            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']

            request.user.save()

            return redirect('profile')

    else:

        form = ProfileForm(
            instance=profile,
            initial={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email
            }
        )

    return render(
        request,
        'profile.html',
        {
            'form': form
        }
    )


@login_required
def notes_view(request):

    filter_type = request.GET.get(
        'filter',
        'all'
    )

    notes = Note.objects.filter(
        user=request.user
    )

    if filter_type == 'active':
        notes = notes.filter(done=False)

    elif filter_type == 'done':
        notes = notes.filter(done=True)

    if request.method == 'POST':

        form = NoteForm(request.POST)

        if form.is_valid():

            note = form.save(commit=False)

            note.user = request.user

            note.save()

            return redirect('notes')

    else:
        form = NoteForm()

    return render(
        request,
        'notes.html',
        {
            'notes': notes,
            'form': form
        }
    )


@login_required
def toggle_note(request, note_id):

    note = get_object_or_404(
        Note,
        id=note_id,
        user=request.user
    )

    note.done = not note.done

    note.save()

    return redirect('notes')


@login_required
def delete_note(request, note_id):

    note = get_object_or_404(
        Note,
        id=note_id,
        user=request.user
    )

    note.delete()

    return redirect('notes')