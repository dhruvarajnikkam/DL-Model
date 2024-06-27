from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FarmVideoUploadForm
from core.models import *
from django.http import JsonResponse

from .utils import convert_video_images, save_frame


@login_required
def farm_video_upload(request):
    if request.method == "POST":
        form = FarmVideoUploadForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form.save()
            convert_video_images(form_obj.id)
            return render(request, "users/farm_video_upload.html", {"form": form})

        else:
            return render(request, "users/farm_video_upload.html", {"form": form})

    form = FarmVideoUploadForm()
    return render(request, "users/farm_video_upload.html", {"form": form})

def divide_list(lst):
    # Calculate the length of each sublist
    sublist_length = len(lst) // 10
    
    # Create a list of empty sublists
    sublists = [[] for _ in range(10)]
    
    # Fill each sublist with its corresponding elements from the original list
    for i, item in enumerate(lst):
        sublist_index = i // sublist_length
        sublists[sublist_index].append(item)
    
    return sublists


# create a / for index.html
def index(request):
    return render(request, "index.html")


@login_required
def results(request, request_id):
    farm_video_obj = FarmVideo.objects.get(id=request_id)
    all_frame_images = farm_video_obj.video_farm_images.all()
    l = []
    for i in all_frame_images:
        detact_obj = i.detact_farm_images.all()[0]

        if detact_obj.disease_detected.all() != []:
            for j in detact_obj.disease_detected.all():
                l.append(j)
            # print(detact_obj.disease_detected.all(),i)
    # print(divide_list(l))        
    # print(l,len(l))
    disease_counts = {}
    for disease in l:
        if disease.name in disease_counts:
            disease_counts[disease.name] += 1
        else:
            disease_counts[disease.name] = 1
    key_of_dict = []
    val_of_dict = []

    for i in disease_counts:
        key_of_dict.append(i)
        val_of_dict.append(disease_counts[i])


    total_percentage=sum(val_of_dict)
    good_crops_percetage=round((disease_counts.get("Healthy",0)/total_percentage)*100,2)
    bad_crops_percetage=round(100-good_crops_percetage,2)
    model_disease_dict=[]
    for disease_name in key_of_dict:
        if disease_name!="Healthy":
            disease_obj=Disease.objects.get(name=disease_name)
            model_disease_dict.append(disease_obj)
    context = {
        "key_of_dict": key_of_dict,
        "val_of_dict": val_of_dict,
        "good_crops_percetage": good_crops_percetage,
        "bad_crops_percetage": bad_crops_percetage,
        "model_disease_dict": model_disease_dict,
        "farmer_video":farm_video_obj,
        "disease_counts": disease_counts,
    }



    return render(request, "results.html", context)


@login_required
def your_results(request):
    farmer_video = FarmVideo.objects.filter(user=request.user).order_by("-created")
    # print(farmer_video)

    return render(request, "report_table.html", {"farmer_video": farmer_video})
