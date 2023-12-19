from django.db import models
from django.conf import settings

# Create your models here.

# get all request on view ida_all_view without attachement files 
class Request(models.Model):
    request_id = models.IntegerField(primary_key=True)
    REQUEST_NO = models.TextField()
    REQUEST_START_DATE = models.TextField()
    REQUEST_TYPE_NAME = models.TextField()
    FACILITY_NUMBER = models.DateField()
    FACILITY_NAME = models.TextField()
    GOVERNORATE_CODE = models.TextField()
    GOVERNORATE_NAME = models.TextField()
    CITY_CODE = models.TextField()
    CITY_NAME = models.TextField()
    INDUSTRIAL_ZONE_CODE = models.TextField()
    INDUSTRIAL_ZONE_NAME = models.TextField()
    DETAILED_ADDRESS = models.TextField()
    INVESTOR_ID = models.TextField()
    INVESTOR_NAME = models.TextField()
    COMMN_NAME = models.TextField()
    OWNER_NAME = models.TextField()
    CREATION_DATE = models.TextField()
    CREATED_BY = models.TextField()
    REQUESTER_NAME = models.TextField()
    REQUESTER_PHONE = models.TextField()
    CATEGORY_TYPE = models.TextField()
    CEO_PHONE = models.TextField()
    class Meta:
            db_table = 'MSA_REQUESTS' 
            

 
# # lookup for attachement types for request
class Attachements_Type(models.Model):
    ATTACHMENT_TYPE_ID = models.IntegerField(primary_key=True)
    display_name = models.TextField()
    DESCRIPTION = models.TextField()
    class Meta:
            db_table = 'ATTACHMENT_TYPES' 



# # lookup for attachement types for request
class REQUEST_ACTIVITES(models.Model):
    ACTIVITY_ID = models.IntegerField(primary_key=True)
    REQUEST_ID = models.IntegerField()
    ACTIVITY_CODE = models.TextField()
    ACTIVITY_TITLE = models.TextField()
    ACTIVITY_DESCRIPTION = models.TextField()
    NOTIFICATION_TYPE = models.TextField()
    CREATION_DATE = models.TextField()
    class Meta:
            db_table = 'MSA_REQUEST_ACTIVITES' 



# # table For Goves
class Country(models.Model):
    name = models.TextField()






# view for know request for any geha  
class External_Entity(models.Model):
    external_entity_no = models.IntegerField(primary_key=True)
    external_entity_name = models.IntegerField()
    request_id = models.IntegerField()
    class Meta:
            db_table = 'external_entity_view' 




# table many - to - many from requests and attachements files
class Request_Attachements(models.Model):
    ATTACHMENT_ID = models.IntegerField(primary_key=True)
    request_id = models.IntegerField()
    attachment_type = models.ForeignKey(Attachements_Type, on_delete=models.CASCADE)
    attachment_display_name = models.TextField()
    attachment_file_path = models.TextField()
    class Meta:
            db_table = 'msa_request_attachments' 






# response Master Table
class Response(models.Model):
    response_id = models.IntegerField(primary_key=True)
    request_id = models.IntegerField()
    CREATION_DATE = models.DateTimeField()
    CREATED_BY = models.TextField()
    class Meta:
            db_table = 'MSA_RESPONSES'            


# response activites Table
class Response_activites(models.Model):
    activity_id = models.AutoField(primary_key=True)
    RESPONSE_ID = models.IntegerField()
    ACTIVITY_CODE = models.TextField()
    ACTIVITY_TITLE = models.TextField()
    ACTIVITY_DESCRIPTION = models.TextField()
    NOTIFICATION_TYPE = models.TextField()
    CREATION_DATE = models.DateField()
    CREATED_BY = models.TextField()
    class Meta:
            db_table = 'msa_response_activites'


def get_upload_to(self, filename):
    return 'files/%d/%s' % (self.response_id, filename)
# response attachements Table
class Response_attachments(models.Model):
    attachment_id = models.AutoField(primary_key=True)
    attachment_type_id = models.IntegerField()
    attachment_file_path = models.TextField()
    attachment_display_name = models.TextField()
    creation_date = models.DateField()
    created_by = models.IntegerField()
    response_id = models.IntegerField()
    class Meta:
            db_table = 'msa_response_attachments'


class Decision(models.Model):
    decision_id = models.IntegerField(primary_key=True)
    decision_name = models.CharField(max_length=100)
    # Other fields

    class Meta:
        db_table = 'msa_decision'




# response external entites Table
class Response_external_entites(models.Model):
    external_entity_id = models.IntegerField()
    response_external_entity_id = models.AutoField(primary_key=True)
    comments = models.TextField()
    creation_date = models.DateField()
    created_by = models.IntegerField()
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE)
    response_id = models.IntegerField()
    class Meta:
            db_table = 'msa_response_external_entities'



#  tables for he2at 3amleata qooat moslha 
class OPERATIONAL_REQUESTS(models.Model):
    OPERATIONAL_REQUEST_ID = models.AutoField(primary_key=True)
    REQUEST_START_DATE = models.TextField()
    REQUEST_TYPE_NAME = models.TextField()
    REQUESTER_NAME = models.DateField()
    NATIONALITY = models.IntegerField()
    WORK_TYPE = models.TextField()
    WORK_ADDRESS = models.TextField()
    MOBILE_NO = models.TextField()
    SUBJECT = models.TextField()
    CREATION_DATE = models.TextField()
    CREATED_BY = models.TextField()
    REQUEST_ID = models.TextField()
    class Meta:
            db_table = 'MSA_OPERATIONAL_REQUESTS'




class OPERATIONAL_REQUEST_ATTACHMENTS(models.Model):
    ATTACHMENT_ID = models.AutoField(primary_key=True)
    OPERATIONAL_REQUEST_ID = models.TextField()
    ATTACHMENT_TYPE_ID = models.TextField()
    ATTACHMENT_DISPLAY_NAME = models.DateField()
    ATTACHMENT_FILE_PATH = models.IntegerField()
    CREATION_DATE = models.TextField()
    CREATED_BY = models.TextField()
    class Meta:
            db_table = 'MSA_OPERATIONAL_REQUEST_ATTACHMENTS'



class OPERATIONAL_REQUEST_ATTACHMENTS(models.Model):
    ATTACHMENT_ID = models.AutoField(primary_key=True)
    OPERATIONAL_REQUEST_ID = models.TextField()
    ATTACHMENT_TYPE_ID = models.TextField()
    ATTACHMENT_DISPLAY_NAME = models.DateField()
    ATTACHMENT_FILE_PATH = models.IntegerField()
    CREATION_DATE = models.TextField()
    CREATED_BY = models.TextField()
    class Meta:
            db_table = 'MSA_OPERATIONAL_REQUEST_ATTACHMENTS'



class OPERATIONAL_RESPONSES(models.Model):
    RESPONSE_ID = models.AutoField(primary_key=True)
    OPERATIONAL_REQUEST_ID = models.IntegerField()
    COMMENTS = models.TextField()
    CREATION_DATE = models.DateField()
    CREATED_BY = models.TextField()
    DECISION_ID = models.IntegerField()
    class Meta:
            db_table = 'MSA_OPERATIONAL_RESPONSES'



class OPERATIONAL_RESPONSES(models.Model):
    ATTACHMENT_ID = models.AutoField(primary_key=True)
    RESPONSE_ID = models.IntegerField()
    ATTACHMENT_TYPE_ID = models.IntegerField()
    ATTACHMENT_DISPLAY_NAME = models.TextField()
    ATTACHMENT_FILE_PATH = models.TextField()
    CREATION_DATE = models.DateField()
    CREATED_BY = models.TextField()
    class Meta:
            db_table = 'MSA_OPERATIONAL_RESPONSE_ATTACHMENTS'
