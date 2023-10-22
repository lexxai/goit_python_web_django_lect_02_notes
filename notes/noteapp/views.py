from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Note, Tag

from .forms import NoteForm, TagForm



# Create your views here.

RECORDS_PER_PAGE = 6


def get_page_num(request):
    page_num = request.GET.get('page', 1)
    try:
        page_num = int(page_num)
    except ValueError:
        page_num = 1
    return page_num


def main(request, state: str = "", tag_id: int = 0, page:int = 1):
    page_num =  get_page_num(request)
    flter = state.lower().strip()
    if flter == "done":
        queryset = Note.objects.filter(done=True, user=request.user).order_by("created").all()
    elif flter == "notdone":
        queryset = Note.objects.filter(done=False, user=request.user).all()
    elif tag_id:
        tag = tag_id
        queryset = Note.objects.filter(user=request.user, tags=int(tag)).all()
    else:
        queryset = Note.objects.filter(user=request.user).order_by("created").all()

    paginator = Paginator(queryset, RECORDS_PER_PAGE)
    page_num =  page_num if page_num <= paginator.num_pages else 1 
    try:
        page = paginator.page(page_num)
    except:
        page = []
    notes = (
        page
        if request.user.is_authenticated
        else []
    )

    tag_name = ""
    if tag_id:
        flter = "tag"
        tag_name = get_object_or_404(Tag, pk=tag_id).name

    context = {"notes": notes, "filter": flter, "tag": tag_name, "page_num": page_num}
    return render(request, "noteapp/index.html", context=context)


@login_required
def set_done(request, note_id):
    Note.objects.filter(pk=note_id, user=request.user).update(done=True)
    return redirect(to="noteapp:main")

@login_required
def set_notdone(request, note_id):
    Note.objects.filter(pk=note_id, user=request.user).update(done=False)
    return redirect(to="noteapp:main")


@login_required
def delete_note(request, note_id):
    Note.objects.filter(user=request.user, pk=note_id).delete()
    return redirect(to="noteapp:main")


@login_required
def tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()
            return redirect(to="noteapp:tags")
        else:
            return render(request, "noteapp/tag.html", {"form": form})

    return render(request, "noteapp/tag.html", {"form": TagForm()})


@login_required
def tag_edit(request, tag_id: int):
    tag = get_object_or_404(Tag, pk=tag_id, user=request.user)
    if request.method == "GET":
        print("tag_edit",tag_id, tag.name )
        if tag:
            form = TagForm(instance=tag)
            context = {"form": form, "id": tag_id}
            return render(request, "noteapp/tag.html", context)
    elif request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            # Tag.objects.filter(pk=tag_id, user=request.user).update(name=form.data['name'])
            if form.save():
                messages.info(request, "tag updated")
                return redirect(to="noteapp:tags")
        context = {"form": form, "id": tag_id}
        return render(request, "noteapp/tag.html", context)
    return  redirect(to="noteapp:tags")


@login_required
def tag_delete(request, tag_id):
    if tag_id:
        if Tag.objects.filter(pk=tag_id, user=request.user).delete():
            messages.info(request, "tag deleted")
        else:
            messages.error(request, "tag not deleted")
    return redirect(to="noteapp:tags")



@login_required
def note(request, note_id: int = 0):
    tags = Tag.objects.filter(user=request.user).all()

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.user = request.user
            new_note.save()

            choice_tags = Tag.objects.filter(
                name__in=request.POST.getlist("tags"), user=request.user
            )
            for tag in choice_tags.iterator():
                new_note.tags.add(tag)

            return redirect(to="noteapp:main")
        else:
            return render(request, "noteapp/note.html", {"tags": tags, "form": form})

    return render(request, "noteapp/note.html", {"tags": tags, "form": NoteForm()})


@login_required
def detail(request, note_id, page: int = 1):
    page_num = request.GET.get('page', 1)
    note = get_object_or_404(Note, pk=note_id, user=request.user)
    return render(request, "noteapp/detail.html", {"note": note, "page_num": page_num})


@login_required
def tags(request):
    tags = (
        Tag.objects.filter(user=request.user).all()
        if request.user.is_authenticated
        else []
    )

    return render(request, "noteapp/tags.html", {"tags": tags})


@login_required
def note_edit(request, note_id: int = 0):
    tags = Tag.objects.filter(user=request.user).all()
    note = get_object_or_404(Note, pk=note_id, user=request.user)
    if request.method == "GET":
        note_tags = tags.filter(note=note_id).all()
        print("note_edit", note_tags)
        form = NoteForm(instance=note)
        context = {"tags": tags, "note_tags": note_tags, "form": form}
        return render(request, "noteapp/note.html", context)
    elif request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.user = request.user
            new_note.save()

            choice_tags = Tag.objects.filter(
                name__in=request.POST.getlist("tags"), user=request.user
            )
            for tag in choice_tags.iterator():
                new_note.tags.add(tag)

            return redirect(to="noteapp:main")
        else:
            return render(request, "noteapp/note.html", {"tags": tags, "form": form})

    return render(request, "noteapp/note.html", {"tags": tags, "form": NoteForm()})