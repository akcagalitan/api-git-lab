from django.shortcuts import render, redirect
from .firebase import db

# Task 3: Add a form to input scores dynamically
def add_student_form(request):
    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "score": int(request.POST.get("score")),
            "subject": request.POST.get("subject"), # Task 1
            "date": request.POST.get("date"),       # Task 1
        }
        db.collection("students").add(data)
        return redirect('dashboard_view')
    return render(request, "input.html")

# Task 1: Fetch all data including Subject and Date
def student_data(request):
    docs = db.collection("students").order_by("date").stream()
    names = []
    scores = []
    
    for doc in docs:
        item = doc.to_dict()
        # Label format: "Name - Subject"
        names.append(f"{item['name']} ({item.get('subject', 'General')})")
        scores.append(item["score"])
        
    return render(request, "dashboard.html", {"names": names, "scores": scores})