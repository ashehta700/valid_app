from django.shortcuts import render
from . models import *
from django.template import RequestContext
from next_prev import next_in_order, prev_in_order
from django.core.paginator import Paginator
from django.db.models import Q 
from django.db.models import Count
from .forms import *
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
import datetime
import time
from django.utils import timezone
from django.db import connections
import os
from django.http import FileResponse
from django.http import HttpResponse
from urllib.parse import quote


# Create your views here.


def index(request):
    user_id = request.user.id
    # Govs  get all for filter   
    govs =   Country.objects.using('sdi')
    all_requests = Request.objects.using('ida')
    count_requests = all_requests.count()

   
    paginator = Paginator(all_requests, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # user for be2a
    if user_id == 6 :
        external_entities = External_Entity.objects.using('ida').filter(external_entity_no=200)
        all_requests = Request.objects.using('ida').filter(request_id__in=external_entities.values('request_id')).order_by('-CREATION_DATE')
        count_requests = all_requests.count()
        # get all responses for requests for user
        paginator = Paginator(all_requests, 7)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        all_response = Response.objects.using('ida')
        all_response_ext_entit = Response_external_entites.objects.using('ida').filter(external_entity_id__icontains=2)
        # Retrieve the response_ids from the Response_external_entites model
        response_ids = list(Response_external_entites.objects.using('ida').filter(external_entity_id__icontains=2).values_list('response_id', flat=True))
        # Retrieve the request_ids from the Response model using the retrieved response_ids
        request_ids = list(Response.objects.using('ida').filter(response_id__in=response_ids).values_list('request_id', flat=True))
        count_response = all_response_ext_entit.count()
        count_sub = count_requests - count_response     
  
        if request.GET.get('request_num') or request.GET.get('faclilty_number') or request.GET.get('monsh2a_name')  :      
            # requestnumber   
            request_num =  request.GET.get('request_num') 
            # requestnumber   
            faclilty_num =  request.GET.get('faclilty_number') 
            # monsh2a name   
            monsh2a_name =  request.GET.get('monsh2a_name') 
            try:
                shehta = all_requests.filter(REQUEST_NO__icontains=request_num).filter(FACILITY_NUMBER__icontains=faclilty_num).filter(INDUSTRIAL_ZONE_NAME__icontains=monsh2a_name)
                paginator = Paginator(shehta, 5)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request,'index.html',{'data':page_obj,'count_req':count_requests,'num_products':all_response_ext_entit,'count_sub':count_sub,"request_ids":request_ids})
            except:
                return render(request,'index.html',{'data':page_obj,'count_req':count_requests,'num_products':all_response_ext_entit,'count_sub':count_sub,"request_ids":request_ids})
        else:
            return render(request, 'index.html', {'data':page_obj,'count_req':count_requests,'num_products':all_response_ext_entit,'count_sub':count_sub,"request_ids":request_ids})        
    
    # user for teran     
    elif user_id == 7 : 
        external_entity = External_Entity.objects.using('ida').get(external_entity_no = 300)
        all_requests = Request.objects.using('ida').filter(request_id = external_entity.request_id)
        all_response_id = all_response.filter(request_id = external_entity.request_id)
        count_requests = all_requests.count()
        # get all responses for requests for user
        response_user = all_response_ext_entit.filter(response_external_entity_id = 300 )
        paginator = Paginator(all_requests, 7)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if  request.GET.get('s_d') or request.GET.get('e_d'):
            start_date =  request.GET.get('s_d')
            end_date =  request.GET.get('e_d')
            try:
                results = all_requests.filter(request_start_date__range=(
                    start_date,
                    end_date
                ))
                paginator = Paginator(results, 5)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request,'index.html',{"data":page_obj,'count_req':count_requests,'govs':govs,'response_user':response_user})
            except:
                return render(request,'index.html',{"data":page_obj,'count_req':count_requests,'govs':govs,'response_user':response_user})        
        elif request.GET.get('request_num') or request.GET.get('faclilty_number') or request.GET.get('monsh2a_name') or request.GET.get('gov') :      
            # requestnumber   
            request_num =  request.GET.get('request_num') 
            # requestnumber   
            faclilty_num =  request.GET.get('faclilty_number') 
            # monsh2a name   
            monsh2a_name =  request.GET.get('monsh2a_name') 
            # governate  name   
            gov_name =  request.GET.get('gov')
            try:
                shehta = all_requests.filter(request_no__icontains=request_num).filter(facility_number__icontains=faclilty_num).filter(investor_name__icontains=monsh2a_name).filter(governorate_name__icontains=gov_name)
                paginator = Paginator(shehta, 5)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request,'index.html',{"data":page_obj,'count_req':count_requests,'govs':govs,'response_user':response_user})
            except:
                return render(request,'index.html',{'data':page_obj,'count_req':count_requests,'govs':govs,'response_user':response_user})
        else:
            return render(request, 'index.html', {'data':page_obj,'count_req':count_requests,'govs':govs,'response_user':response_user})       
    
    # user for hemaya madania     
    elif user_id == 8 : 
        external_entities = External_Entity.objects.using('ida').filter(external_entity_no=100)
        all_requests = Request.objects.using('ida').filter(request_id__in=external_entities.values('request_id')).order_by('-CREATION_DATE')
        count_requests = all_requests.count()
        # get all responses for requests for user
        paginator = Paginator(all_requests, 7)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        all_response = Response.objects.using('ida')
        all_response_ext_entit = Response_external_entites.objects.using('ida').filter(external_entity_id__icontains=1)
        # Retrieve the response_ids from the Response_external_entites model
        response_ids = list(Response_external_entites.objects.using('ida').filter(external_entity_id__icontains=1).values_list('response_id', flat=True))
        # Retrieve the request_ids from the Response model using the retrieved response_ids
        request_ids = list(Response.objects.using('ida').filter(response_id__in=response_ids).values_list('request_id', flat=True))
        count_response = all_response_ext_entit.count()
        count_sub = count_requests - count_response     
        if request.GET.get('request_num') or request.GET.get('faclilty_number') or request.GET.get('monsh2a_name')  :      
            # requestnumber   
            request_num =  request.GET.get('request_num') 
            # requestnumber   
            faclilty_num =  request.GET.get('faclilty_number') 
            # monsh2a name   
            monsh2a_name =  request.GET.get('monsh2a_name') 
            try:
                shehta = all_requests.filter(REQUEST_NO__icontains=request_num).filter(FACILITY_NUMBER__icontains=faclilty_num).filter(INDUSTRIAL_ZONE_NAME__icontains=monsh2a_name)
                paginator = Paginator(shehta, 5)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request,'index.html',{'data':page_obj,'count_req':count_requests,'num_products':all_response_ext_entit,'count_sub':count_sub,"request_ids":request_ids})
            except:
                return render(request,'index.html',{'data':page_obj,'count_req':count_requests,'num_products':all_response_ext_entit,'count_sub':count_sub,"request_ids":request_ids})
        else:
            return render(request, 'index.html', {'data':page_obj,'count_req':count_requests,'num_products':all_response_ext_entit,'count_sub':count_sub,"request_ids":request_ids})        
     
    
    # user for 3amleat qoat mosla7a     
    elif user_id == 9 : 
        external_entity = External_Entity.objects.using('ida').get(external_entity_no = 400)
        all_requests = OPERATIONAL_REQUESTS.objects.using('ida')
        count_requests = all_requests.count()
        paginator = Paginator(all_requests, 7)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)       
        if request.GET.get('request_num') or request.GET.get('faclilty_number') or request.GET.get('monsh2a_name') or request.GET.get('gov') :      
            # requestnumber   
            request_num =  request.GET.get('request_num') 
            # requestnumber   
            faclilty_num =  request.GET.get('faclilty_number') 
            # monsh2a name   
            monsh2a_name =  request.GET.get('monsh2a_name') 
            # governate  name   
            gov_name =  request.GET.get('gov')
            try:
                shehta = all_requests.filter(request_no__icontains=request_num).filter(facility_number__icontains=faclilty_num).filter(investor_name__icontains=monsh2a_name).filter(governorate_name__icontains=gov_name)
                paginator = Paginator(shehta, 5)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request,'index.html',{"data":page_obj,'count_req':count_requests,'govs':govs})
            except:
                return render(request,'index.html',{'data':page_obj,'count_req':count_requests,'govs':govs})
        else:
            return render(request, 'index.html', {'data':page_obj,'count_req':count_requests})        
    
    return render(request, 'index.html',{'data':page_obj,'count_req':count_requests})



def print_label(request, id):
    requestid = int(id)
    try:
        request_sel = Request.objects.using('ida').get(request_id = requestid)
        # attachement_sel = ('Request_Attachements__REQUEST_ID', 'Request')
        attachement_sel = Request_Attachements.objects.using('ida').filter(request_id = requestid)
        request_activity_sel = REQUEST_ACTIVITES.objects.using('ida').filter(REQUEST_ID__icontains = int(requestid))
        # file_url = settings.MEDIA_URL +attachement_sel.
        external_entity = External_Entity.objects.using('ida').filter(request_id = requestid)
        response_sel = Response.objects.using('ida').filter(request_id = requestid)      
        response_attachments = Response_attachments.objects.using('ida').filter(response_id__in=[response.response_id for response in response_sel]) 
        context={'list':request_sel,'attachement_sel':attachement_sel,'external_entity':external_entity,"response_attachments":response_attachments}
        if response_sel:
            response_external_entites_sel_list = []
            for i in response_sel:
                response_external_entites_sel = Response_external_entites.objects.using('ida').filter(response_id=i.response_id)
                response_external_entites_sel_list.extend(response_external_entites_sel)
            context['response_external_entites_sel'] = response_external_entites_sel_list
            context['request_activity_sel'] = request_activity_sel

        

    except Request.DoesNotExist:
        return redirect('index')
    return render(request, 'label.html', context=context) 



# download files
def download_file(request, attachment_display_name):
    file_path = os.path.join(settings.MEDIA_ROOT, attachment_display_name)
    try:
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{attachment_display_name}"'
            return response
    except FileNotFoundError:
        return HttpResponse('File not found', status=404)

# response for MergeRequest from admin only
def replay(request, id):
    requestid = int(id)    
    try:
        request_sel = Request.objects.using('ida').get(request_id = requestid)
    except Request.DoesNotExist:
        return redirect('index') 
    # Response Form

    user_id = request.user.id
    request_activity_sel = REQUEST_ACTIVITES.objects.using('ida').filter(REQUEST_ID__icontains = int(requestid))
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y%m%d%H%M%S")
    if request.method == 'POST'  : 
        # for user teran madny to response
        if user_id == 7 :  
            # response table
            Response.objects.using('ida').create(
                request_id = requestid
            )
            responseID = Response.objects.using('ida').latest('response_id')
            # entites table
            Response_external_entites.objects.using('ida').create(
                external_entity_id = 528,
                response_external_entity_id = 300,
                comments = request.POST['comment'],
                creation_date = '2021-11-29',
                created_by = 10,
                DESCISION_ID = request.POST['decision'],       
                response_id = responseID.response_id
            ) 
            # activites table
            Response_activites.objects.using('ida').create(
                activity_id = 528,
                request_id = request_sel.request_id,
                activity_code = request_sel.activity_code,
                activity_title = request_sel.activity_title,
                activity_description = request_sel.activity_description,
                notification_type  = request_sel.notification_type           
            )                
            # attach Table
            Response_attachments.objects.using('ida').create(
                attachment_id = 528,
                request_id = 28,
                attachment_type_id = 59,
                attachment_file_path = request.FILES['file1'],
                attachment_display_name = request.FILES['file1'],
                creation_date = '2021-11-29',
                created_by = 10,
                response_id = responseID.response_id

            )
          
        # for user be2a to response
        if user_id == 6 :  
            # response table
            current_datetime = timezone.now()
            response = Response(
                request_id=requestid,
                CREATION_DATE=current_datetime,
                CREATED_BY=6
            )
            response.save(using='ida')
            # Get the last inserted response_id
            with connections['ida'].cursor() as cursor:
                cursor.execute("SELECT response_id FROM MSA_RESPONSES ORDER BY response_id DESC FETCH FIRST 1 ROWS ONLY")
                response_id = cursor.fetchone()[0]   
            response_activites = Response_activites()
            response_activites_list = []
            for activity in request_activity_sel:
                response_activites = Response_activites(
                    RESPONSE_ID=response_id,
                    ACTIVITY_CODE=activity.ACTIVITY_CODE,
                    ACTIVITY_TITLE=activity.ACTIVITY_TITLE,
                    ACTIVITY_DESCRIPTION=activity.ACTIVITY_DESCRIPTION,
                    NOTIFICATION_TYPE=activity.NOTIFICATION_TYPE,
                    CREATION_DATE=current_time,
                    CREATED_BY = 6
                )
            response_activites_list.append(response_activites)

            # Bulk create the response_activites_list
            Response_activites.objects.using('ida').bulk_create(response_activites_list)
            # 
            decision_instance = Decision.objects.using('ida').get(pk=int(request.POST['decision']))
            external_entites = Response_external_entites(
                external_entity_id=2,
                comments=request.POST['comment'],
                creation_date=current_datetime,
                created_by=6,
                decision_id=decision_instance.decision_id,
                response_id=int(response_id)
            )
            external_entites.save(using='ida')
            file1 = request.FILES.get('file1')
            file_extension = file1.name.split('.')[-1]
            file_name = file1.name
            file_directory = os.path.join(settings.MEDIA_ROOT, 'response', str(request_sel.REQUEST_NO))
            os.makedirs(file_directory, exist_ok=True)
            file_path = os.path.join(file_directory, request_sel.REQUEST_NO + "_" + timestamp + "." + file_extension)
            with open(file_path, 'wb') as file:
                for chunk in file1.chunks():
                    file.write(chunk)

            # Replace UNC path with the desired format
            file_path = file_path.replace("\\", "/")
            file_path = file_path.replace(settings.MEDIA_ROOT, "")        
            file_path = file_path.replace("\\\\192.168.160.15\\sharedIntegrationDocument", "/sharedIntegrationDocument")
            file_path = file_path.replace("//192.168.160.15", "")
            ResponseAttachments = Response_attachments(
                attachment_type_id=7,
                attachment_file_path=file_path,
                attachment_display_name=request_sel.REQUEST_NO + "_" + timestamp + "." + file_extension,
                creation_date=current_datetime,
                created_by=6,
                response_id=response_id
            )
            ResponseAttachments.save(using='ida')
            

        # for user  hemaya madania to response
        if user_id == 8 :  
            # response table
            current_datetime = timezone.now()
            response = Response(
                request_id=requestid,
                CREATION_DATE=current_datetime,
                CREATED_BY=8
            )
            response.save(using='ida')
            # Get the last inserted response_id
            with connections['ida'].cursor() as cursor:
                cursor.execute("SELECT response_id FROM MSA_RESPONSES ORDER BY response_id DESC FETCH FIRST 1 ROWS ONLY")
                response_id = cursor.fetchone()[0]   
            response_activites = Response_activites()
            response_activites_list = []
            for activity in request_activity_sel:
                response_activites = Response_activites(
                    RESPONSE_ID=response_id,
                    ACTIVITY_CODE=activity.ACTIVITY_CODE,
                    ACTIVITY_TITLE=activity.ACTIVITY_TITLE,
                    ACTIVITY_DESCRIPTION=activity.ACTIVITY_DESCRIPTION,
                    NOTIFICATION_TYPE=activity.NOTIFICATION_TYPE,
                    CREATION_DATE=current_time,
                    CREATED_BY = 8
                )
            response_activites_list.append(response_activites)

            # Bulk create the response_activites_list
            Response_activites.objects.using('ida').bulk_create(response_activites_list)
            # 
            decision_instance = Decision.objects.using('ida').get(pk=int(request.POST['decision']))
            external_entites = Response_external_entites(
                external_entity_id=1,
                comments=request.POST['comment'],
                creation_date=current_datetime,
                created_by=8,
                decision_id=decision_instance.decision_id,
                response_id=int(response_id)
            )
            external_entites.save(using='ida')
            file1 = request.FILES.get('file1')
            file_extension = file1.name.split('.')[-1]
            file_name = file1.name
            file_directory = os.path.join(settings.MEDIA_ROOT, 'response', str(request_sel.REQUEST_NO))
            os.makedirs(file_directory, exist_ok=True)
            file_path = os.path.join(file_directory, request_sel.REQUEST_NO + "_" + timestamp + "." + file_extension)
            with open(file_path, 'wb') as file:
                for chunk in file1.chunks():
                    file.write(chunk)

            # Replace UNC path with the desired format
            file_path = file_path.replace("\\", "/")
            file_path = file_path.replace(settings.MEDIA_ROOT, "")        
            file_path = file_path.replace("\\\\192.168.160.15\\sharedIntegrationDocument", "/sharedIntegrationDocument")
            file_path = file_path.replace("//192.168.160.15", "")
            ResponseAttachments = Response_attachments(
                attachment_type_id=7,
                attachment_file_path=file_path,
                attachment_display_name=request_sel.REQUEST_NO + "_" + timestamp + "." + file_extension,
                creation_date=current_datetime,
                created_by=8,
                response_id=response_id
            )
            ResponseAttachments.save(using='ida')
            
               
        # for user 3amleat qoat mosla7a  to response
        if user_id == 9 :  
            # response table
            Response.objects.using('ida').create(
                request_id = requestid
            )
            responseID = Response.objects.using('ida').latest('response_id')
            # entites table
            Response_external_entites.objects.using('ida').create(
                external_entity_id = 528,
                response_external_entity_id = 400,
                comments = request.POST['comment'],
                creation_date = '2021-11-29',
                created_by = 10,
                DESCISION_ID = request.POST['decision'],       
                response_id = responseID.response_id
            ) 
            # activites table
            Response_activites.objects.using('ida').create(
                activity_id = 528,
                request_id = request_sel.request_id,
                activity_code = request_sel.activity_code,
                activity_title = request_sel.activity_title,
                activity_description = request_sel.activity_description,
                notification_type  = request_sel.notification_type           
            )                
            # attach Table
            Response_attachments.objects.using('ida').create(
                attachment_id = 528,
                request_id = 28,
                attachment_type_id = 59,
                attachment_file_path = request.FILES['file1'],
                attachment_display_name = request.FILES['file1'],
                creation_date = '2021-11-29',
                created_by = 10,
                response_id = responseID.response_id

            )
           

        return redirect('index')       
    return render(request, 'replay.html', {'list':request_sel}) 

# replay for request
# def replay(request, id):
#     requestid = int(id)
#     try:
#         request_sel = Request.objects.using('ida').get(request_id = requestid)
#         # attachement_sel = ('Request_Attachements__REQUEST_ID', 'Request')
#         attachement_sel = Request_Attachements.objects.using('ida').filter(request_id = requestid)
#         external_entity = External_Entity.objects.using('ida').filter(request_id = requestid)    

#     except Request.DoesNotExist:
#         return redirect('home')
#     return render(request, 'replay.html', {'list':request_sel,'attachement_sel':attachement_sel,'external_entity':external_entity})


    # signup
def signup(request):
    if request.method=='POST':
        form=Signupform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password1')
            user = authenticate(username=username,passord=pwd)
            login(request,user)
            return redirect('index')
    form = Signupform
    return render(request, 'registration/signup.html',{'form':form})  