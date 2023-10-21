from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Note, Tag

from .forms import NoteForm, TagForm


# Create your views here.


def main(request, state: str = "", tag_id: int = 0):
    print("main", state)
    flter = state.lower().strip()
    if flter == "done":
        print("main - onlydone")
        notes = (
            Note.objects.filter(done=True, user=request.user).all()
            if request.user.is_authenticated
            else []
        )
    elif flter == "notdone":
        print("main - onlynotdone")
        notes = (
            Note.objects.filter(done=False, user=request.user).all()
            if request.user.is_authenticated
            else []
        )
    elif tag_id:
        tag = tag_id
        notes = (
            Note.objects.filter(user=request.user, tags=int(tag)).all()
            if request.user.is_authenticated
            else []
        )
    else:
        notes = (
            Note.objects.filter(user=request.user).all()
            if request.user.is_authenticated
            else []
        )
    if tag_id:
        flter = "tag"
    context = {"notes": notes, "filter": flter}
    return render(request, "noteapp/index.html", context=context)


@login_required
def set_done(request, note_id):
    Note.objects.filter(pk=note_id, user=request.user).update(done=True)
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
def note(request):
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
def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id, user=request.user)
    return render(request, "noteapp/detail.html", {"note": note})


@login_required
def tags(request):
    tags = (
        Tag.objects.filter(user=request.user).all()
        if request.user.is_authenticated
        else []
    )

    return render(request, "noteapp/tags.html", {"tags": tags})
